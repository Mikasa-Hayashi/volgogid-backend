from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.monument import MonumentResponse
from app.schemas.monument_detail import MonumentDetailResponse
from app.services.monument_service import get_monument_by_id, get_monuments

router = APIRouter()


@router.get(
    "/",
    response_model=list[MonumentResponse],
)
async def monument_list(
    db: AsyncSession = Depends(get_db),
):
    return await get_monuments(db)


@router.get(
    "/{monument_id}",
    response_model=MonumentDetailResponse,
)
async def monument_detail(
    monument_id: str,
    db: AsyncSession = Depends(get_db),
):
    monument = await get_monument_by_id(
        db,
        monument_id,
    )

    if monument is None:
        raise HTTPException(
            status_code=404,
            detail="Monument not found",
        )

    return monument
