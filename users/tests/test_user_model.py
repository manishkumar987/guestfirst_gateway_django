import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

@pytest.mark.django_db
class TestCustomUser:
    def test_create_user_with_email_successful(self):
        user = User.objects.create_user(email="test@example.com", password="securepass123")
        assert user.email == "test@example.com"
        assert user.check_password("securepass123") is True
        assert user.is_active is True

    def test_email_is_username_field(self):
        assert User.USERNAME_FIELD == "email"

    def test_create_user_without_email_fails(self):
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="testpass")

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        assert admin_user.is_superuser is True
        assert admin_user.is_staff is True
