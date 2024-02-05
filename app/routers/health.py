from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "ok"},
    )
