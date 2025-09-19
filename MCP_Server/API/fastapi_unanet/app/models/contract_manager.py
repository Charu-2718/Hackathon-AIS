# models/contract_manager.py
from pydantic import BaseModel

class ContractManager(BaseModel):
    Id: int
    Name: str = ""
