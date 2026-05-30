from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.monument import Monument


async def get_monuments(db: AsyncSession) -> list[Monument]:
    stmt = (
        select(Monument)
        .where(Monument.deleted.is_(False))
        .order_by(Monument.sort_order)
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_monument_by_id(
    db: AsyncSession,
    monument_id: str,
) -> Monument | None:
    stmt = (
        select(Monument)
        .options(
            selectinload(Monument.translations),
        )
        .where(
            Monument.id == monument_id,
            Monument.deleted.is_(False),
        )
    )

    result = await db.execute(stmt)

    return result.scalar_one_or_none()


async def get_monuments_paginated(
    db: AsyncSession,
    limit: int,
    offset: int,
) -> list[Monument]:
    stmt = (
        select(Monument)
        .where(Monument.deleted.is_(False))
        .order_by(Monument.sort_order)
        .limit(limit)
        .offset(offset)
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def search_monuments(
    db: AsyncSession,
    query: str,
    limit: int = 20,
) -> list[Monument]:
    stmt = (
        select(Monument)
        .where(
            Monument.deleted.is_(False),
        )
        .where(Monument.id.ilike(f"%{query}%"))
        .order_by(Monument.sort_order)
        .limit(limit)
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())
