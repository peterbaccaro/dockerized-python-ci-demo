from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Ready"])


@router.get("/ready")
def readiness() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "ok"},
    )
