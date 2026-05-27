from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Route(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "routes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    cover_monument_id: Mapped[str] = mapped_column(String)
    sort_order: Mapped[int] = mapped_column(Integer)
