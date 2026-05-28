from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.monument import MonumentResponse
from app.services.monument_service import get_monuments

router = APIRouter()


@router.get(
    "/",
    response_model=list[MonumentResponse],
)
async def monument_list(
    db: AsyncSession = Depends(get_db),
):
    return await get_monuments(db)
