import json

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
