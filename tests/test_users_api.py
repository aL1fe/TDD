from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

from app.api_exceptions import NotFoundException
from app.main import app


client = TestClient(app)


def test_get_user_endpoint(monkeypatch):
    user_id = 1
    user_service = AsyncMock()
    user_service.get_user_by_id.return_value = {"id": user_id, "name": "Alice"}

    # replacing the service factory from Depends with our mock
    monkeypatch.setattr("app.main.get_user_service", lambda: user_service)

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_id, "name": "Alice"}


def test_get_user_by_id_not_found(monkeypatch):
    user_id = 999  # non-existent user
    user_service = AsyncMock()
    user_service.side_effect = NotFoundException(detail=f"User with Id '{user_id}' not found")

    monkeypatch.setattr("app.main.get_user_service", lambda: user_service)

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404 
    assert response.json() == { "detail": f"User with Id '{user_id}' not found", 'extra': {}, 'error_code': 'not_found' }
