from unittest.mock import AsyncMock
import pytest

from app.user_repo import UserRepo
from app.api_exceptions import NotFoundException


@pytest.mark.anyio
async def test_get_user_by_id_success():
    user_id = 1
    mock_repo = AsyncMock(spec=UserRepo)
    mock_repo.get_user_by_id.return_value = {"id": user_id, "name": "Alice"}

    user = await mock_repo.get_user_by_id(user_id)
    assert user == {"id": user_id, "name": "Alice"}
    mock_repo.get_user_by_id.assert_awaited_once_with(user_id)


@pytest.mark.anyio
async def test_get_user_by_id_not_found():
    user_id = 999  # non-existent user
    mock_repo = AsyncMock(spec=UserRepo)
    mock_repo.get_user_by_id.side_effect = NotFoundException(detail=f"User with Id '{user_id}' not found")

    with pytest.raises(NotFoundException) as exc:
        await mock_repo.get_user_by_id(user_id)
    assert f"User with Id '{user_id}' not found" in str(exc.value.detail)
    mock_repo.get_user_by_id.assert_awaited_once_with(user_id)
