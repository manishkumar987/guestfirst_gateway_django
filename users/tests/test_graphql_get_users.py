import pytest
from guestfirst_gateway_django.schema import schema
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

User = get_user_model()


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_get_users_query():
    # Arrange: Create 2 users
    await sync_to_async(User.objects.create_user)(email="user1@example.com", password="password1")
    await sync_to_async(User.objects.create_user)(email="user2@example.com", password="password2")

    # Define the query
    query = """
    query {
        users {
            id
            email
        }
    }
    """

    # Act: Execute the query
    result = await schema.execute(query)

    # Assert: No errors
    assert result.errors is None, f"Errors: {result.errors}"

    users = result.data["users"]
    assert len(users) == 2

    emails = [user["email"] for user in users]
    assert "user1@example.com" in emails
    assert "user2@example.com" in emails
