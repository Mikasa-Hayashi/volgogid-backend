from pydantic import BaseModel


class MonumentResponse(BaseModel):
    id: str
    lat: float
    lon: float
    image_url: str
    sort_order: int

    model_config = {
        "from_attributes": True,
    }
