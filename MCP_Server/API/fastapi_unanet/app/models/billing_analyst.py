# models/billing_analyst.py
from pydantic import BaseModel

class BillingAnalyst(BaseModel):
    Id: int
    Name: str = ""
