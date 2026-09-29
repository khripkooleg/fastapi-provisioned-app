from fastapi import APIRouter, HTTPException

import psutil

router = APIRouter(tags=["Metrics"])

GIG_DIVISOR = 1024 ** 3

@router.get("/metrics")
async def metrics():
    try:
        users = psutil.users()
        user_name = users[0].name if users else "N/A"
        
        load_avg = psutil.getloadavg() if hasattr(psutil, "getloadavg") else None

        return {
            "host_cpu_cores_count": psutil.cpu_count(),
            "load_average": load_avg,
            "memory_usage_available (GB)": round(psutil.virtual_memory().total / GIG_DIVISOR, 1),
            "user": user_name
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch system metrics: {str(exc)}"
        )