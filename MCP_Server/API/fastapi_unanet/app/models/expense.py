# models/expense.py
from pydantic import BaseModel
from decimal import Decimal

class Expense(BaseModel):
    Id: int
    ProjectId: int
    Amount: Decimal
    Description: str = ""
