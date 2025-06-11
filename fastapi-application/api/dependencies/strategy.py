from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends
from fastapi_users.authentication.strategy.db import (
    DatabaseStrategy,
)

from core.config import settings
from core.models.access_token import get_access_tokens_db


if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_tokens_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_tokens_db),
    ],
) -> DatabaseStrategy:
    """
    Возвращает стратегию аутентификации с хранением access-токенов в базе данных.

    Эта стратегия используется FastAPI Users и реализует хранение access-токенов
    в базе данных через переданный адаптер `access_tokens_db`.

    Параметры:
        access_tokens_db (AccessTokenDatabase[AccessToken]):
            Зависимость, автоматически внедряемая FastAPI,
            предоставляющая адаптер для работы с токенами доступа.

    Возвращает:
        DatabaseStrategy: стратегия аутентификации с поддержкой хранения токенов в БД.
    """
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
