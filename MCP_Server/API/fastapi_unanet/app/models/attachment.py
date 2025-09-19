from pydantic import BaseModel

class Attachment(BaseModel):
    Id: int
    Name: str = ""
