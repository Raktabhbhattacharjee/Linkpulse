import secrets
from app.repositories.link_repository import LinkRepository
class LinkService:
    def __init__(self,repository:LinkRepository):
        self.repository=repository
    async def create_link(self,url:str):
        short_code =secrets.token_urlsafe(6)
        return await self.repository.create(
            original_url=url,
            short_code=short_code
        )
    async def get_original_url(self,short_code:str):
        link = await self.repository.get_by_short_code(short_code)
        if not link:
            return None
        
        return link.original_url

        
    