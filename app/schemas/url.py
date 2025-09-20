from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    original_url: HttpUrl
    short_code: str

class URLInfo(BaseModel):
    original_url: HttpUrl
    short_code: str
    created_at: datetime

    class Config:
        orm_mode = True