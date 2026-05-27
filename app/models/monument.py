from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Monument(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "monuments"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    lat: Mapped[float] = mapped_column(Float)
    lon: Mapped[float] = mapped_column(Float)
    image_url: Mapped[str] = mapped_column(String)
    sort_order: Mapped[int] = mapped_column(Integer)
