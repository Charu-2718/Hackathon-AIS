# models/expense_history.py
from pydantic import BaseModel
from datetime import date

class ExpenseHistory(BaseModel):
    Id: int
    ExpenseId: int
    Status: str = ""
    Date: date
