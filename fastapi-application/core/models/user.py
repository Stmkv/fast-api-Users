from typing import TYPE_CHECKING
from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from core.types.user_id import UserIdType
from .base import Base
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):  # type: ignore[misc]

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """
        Класс-метод, создающий и возвращающий объект SQLAlchemyUserDatabase, который:
            - Используется FastAPI Users для взаимодействия с базой данных;
            - Принимает модель пользователя (User) как аргумент.
        """
        return SQLAlchemyUserDatabase(session, User)
