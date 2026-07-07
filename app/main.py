from fastapi import FastAPI

from app.api.routes.link_routes import router as link_router
from app.exceptions.base import AppError
from app.exceptions.handlers import app_error_handler

app = FastAPI()

app.include_router(link_router)
app.add_exception_handler(AppError,app_error_handler)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "linkpulse"}
