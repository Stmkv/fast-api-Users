# Файл примера создания новой модели. При начале нового проекта удалить!
# =============================================================================
# TODO DELETE
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
