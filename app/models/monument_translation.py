from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class MonumentTranslation(Base):
    __tablename__ = "monument_translations"

    monument_id: Mapped[str] = mapped_column(
        ForeignKey("monuments.id"),
        primary_key=True,
    )
    lang: Mapped[str] = mapped_column(String, primary_key=True)
    field_key: Mapped[str] = mapped_column(String, primary_key=True)
    field_value: Mapped[str] = mapped_column(String)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
