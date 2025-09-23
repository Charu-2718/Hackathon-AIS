from pydantic import BaseModel
from typing import Optional

class ProjectFee(BaseModel):
    Id: int
    ProjectId: int
    Description: str
    Amount: float

class ProjectFunding(BaseModel):
    Id: int
    ProjectId: int
    Source: str
    Amount: float

class ProjectHistory(BaseModel):
    Id: int
    ProjectId: int
    ChangeDescription: str
    ChangedBy: str

class ProjectLocation(BaseModel):
    Id: int
    ProjectId: int
    Address: str
    City: str
    Country: str

class ProjectMilestone(BaseModel):
    Id: int
    ProjectId: int
    Name: str
    DueDate: str

class ProjectNote(BaseModel):
    Id: int
    ProjectId: int
    Content: str
    Author: str

class ProjectOrganization(BaseModel):
    Id: int
    ProjectId: int
    OrgName: str
    Role: str

class ProjectPeriod(BaseModel):
    Id: int
    ProjectId: int
    StartDate: str
    EndDate: str

class ProjectTypeAssignment(BaseModel):
    Id: int
    ProjectId: int
    TypeName: str

class ProjectRate(BaseModel):
    Id: int
    ProjectId: int
    RateType: str
    Value: float

class ProjectResource(BaseModel):
    Id: int
    ProjectId: int
    ResourceName: str
    Role: str

class ProjectRevenue(BaseModel):
    Id: int
    ProjectId: int
    Amount: float
    Period: str

class ProjectTask(BaseModel):
    Id: int
    ProjectId: int
    TaskName: str
    Status: str

class ProjectTeam(BaseModel):
    Id: int
    ProjectId: int
    MemberName: str
    Role: str
