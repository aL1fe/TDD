from app.api_exceptions import NotFoundException
from app.contracts import UserRepo

USERS = {
    1: {"id": 1, "name": "Alice"}
}


class InMamoryRepository(UserRepo):
    async def get_user_by_id(self, user_id: int) -> dict:
        user = USERS.get(user_id)
        if not user:
            raise NotFoundException(
                detail=f"User with Id '{user_id}' not found"
            )
        return user


class SqlUserRepository(UserRepo):
    async def get_user_by_id(self, user_id: int) -> dict:
        return {"id": user_id, "name": "Alice"}