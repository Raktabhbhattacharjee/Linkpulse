from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Link

class LinkRepository:
    def __init__(self,db:AsyncSession):
        self.db=db

    async def create(self,original_url:str,short_code:str)->Link:
        link = Link(original_url=original_url,short_code=short_code)
        self.db.add(link)
        await self.db.commit()
        await self.db.refresh(link)
        return link