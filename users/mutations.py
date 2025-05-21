import strawberry
from django.contrib.auth import get_user_model
from users.types import RegisterInput, UserType, LoginInput
from users.utils.jwt import generate_jwt_token
from django.contrib.auth import authenticate


User = get_user_model()

@strawberry.type
class RegisterResponse:
    success: bool
    user: UserType | None

@strawberry.mutation
def register_user(input: RegisterInput) -> RegisterResponse:
    if User.objects.filter(email=input.email).exists():
        return RegisterResponse(success=False, user=None)

    user = User.objects.create_user(email=input.email, password=input.password)
    return RegisterResponse(success=True, user=user)

@strawberry.type
class LoginResponse:
    token: str

@strawberry.mutation
def login_user(input: LoginInput) -> LoginResponse:
    user = authenticate(email=input.email, password=input.password)
    if not user:
        raise Exception("Invalid credentials")

    token = generate_jwt_token(user.id)
    return LoginResponse(token=token)
