# models/payment_method.py
from pydantic import BaseModel

class PaymentMethod(BaseModel):
    ExpenseId: int
    Method: str = ""
