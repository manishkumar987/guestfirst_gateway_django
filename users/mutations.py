import strawberry
from django.contrib.auth import get_user_model
from users.types import RegisterInput, UserType, LoginInput
from users.utils.jwt import generate_jwt_token
from django.contrib.auth import authenticate
from asgiref.sync import sync_to_async


User = get_user_model()


@strawberry.type
class RegisterResponse:
    success: bool
    user: UserType | None


@strawberry.mutation
async def register_user(input: RegisterInput) -> RegisterResponse:
    user_exists = await sync_to_async(User.objects.filter(email=input.email).exists)()
    if user_exists:
        raise Exception("User already exits")

    user = await sync_to_async(User.objects.create_user)(
        email=input.email, password=input.password
    )
    return RegisterResponse(success=True, user=user)


@strawberry.type
class LoginResponse:
    token: str


@strawberry.mutation
async def login_user(input: LoginInput) -> LoginResponse:
    user = await sync_to_async(authenticate)(email=input.email, password=input.password)
    if not user:
        raise Exception("Invalid credentials")

    token = await sync_to_async(generate_jwt_token)(user.id)
    return LoginResponse(token=token)
