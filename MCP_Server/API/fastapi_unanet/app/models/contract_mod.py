# models/contract_mod.py
from pydantic import BaseModel

class ContractMod(BaseModel):
    ModNumber: int
    ContractId: int
    Description: str = ""
