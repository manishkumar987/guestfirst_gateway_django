import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings


def generate_jwt_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=7),
        "iat": datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token
