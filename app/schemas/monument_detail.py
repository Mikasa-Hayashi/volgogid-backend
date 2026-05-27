from pydantic import BaseModel


class TranslationSchema(BaseModel):
    lang: str
    field_key: str
    field_value: str


class MonumentDetailResponse(BaseModel):
    id: str
    lat: float
    lon: float
    image_url: str

    translations: list[TranslationSchema]
