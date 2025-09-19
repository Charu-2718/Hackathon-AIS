# models/contract_status.py
from pydantic import BaseModel

class ContractStatus(BaseModel):
    Id: int
    Name: str = ""
