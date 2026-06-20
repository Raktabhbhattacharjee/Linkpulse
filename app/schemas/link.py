from  pydantic import BaseModel,HttpUrl

class CreatelinkRequest(BaseModel):
    url:HttpUrl

class LinkResponse(BaseModel):
    id:int
    original_url:str
    short_code:str