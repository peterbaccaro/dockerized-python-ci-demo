from pydantic import BaseModel


class CalcResponse(BaseModel):
    result: str = None
    operation: str = None
