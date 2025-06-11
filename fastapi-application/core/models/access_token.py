from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    """
    Модель токена доступа для хранения в базе данных.

    Эта модель используется FastAPI Users для управления access-токенами,
    которые выдаются при аутентификации пользователя. Она связывает токен с
    конкретным пользователем через внешний ключ `user_id`.

    Наследуется от:
    - Base: базовый класс SQLAlchemy моделей;
    - SQLAlchemyBaseAccessTokenTable: предоставляет поля токена (`token`, `created_at`, и т.д.).

    Атрибуты:
        user_id (UserIdType): внешний ключ, указывающий на ID пользователя.
    """

    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """
        Возвращает адаптер доступа к таблице access-токенов.

        Этот метод создаёт объект `SQLAlchemyAccessTokenDatabase`,
        позволяющий работать с access-токенами в базе данных через асинхронную сессию.

        Параметры:
            session (AsyncSession): асинхронная сессия SQLAlchemy.

        Возвращает:
            SQLAlchemyAccessTokenDatabase: адаптер для доступа к токенам.
        """
        return SQLAlchemyAccessTokenDatabase(session, cls)
