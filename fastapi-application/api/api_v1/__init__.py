from fastapi import APIRouter

from core.config import settings

from .users import router as users_router # TODO DELETE

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    users_router,# TODO DELETE
    prefix=settings.api.v1.users,# TODO DELETE
)