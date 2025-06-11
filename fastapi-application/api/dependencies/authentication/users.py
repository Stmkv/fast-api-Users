from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from core.models import (
    db_helper,
    User,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    """
    Асинхронная зависимость FastAPI для получения адаптера доступа к пользователям.

    Эта функция предоставляет FastAPI Users адаптер `SQLAlchemyUserDatabase`,
    который используется для создания, обновления и поиска пользователей в базе данных.

    Параметры:
        session (AsyncSession): асинхронная SQLAlchemy-сессия, автоматически
        передаётся через зависимость `db_helper.session_getter`.

    Возвращает:
        SQLAlchemyUserDatabase: адаптер для работы с моделью пользователей (`User`).
    """
    yield User.get_db(session=session)