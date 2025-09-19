# models/project_alert.py
from pydantic import BaseModel

class ProjectAlert(BaseModel):
    Id: int
    ProjectId: int
    Message: str = ""
