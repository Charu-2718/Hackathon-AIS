# models/project_account.py
from pydantic import BaseModel

class ProjectAccount(BaseModel):
    Id: int
    ProjectId: int
    Name: str = ""
