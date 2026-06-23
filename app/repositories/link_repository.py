from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Link


class LinkRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, original_url: str, short_code: str) -> Link:
        link = Link(original_url=original_url, short_code=short_code)
        self.db.add(link)
        await self.db.commit()
        await self.db.refresh(link)
        return link

    async def get_by_short_code(self, short_code: str) -> Link:
        link_query = select(Link).where(Link.short_code == short_code)
        result = await self.db.execute(link_query)
        link = result.scalar_one_or_none()
        return link
    async def update(self,link:Link)->Link:
        self.db.add(link)
        await self.db.commit()
        await self.db.refresh(link)
        return link
        