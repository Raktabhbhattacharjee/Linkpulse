from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.link_repository import LinkRepository
from app.services.link_service import LinkService


def get_link_service(
    db: AsyncSession = Depends(get_db),
) -> LinkService:
    repository = LinkRepository(db)
    return LinkService(repository)