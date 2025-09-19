# models/contract.py
from pydantic import BaseModel

class Contract(BaseModel):
    Id: int
    Name: str = ""
    Status: str = ""
