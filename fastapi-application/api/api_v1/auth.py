import fastapi_users.router
from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.router.get_auth_router(authentication_backend),
)
