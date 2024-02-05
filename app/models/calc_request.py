import re

from fastapi import Query
from pydantic import BaseModel, field_validator

REGEX_SIMPLE_MATH = re.compile(r"([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)")


class CalcRequest(BaseModel):
    expression: str = Query(None, max_length=50)

    @field_validator("expression")
    def only_simple_math(cls, v: str):
        if REGEX_SIMPLE_MATH.match(v):
            return v
        else:
            raise ValueError("only simple math and numbers required")
