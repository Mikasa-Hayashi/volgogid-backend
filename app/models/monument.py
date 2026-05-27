from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Monument(Base):
    __tablename__ = "monuments"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    lat: Mapped[float] = mapped_column(Float)
    lon: Mapped[float] = mapped_column(Float)
    image_url: Mapped[str] = mapped_column(String)
    sort_order: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)
