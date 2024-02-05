from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .routers import calculator, health, readiness

API_PREFIX = "/api"

app = FastAPI(
    title="FastAPI Calculator 🚀",
    description="FastAPI Calculator",
    version="0.0.1",
    # to hide the Schema section in Swagger
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url=f"{API_PREFIX}/docs",
    openapi_url=f"{API_PREFIX}/openapi.json",
)

app.include_router(health.router, prefix=API_PREFIX)
app.include_router(calculator.router, prefix=API_PREFIX)
app.include_router(readiness.router, prefix=API_PREFIX)


@app.exception_handler(RequestValidationError)
async def error_handler(request: Request, exc: Request):
    return JSONResponse(
        content={"detail": f"{exc}"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )
