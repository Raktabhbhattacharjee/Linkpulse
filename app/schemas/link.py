from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional
class CreateLinkRequest(BaseModel):
    url: HttpUrl


class LinkResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
class LinkStatsResponse(BaseModel):
    original_url:str
    short_code:str
    click_count:int
    created_at:datetime
    updated_at:datetime
    last_accessed_at: Optional[datetime] = None
    