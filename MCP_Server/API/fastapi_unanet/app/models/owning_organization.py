# models/owning_organization.py
from pydantic import BaseModel

class OwningOrganization(BaseModel):
    Id: int
    Name: str = ""
