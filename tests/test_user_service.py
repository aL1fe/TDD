import pytest
from app.user_service import UserService

from app.api_exceptions import NotFoundException


@pytest.mark.anyio
async def test_get_user_by_id_success():
    user_service = UserService()
    user = await user_service.get_user_by_id(1)
    assert user == {"id": 1, "name": "Alice"}


@pytest.mark.anyio
async def test_get_user_by_id_not_found():
    user_id = 999
    user_service = UserService()
    with pytest.raises(NotFoundException) as exc:
        await user_service.get_user_by_id(user_id)
    assert exc.value.detail == f"User with Id '{user_id}' not found"
