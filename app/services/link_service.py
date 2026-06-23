import secrets
from app.repositories.link_repository import LinkRepository
from datetime import datetime, timezone


class LinkService:
    def __init__(self, repository: LinkRepository):
        self.repository = repository

    async def create_link(self, url: str):
        short_code = secrets.token_urlsafe(6)
        return await self.repository.create(original_url=url, short_code=short_code)

    async def get_original_url(self, short_code: str):
        link = await self.repository.get_by_short_code(short_code)
        if not link:
            return None
        link.click_count += 1
        link.last_accessed_at = datetime.now(timezone.utc)
        await self.repository.update(link)

        return link.original_url

    async def get_link_stats(self, short_code: str):
        link = await self.repository.get_by_short_code(short_code)
        if not link:
            return None
        return link
        
