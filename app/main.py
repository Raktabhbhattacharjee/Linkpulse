from fastapi import FastAPI

from app.api.routes.link_routes import router as link_router
from app.exceptions.link import LinkNotFoundError
from app.exceptions.handlers import link_not_found_handler

app = FastAPI()

app.include_router(link_router)
app.add_exception_handler(LinkNotFoundError,link_not_found_handler)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "linkpulse"}
