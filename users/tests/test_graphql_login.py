import pytest
from django.contrib.auth import get_user_model
from guestfirst_gateway_django.schema import schema
from asgiref.sync import sync_to_async

User = get_user_model()

@pytest.mark.django_db
@pytest.mark.asyncio
async def test_login_user_mutation():
    # Arrange: create a test user
    await sync_to_async(User.objects.create_user)(email="login@test.com", password="secure123")

    # Act: define the mutation and variables
    mutation = """
    mutation LoginUser($input: LoginInput!) {
        loginUser(input: $input) {
            token
        }
    }
    """
    variables = {
        "input": {
            "email": "login@test.com",
            "password": "secure123"
        }
    }

    result = await schema.execute(mutation, variable_values=variables)

    # Assert: ensure no errors and token is returned
    assert result.errors is None, f"GraphQL Errors: {result.errors}"
    data = result.data["loginUser"]
    assert "token" in data
    assert isinstance(data["token"], str)
