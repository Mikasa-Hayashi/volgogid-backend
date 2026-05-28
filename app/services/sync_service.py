from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.monument import Monument


async def get_updated_monuments(
    db: AsyncSession,
    since: datetime,
) -> list[Monument]:
    stmt = select(Monument).where(Monument.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())
