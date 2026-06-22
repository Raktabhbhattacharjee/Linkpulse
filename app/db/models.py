from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Link(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)

    original_url: Mapped[str] = mapped_column(
        String(2048)
    )

    short_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
    )