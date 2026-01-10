from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

from app.main import app


client = TestClient(app)


def test_get_user_by_id_success():
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Alice"
    }


def test_get_user_endpoint(monkeypatch):
    mock_service = AsyncMock()
    mock_service.get_user_by_id.return_value = {"id": 1, "name": "Alice"}

    # replacing the service factory with our mock
    monkeypatch.setattr("app.main.get_user_service", lambda: mock_service)

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Alice"}


def test_get_user_by_id_not_found(): 
    response = client.get("/users/999")  # non-existent user
    assert response.status_code == 404 
    assert response.json() == { "detail": "User with Id '999' not found", 'extra': {}, 'error_code': 'not_found' }
