from fastapi import FastAPI

from app.api.routes.link_routes import router as link_router

app = FastAPI()

app.include_router(link_router)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "linkpulse"}
