import uvicorn
import logging
from fastapi import FastAPI

from handlers.health import router as health_router
from handlers.metrics import router as metrics_router
from handlers.uptime import lifespan, get_uptime_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)

app = FastAPI()
app.include_router(health_router)
app.include_router(metrics_router)

app = FastAPI(title="Metrics API", lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message": "Hello, World!",
        "system_runtime": get_uptime_data()
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, log_level="info")