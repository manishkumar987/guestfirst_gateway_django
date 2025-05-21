import strawberry
from users.schema import Mutation
import strawberry_django

@strawberry.type
class Query:
    hello: str = strawberry_django.field(resolver=lambda: "hello")

schema = strawberry.Schema(mutation=Mutation, query=Query)

