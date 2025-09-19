# models/wage_determination.py
from pydantic import BaseModel

class WageDetermination(BaseModel):
    Id: int
    ContractId: int
    Name: str = ""
