import json

from core.config import API_PREFIX
from fastapi import status


def test_signup(client) -> None:
    data = {"username": "kerem", "password": "123123"}
    response = client.post(f"{API_PREFIX}/signup", json.dumps(data))
    result = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert result == {"result": True, "message": "Created successfully."}


def test_signup_missing_data(client) -> None:
    data = {"password": "123123"}
    response = client.post(f"{API_PREFIX}/signup", json.dumps(data))
    result = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert result == {"detail": "Missing parameter."}


def test_login(client) -> None:
    data = {"username": "test", "password": "test"}
    response = client.post(f"{API_PREFIX}/login", json.dumps(data))
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result.get("access_token", None) is not None


def test_login_without_username(client) -> None:
    data = {"password": "test"}
    response = client.post(f"{API_PREFIX}/login", json.dumps(data))
    result = response.json()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert result == {"detail": "Invalid username"}


def test_login_invalid_password(client) -> None:
    data = {"username": "test", "password": "test1"}
    response = client.post(f"{API_PREFIX}/login", json.dumps(data))
    result = response.json()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert result == {"detail": "Invalid password"}


def test_refresh_token(client, refresh_token) -> None:
    response = client.get(
        f"{API_PREFIX}/refresh_token",
        headers={"Authorization": f"Bearer {refresh_token}"},
    )
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result.get("access_token") is not None


def test_refresh_token_fail(client, access_token) -> None:
    response = client.get(
        f"{API_PREFIX}/refresh_token",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    result = response.json()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert result["detail"] == "Invalid scope for token"
