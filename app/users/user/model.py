from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from app.core import BaseModel


class User(BaseModel):

    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()


class UserSettings(BaseModel):

    __tablename__ = 'user_settings'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
