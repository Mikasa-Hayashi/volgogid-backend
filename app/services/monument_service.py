from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.monument import Monument


async def get_monuments(db: AsyncSession) -> list[Monument]:
    stmt = (
        select(Monument)
        .where(Monument.deleted.is_(False))
        .order_by(Monument.sort_order)
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())
