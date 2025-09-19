# models/expense_attachment.py
from pydantic import BaseModel

class ExpenseAttachment(BaseModel):
    Id: int
    ExpenseId: int
    FileName: str
