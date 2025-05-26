import strawberry
from users.schema import Mutation as UserMutation
from users.queries import Query as UserQuery
# from users.utils.extension import AuthExtension
# from strawberry.extensions import AddValidationRules


@strawberry.type
class Query(UserQuery):
    pass


# can inherit all mutation to Mutation
@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(mutation=Mutation, query=Query)
