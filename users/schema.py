import strawberry
from users.mutations import register_user, login_user

@strawberry.type
class Mutation:
    register_user = register_user
    login_user = login_user 