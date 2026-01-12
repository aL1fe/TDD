import pytest

from app.user_repo import UserRepo
from app.api_exceptions import NotFoundException


@pytest.mark.anyio
async def test_get_user_by_id_success():
    repo = UserRepo()

    user = await repo.get_user_by_id(1)

    assert user == {"id": 1, "name": "Alice"}


@pytest.mark.anyio
async def test_get_user_by_id_not_found():
    repo = UserRepo()

    with pytest.raises(NotFoundException) as exc:
        await repo.get_user_by_id(999)

    assert "User with Id '999' not found" in str(exc.value.detail)
