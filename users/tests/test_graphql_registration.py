import pytest
from guestfirst_gateway_django.schema import schema
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

User = get_user_model()

@pytest.mark.django_db
@pytest.mark.asyncio
async def test_register_user_mutation():
    mutation = """
    mutation RegisterUser($input: RegisterInput!) {
        registerUser(input: $input) {
            success
            user {
                id
                email
            }
        }
    }
    """

    variables = {
        "input": {
            "email": "newuser@test.com",
            "password": "strongpassword123"
        }
    }

    result = await schema.execute(mutation, variable_values=variables)

    assert result.errors is None, f"Errors: {result.errors}"
    data = result.data["registerUser"]

    assert data["success"] is True
    assert data["user"]["email"] == "newuser@test.com"
   
    exists = await sync_to_async(User.objects.filter(email="newuser@test.com").exists)()
    assert exists

