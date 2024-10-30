from pydantic import BaseModel, Field, root_validator
from typing import Optional, List
from datetime import date, datetime

class bookResObj(BaseModel):
    message: str
    status_code: int
    pid: int
    content: dict = Field({}, example='Review data')

