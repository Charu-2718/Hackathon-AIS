# models/timesheet.py
from pydantic import BaseModel
from datetime import date

class Timesheet(BaseModel):
    Id: int
    EmployeeId: int
    Date: date
    HoursWorked: float
