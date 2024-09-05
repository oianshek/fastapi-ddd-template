from app.core import BaseRepository
from app.users.user.model import User


class UserRepository(BaseRepository):

    model = User
