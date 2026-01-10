from app.exceptions import UserNotFoundError


USERS = {
    1: {"id": 1, "name": "Alice"}
}


class UserService():
    async def get_user_by_id(self, user_id: int) -> dict:
        user = USERS.get(user_id)
        if not user:
            raise UserNotFoundError()
        return user


# Функция-фабрика для Dependency Injection
def get_user_service() -> UserService:
    return UserService()
