from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.link import LinkNotFoundError

async def link_not_found_handler(request:Request , exc:LinkNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "detail":str(exc)
        },
    )