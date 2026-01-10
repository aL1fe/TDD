from app.api_exceptions import NotFoundException


USERS = {
    1: {"id": 1, "name": "Alice"}
}


class UserService():
    async def get_user_by_id(self, user_id: int) -> dict:
        user = USERS.get(user_id)
        if not user:
            raise NotFoundException(detail=f"User with Id '{user_id}' not found")
        return user


# Fabrice function for dependency injection
def get_user_service() -> UserService:
    return UserService()
