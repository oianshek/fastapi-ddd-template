from app.users.auth import router as auth_router
from app.users.user import router as user_router

users_routers = [user_router, auth_router]

__all__ = ['users_routers']
