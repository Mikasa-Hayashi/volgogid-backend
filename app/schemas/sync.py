from pydantic import BaseModel

from app.schemas.monument import MonumentResponse
from app.schemas.monument_detail import MonumentTranslationResponse


class DeletedIdsResponse(BaseModel):
    monuments: list[str]
    routes: list[str]


class SyncResponse(BaseModel):
    monuments: list[MonumentResponse]

    monument_translations: list[MonumentTranslationResponse]

    deleted_ids: DeletedIdsResponse
