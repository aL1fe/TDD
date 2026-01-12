from unittest.mock import AsyncMock
import pytest
from app.user_service import UserService

from app.api_exceptions import NotFoundException


@pytest.mark.anyio
async def test_get_user_by_id_success():
    user_id = 1
    repo = AsyncMock()
    repo.get_user_by_id.return_value = {"id": user_id, "name": "Alice"}

    user_service = UserService(repo)
    user = await user_service.get_user_by_id(user_id)
    assert user == {"id": user_id, "name": "Alice"}
    repo.get_user_by_id.assert_awaited_once_with(user_id)


@pytest.mark.anyio
async def test_get_user_by_id_not_found():
    user_id = 999
    repo = AsyncMock()
    repo.get_user_by_id.side_effect = NotFoundException(detail=f"User with Id '{user_id}' not found")

    user_service = UserService(repo)
    with pytest.raises(NotFoundException) as exc:
        await user_service.get_user_by_id(user_id)
    assert exc.value.detail == f"User with Id '{user_id}' not found"
