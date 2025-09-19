# models/project.py
from pydantic import BaseModel

class Project(BaseModel):
    Id: int
    Name: str = ""
    Client: str = ""
