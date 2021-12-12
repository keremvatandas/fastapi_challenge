from core.config import API_PREFIX
from fastapi import status


def test_get_apps(client, access_token) -> None:
    response = client.get(
        f"{API_PREFIX}/get_apps", headers={"Authorization": f"Bearer {access_token}"}
    )
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(result) == 10
    assert result[0]["name"] == "Roller Splat!"


def test_fail_get_apps_without_token(client) -> None:
    response = client.get(
        f"{API_PREFIX}/get_apps", headers={"Authorization": f"Bearer"}
    )
    result = response.json()
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert result["detail"] == "Not authenticated"


def test_fail_get_apps_with_invalid_token(client) -> None:
    response = client.get(
        f"{API_PREFIX}/get_apps", headers={"Authorization": f"Bearer INVALID"}
    )
    result = response.json()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert result["detail"] == "Invalid token"


def test_get_screenshots(client, access_token) -> None:
    response = client.get(
        f"{API_PREFIX}/get_screenshots/51",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(result) == 5
    assert result[0] == "/static/images/ss/XJrscctNsw.jpg"


def test_fail_get_screenshots_without_token(client) -> None:
    response = client.get(
        f"{API_PREFIX}/get_screenshots/51", headers={"Authorization": f"Bearer"}
    )
    result = response.json()
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert result["detail"] == "Not authenticated"


def test_fail_get_screenshots_with_invalid_token(client) -> None:
    response = client.get(
        f"{API_PREFIX}/get_screenshots/51", headers={"Authorization": f"Bearer INVALID"}
    )
    result = response.json()
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert result["detail"] == "Invalid token"


def test_fail_get_screenshots_with_invalid_token2(client, access_token) -> None:
    """invalid parameter"""
    response = client.get(
        f"{API_PREFIX}/get_screenshots/",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    result = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert result["detail"] == "Not Found"
