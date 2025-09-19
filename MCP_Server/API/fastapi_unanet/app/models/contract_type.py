# models/contract_type.py
from pydantic import BaseModel

class ContractType(BaseModel):
    Id: int
    Name: str = ""
