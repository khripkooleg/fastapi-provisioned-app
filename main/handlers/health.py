from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Health"])

@router.get("/health", response_class=JSONResponse)
async def healthcheck() -> JSONResponse:
    try:
        return JSONResponse(
            content={"status": "healthy"},
            status_code=200
        )
    except (RuntimeError, OSError) as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )
