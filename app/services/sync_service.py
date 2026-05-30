from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.monument import Monument
from app.models.monument_translation import MonumentTranslation
from app.models.route import Route
from app.models.route_stop import RouteStop
from app.models.route_translation import RouteTranslation


async def get_updated_monuments(
    db: AsyncSession,
    since: datetime,
) -> list[Monument]:
    stmt = select(Monument).where(Monument.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_updated_translations(
    db: AsyncSession,
    since: datetime,
) -> list[MonumentTranslation]:
    stmt = select(MonumentTranslation).where(MonumentTranslation.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_deleted_monument_ids(
    db: AsyncSession,
    since: datetime,
) -> list[str]:
    stmt = select(Monument.id).where(
        Monument.deleted.is_(True),
        Monument.updated_at > since,
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_updated_routes(
    db: AsyncSession,
    since: datetime,
) -> list[Route]:
    stmt = select(Route).where(Route.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_updated_route_translations(
    db: AsyncSession,
    since: datetime,
) -> list[RouteTranslation]:
    stmt = select(RouteTranslation).where(RouteTranslation.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_updated_route_stops(
    db: AsyncSession,
    since: datetime,
) -> list[RouteStop]:
    stmt = select(RouteStop).where(RouteStop.updated_at > since)

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def get_deleted_route_ids(
    db: AsyncSession,
    since: datetime,
) -> list[str]:
    stmt = select(Route.id).where(
        Route.deleted.is_(True),
        Route.updated_at > since,
    )

    result = await db.execute(stmt)

    return list(result.scalars().all())


async def sync_data(
    db: AsyncSession,
    since: datetime,
):
    monuments = await get_updated_monuments(
        db,
        since,
    )

    translations = await get_updated_translations(
        db,
        since,
    )

    deleted_monuments = await get_deleted_monument_ids(
        db,
        since,
    )

    return {
        "monuments": monuments,
        "monument_translations": translations,
        "deleted_ids": {
            "monuments": deleted_monuments,
            "routes": [],
        },
    }
