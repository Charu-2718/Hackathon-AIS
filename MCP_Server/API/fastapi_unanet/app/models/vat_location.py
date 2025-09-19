# models/vat_location.py
from pydantic import BaseModel

class VatLocation(BaseModel):
    Id: int
    Name: str = ""
