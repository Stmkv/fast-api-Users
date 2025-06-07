from sqlalchemy.orm import Mapped, mapped_column


class IdIntPkMixin:
    """Миксин - если в модели есть другой primary key"""

    id: Mapped[int] = mapped_column(primary_key=True)
