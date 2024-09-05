from dataclasses import dataclass

from app.users.user import UserService


@dataclass
class AuthService:
    user_service: UserService

    async def login(self, body):
        pass

