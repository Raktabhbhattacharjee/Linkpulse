from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.link_service import LinkService
from app.schemas.link import CreateLinkRequest, LinkResponse
from app.repositories.link_repository import LinkRepository
router = APIRouter(prefix="/links", tags=["Links"])


@router.post("/", response_model=LinkResponse)
async def create_link(
    payload: CreateLinkRequest,
    db: AsyncSession = Depends(get_db)
):
    service = LinkService(
        repository=LinkRepository(db)
    )

    link = await service.create_link(str(payload.url))

    return link