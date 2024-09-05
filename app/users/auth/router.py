from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from app.users.auth import LoginSchema, AuthService
from app.users.dependency import get_auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login")
async def login(
    body: LoginSchema,
    service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await service.login(body=body)
