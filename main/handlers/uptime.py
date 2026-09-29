from datetime import datetime, timezone
import logging
from contextlib import asynccontextmanager

import psutil

logger = logging.getLogger(__name__)

BOOT_TIME = datetime.fromtimestamp(psutil.boot_time(), tz=timezone.utc)

@asynccontextmanager
async def lifespan(app):
    logger.info("Starting FastAPI application...")
    yield
    logger.info("Shutting down FastAPI application...")

def get_uptime_data() -> dict:
    now = datetime.now(tz=timezone.utc)
    uptime_duration = now - BOOT_TIME

    total_seconds = int(uptime_duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    return {
        "uptime_formatted": f"{days}d {hours}h {minutes}m {seconds}s",
        "uptime_seconds": total_seconds,
        "boot_time": BOOT_TIME.isoformat()
    }
    
