# models/master_contract.py
from pydantic import BaseModel

class MasterContract(BaseModel):
    Id: int
    OwningOrgId: int
    Name: str = ""
