from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Функция выполняет действия при запуске приложения и после завершения работы приложения
    """
    # startup
    # Вариант для быстрого теста
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    yield
    # shutdown
    print("dispose engine")
    db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
