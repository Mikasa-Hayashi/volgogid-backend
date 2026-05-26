from fastapi import APIRouter, Query

router = APIRouter()


@router.get("")
async def sync(since: str = Query(...)):
    return {"since": since, "monuments": [], "routes": [], "deleted_ids": {}}
