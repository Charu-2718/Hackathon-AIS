# models/timesheet_audit.py
from pydantic import BaseModel
from datetime import date

class TimesheetAudit(BaseModel):
    Id: int
    TimesheetId: int
    Action: str = ""
    Date: date
