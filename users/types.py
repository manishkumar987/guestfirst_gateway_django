import strawberry
import strawberry_django
from django.contrib.auth import get_user_model

User = get_user_model()

@strawberry.input
class RegisterInput:
    email: str
    password: str

@strawberry_django.type(User)
class UserType:
    id: strawberry.ID
    email: str


@strawberry.input
class LoginInput:
    email: str
    password: str
