# models/provision.py
from pydantic import BaseModel

class Provision(BaseModel):
    Id: int
    Name: str = ""
