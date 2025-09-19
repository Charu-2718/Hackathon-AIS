# models/expense_detail.py
from pydantic import BaseModel

class ExpenseDetail(BaseModel):
    Id: int
    ExpenseId: int
    Description: str = ""
