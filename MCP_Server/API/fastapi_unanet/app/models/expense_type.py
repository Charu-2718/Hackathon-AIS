# models/expense_type.py
from pydantic import BaseModel

class ExpenseType(BaseModel):
    Id: int
    Name: str = ""
