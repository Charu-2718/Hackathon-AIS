# app/models/people.py
from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    Id: int
    Name: str
    Email: str

class AccrualPlan(BaseModel):
    Id: int
    PersonId: int
    PlanName: str

class Alternate(BaseModel):
    Id: int
    PersonId: int
    Name: str

class ApprovalGroup(BaseModel):
    Id: int
    PersonId: int
    Type: str

class PersonAttachment(BaseModel):
    Id: int
    PersonId: int
    FileName: str

class BenefitsValue(BaseModel):
    Id: int
    PersonId: int
    PackageName: str

class Rate(BaseModel):
    Id: int
    PersonId: int
    Amount: float

class Skill(BaseModel):
    Id: int
    PersonId: int
    SkillName: str

class PersonSummary(BaseModel):
    Id: int
    Name: str
