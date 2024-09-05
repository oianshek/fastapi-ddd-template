from typing import Annotated
from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Depends

from app.users.dependency import get_user_service
from app.users.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get('/users/{id}')
async def get_one(
    id: UUID,
    service: Annotated[UserService, Depends(get_user_service)]
):
    return await service.get_one(id=id)
