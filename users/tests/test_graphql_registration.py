import pytest
from guestfirst_gateway_django.schema import schema
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
def test_register_user_mutation():
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

    result = schema.execute_sync(mutation, variable_values=variables)

    assert result.errors is None, f"Errors: {result.errors}"
    data = result.data["registerUser"]

    assert data["success"] is True
    assert data["user"]["email"] == "newuser@test.com"
    assert User.objects.filter(email="newuser@test.com").exists()
