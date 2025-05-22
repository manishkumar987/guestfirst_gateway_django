import strawberry
from users.schema import Mutation as UserMutation
import strawberry_django

@strawberry.type
class Query:
    hello: str = strawberry_django.field(resolver=lambda: "hello")


# can inherit all mutation to Mutation
@strawberry.type
class Mutation(UserMutation): 
    pass

schema = strawberry.Schema(mutation=Mutation, query=Query)

