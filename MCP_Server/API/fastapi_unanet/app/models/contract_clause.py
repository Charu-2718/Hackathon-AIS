# models/contract_clause.py
from pydantic import BaseModel

class ContractClause(BaseModel):
    Id: int
    ContractId: int
    Text: str = ""
