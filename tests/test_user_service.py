import pytest
from app.user_service import UserService

from app.exceptions import UserNotFoundError


@pytest.mark.anyio
async def test_get_user_by_id_success():
    user_service = UserService()
    user = await user_service.get_user_by_id(1)
    assert user == {"id": 1, "name": "Alice"}


@pytest.mark.anyio
async def test_get_user_by_id_not_found():
    user_service = UserService()
    with pytest.raises(UserNotFoundError) as exc:
        await user_service.get_user_by_id(999)
    assert exc.value.message == "User not found"
