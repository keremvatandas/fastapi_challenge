from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from passlib.context import CryptContext
from routes.exceptions import (
    EXPIRED_TOKEN,
    INVALID_REFRESH_TOKEN,
    INVALID_SCOPE_TOKEN,
    INVALID_TOKEN,
    REFRESH_TOKEN_EXP,
)

from core.config import API_ALGORITHM, SECRET_KEY


class Auth:

    hasher = CryptContext(schemes=["bcrypt"])
    secret = SECRET_KEY

    def encode_password(self, password: str) -> str:
        return self.hasher.hash(password)

    def verify_password(self, password: str, encoded_password: str) -> str:
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, username: str) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
            "iat": datetime.utcnow(),
            "scope": "access_token",
            "sub": username,
        }
        return jwt.encode(payload, self.secret, algorithm=API_ALGORITHM)

    def decode_token(self, token: str) -> Dict[str, Any]:
        try:
            payload = jwt.decode(token, self.secret, algorithms=[API_ALGORITHM])
            if payload["scope"] == "access_token":
                return payload["sub"]
            raise INVALID_SCOPE_TOKEN
        except jwt.ExpiredSignatureError:
            raise EXPIRED_TOKEN
        except jwt.InvalidTokenError:
            raise INVALID_TOKEN

    def encode_refresh_token(self, username: str) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, hours=10),
            "iat": datetime.utcnow(),
            "scope": "refresh_token",
            "sub": username,
        }
        return jwt.encode(payload, self.secret, algorithm=API_ALGORITHM)

    def refresh_token(self, refresh_token: str) -> str:
        try:
            payload = jwt.decode(refresh_token, self.secret, algorithms=[API_ALGORITHM])
            if payload["scope"] == "refresh_token":
                username = payload["sub"]
                new_token = self.encode_token(username)
                return new_token
            raise INVALID_SCOPE_TOKEN
        except jwt.ExpiredSignatureError:
            raise REFRESH_TOKEN_EXP
        except jwt.InvalidTokenError:
            raise INVALID_REFRESH_TOKEN
