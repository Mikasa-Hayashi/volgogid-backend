from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.monument import Monument
from app.models.monument_translation import MonumentTranslation


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
    id_stmt = (
        select(MonumentTranslation.monument_id)
        .where(
            MonumentTranslation.field_key == "name",
            MonumentTranslation.field_value.ilike(f"%{query}%"),
        )
        .limit(limit)
    )

    res = await db.execute(id_stmt)
    ids = res.scalars().all()

    if not ids:
        return []

    stmt = select(Monument).where(Monument.id.in_(ids))

    result = await db.execute(stmt)

    return list(result.scalars().all())
