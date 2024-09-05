from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_db_session
from app.users.auth import AuthService
from app.users.user import UserRepository, UserService


async def get_user_repo(
    session: AsyncSession = Depends(get_db_session)
) -> UserRepository:
    return UserRepository(session)


async def get_user_service(
    user_repo: UserRepository = Depends(get_user_repo),
):
    return UserService(user_repo)


def get_auth_service(
    user_service: UserService = Depends(get_user_service)
):
    return AuthService(user_service)
