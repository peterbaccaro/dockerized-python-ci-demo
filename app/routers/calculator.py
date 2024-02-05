from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.models.calc_request import CalcRequest
from app.models.calc_response import CalcResponse

router = APIRouter(tags=["Calculator"])


@router.get("/calc", summary="Calc as get method", response_model=CalcResponse)
async def get_calc(query: CalcRequest = Depends(CalcRequest)):
    params = query.model_dump()
    calc_rsp = {
        "result": str(eval(params["expression"])),
        "operation": params["expression"],
    }
    return JSONResponse(content=calc_rsp, status_code=status.HTTP_200_OK)
