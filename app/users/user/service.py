from dataclasses import dataclass
from uuid import UUID

from app.users.user.repository import UserRepository


@dataclass
class UserService:
    repo: UserRepository

    async def get_one(self, id: UUID):
        return await self.repo.get_one(id)
