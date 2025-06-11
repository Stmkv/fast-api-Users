from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from core.models import (
    db_helper,
    AccessToken,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    """
    Асинхронная зависимость FastAPI для получения адаптера доступа к токенам.

    Эта функция используется для внедрения `AccessTokenDatabase`, который позволяет
    FastAPI Users сохранять и читать access-токены из базы данных.

    Параметры:
        session (AsyncSession): асинхронная SQLAlchemy-сессия, автоматически
        предоставляемая через зависимость `db_helper.session_getter`.

    Возвращает:
        AccessTokenDatabase: адаптер для взаимодействия с таблицей токенов доступа.
    """
    yield AccessToken.get_db(session=session)