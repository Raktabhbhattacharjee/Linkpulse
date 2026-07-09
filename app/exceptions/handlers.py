from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.logging import logger
from app.exceptions.base import AppError


async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.error_code,
                "message": exc.message,
            }
        },
    )


async def validation_error_handler(request: Request, exc: RequestValidationError):
    details = []

    for error in exc.errors():
        details.append(
            {
                "field": error["loc"][-1],
                "message": error["msg"],
            }
        )

    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": details,
            }
        },
    )
async def global_exception_handler(request:Request,exc:Exception):
    logger.exception("Unhandled exception occured")
    return JSONResponse(
        status_code=500,
        content={
               "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred.",
            }
        },
    )
    