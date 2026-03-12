from fastapi import FastAPI
from src.api.routes_generate import router as generate_router
from src.api.routes_lore import router as lore_router
from src.api.routes_health import router as health_router

app = FastAPI()

app.include_router(generate_router, prefix="/api")
app.include_router(lore_router, prefix="/api")

# Health should NOT use /api
app.include_router(health_router)