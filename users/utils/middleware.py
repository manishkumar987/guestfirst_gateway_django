from django.http import JsonResponse
from django.conf import settings
import jwt  # You'd need a library like PyJWT


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define paths that don't require authentication
        self.unauthenticated_paths = ["/graphql/"]
        self.exempt_paths_prefixes = ["/admin/", "/static/"]  # Allow all /admin/*

    def __call__(self, request):
        # Allow OPTIONS requests to pass through (important for CORS preflight)
        if request.method == "OPTIONS":
            return self.get_response(request)

        # Skip authentication for exempt paths (like admin, static, etc.)
        if any(
            request.path.startswith(prefix) for prefix in self.exempt_paths_prefixes
        ):
            return self.get_response(request)

        # Allow login/register GraphQL mutations
        if request.path == "/graphql/" and request.method == "POST":
            try:
                import json

                body = json.loads(request.body)
                query = body.get("query", "")
                if "mutation LoginUser" in query or "mutation RegisterUser" in query:
                    return self.get_response(request)
            except json.JSONDecodeError:
                pass  # Handle malformed JSON if necessary

        # Perform JWT authentication
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"error": "Authentication credentials not provided."}, status=401
            )

        token = auth_header.split(" ")[1]

        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get("user_id")
            if not user_id:
                raise ValueError("Token does not contain user_id.")

            from django.contrib.auth import get_user_model

            User = get_user_model()
            request.user = User.objects.get(id=user_id)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired."}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token."}, status=401)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=401)
        except Exception as e:
            return JsonResponse(
                {"error": f"Authentication error: {str(e)}"}, status=401
            )

        return self.get_response(request)
