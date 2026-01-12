from abc import ABC, abstractmethod

class UserRepo(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> dict:
        pass
