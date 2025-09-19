# models/meal_cap.py
from pydantic import BaseModel
from decimal import Decimal

class MealCap(BaseModel):
    ExpenseId: int
    MaxAmount: Decimal
