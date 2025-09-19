# models/timesheet_adjustment.py
from pydantic import BaseModel

class TimesheetAdjustment(BaseModel):
    Id: int
    TimesheetId: int
    Reason: str = ""
