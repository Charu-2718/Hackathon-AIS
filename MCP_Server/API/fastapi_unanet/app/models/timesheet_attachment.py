# models/timesheet_attachment.py
from pydantic import BaseModel

class TimesheetAttachment(BaseModel):
    Id: int
    TimesheetId: int
    FileName: str = ""
