from app.user_repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo


    async def get_user_by_id(self, user_id: int) -> dict:
        user = await self.user_repo.get_user_by_id(user_id)
        return user


# Fabrice function for dependency injection
def get_user_service() -> UserService:
    return UserService(UserRepo())
