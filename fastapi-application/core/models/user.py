from typing import TYPE_CHECKING
from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):  # type: ignore[misc]

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
