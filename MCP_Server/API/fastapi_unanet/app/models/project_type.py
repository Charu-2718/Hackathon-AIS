# models/project_type.py
from pydantic import BaseModel

class ProjectType(BaseModel):
    Id: int
    Name: str = ""
