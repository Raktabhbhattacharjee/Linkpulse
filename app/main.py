from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.routes.link_routes import router as link_router
from app.exceptions.base import AppError
from app.exceptions.handlers import (
    app_error_handler,
    validation_error_handler,
    global_exception_handler,
)

app = FastAPI()

app.include_router(link_router)

# Business exceptions
app.add_exception_handler(
    AppError,
    app_error_handler,
)

# Request validation exceptions
app.add_exception_handler(
    RequestValidationError,
    validation_error_handler,
)

# Catch-all for unexpected exceptions
app.add_exception_handler(
    Exception,
    global_exception_handler,
)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "linkpulse"}