from typing import List
import strawberry
from users.types import UserType
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

User = get_user_model()


@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> List[UserType]:
        return await sync_to_async(list)(User.objects.all())
