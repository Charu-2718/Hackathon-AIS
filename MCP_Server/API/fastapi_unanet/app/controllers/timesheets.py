from fastapi import APIRouter, HTTPException
from typing import List
from app.data import dummy_data as dd

router = APIRouter(prefix="/rest/time", tags=["Timesheets"])

# GET /rest/time
@router.get("/", response_model=List)
def get_timesheets():
    return dd.Timesheets

# GET /rest/time/{id}
@router.get("/{id}")
def get_timesheet(id: int):
    ts = next((t for t in dd.Timesheets if t.Id == id), None)
    if not ts:
        raise HTTPException(status_code=404, detail="Timesheet not found")
    return ts

# GET /rest/time/{id}/adjustments
@router.get("/{id}/adjustments", response_model=List)
def get_timesheet_adjustments(id: int):
    return [a for a in dd.TimesheetAdjustments if a.TimesheetId == id]

# GET /rest/time/{id}/attachment/{attachmentId}
@router.get("/{id}/attachment/{attachmentId}")
def get_timesheet_attachment(id: int, attachmentId: int):
    attachment = next((a for a in dd.TimesheetAttachments if a.Id == attachmentId and a.TimesheetId == id), None)
    if not attachment:
        raise HTTPException(status_code=404, detail="Timesheet attachment not found")
    return attachment

# GET /rest/time/{id}/attachments
@router.get("/{id}/attachments", response_model=List)
def get_timesheet_attachments(id: int):
    return [a for a in dd.TimesheetAttachments if a.TimesheetId == id]

# GET /rest/time/{id}/audit
@router.get("/{id}/audit", response_model=List)
def get_timesheet_audit(id: int):
    return [a for a in dd.TimesheetAudits if a.TimesheetId == id]

# GET /rest/time/{id}/auto-fill
@router.get("/{id}/auto-fill", response_model=List)
def get_auto_fill(id: int):
    return ["Auto Fill Row A", "Auto Fill Row B"]

# GET /rest/time/{id}/auto-fill/deleted
@router.get("/{id}/auto-fill/deleted", response_model=List)
def get_deleted_auto_fill(id: int):
    return ["Deleted Auto Fill Row A", "Deleted Auto Fill Row B"]

# GET /rest/time/{id}/history
@router.get("/{id}/history", response_model=List)
def get_timesheet_history(id: int):
    return ["History A", "History B"]

# GET /rest/time/{id}/items/audit
@router.get("/{id}/items/audit", response_model=List)
def get_items_audit(id: int):
    return ["Item Audit A", "Item Audit B"]

# GET /rest/time/{id}/offline
@router.get("/{id}/offline")
def get_offline_timesheet(id: int):
    return {"OfflineData": "Offline timesheet data content"}

# GET /rest/time/{id}/project-types
@router.get("/{id}/project-types", response_model=List)
def get_timesheet_project_types(id: int):
    return dd.ExpenseProjectTypes

# GET /rest/time/{id}/projects
@router.get("/{id}/projects", response_model=List)
def get_timesheet_projects(id: int):
    return dd.Projects

# GET /rest/time/{id}/projects/{projectId}/labor-categories
@router.get("/{id}/projects/{projectId}/labor-categories", response_model=List)
def get_project_labor_categories(id: int, projectId: int):
    return ["Labor Category A", "Labor Category B"]

# GET /rest/time/{id}/projects/{projectId}/locations
@router.get("/{id}/projects/{projectId}/locations", response_model=List)
def get_project_locations(id: int, projectId: int):
    return ["Location A", "Location B"]

# GET /rest/time/{id}/tasks/{taskId}/labor-categories
@router.get("/{id}/tasks/{taskId}/labor-categories", response_model=List)
def get_task_labor_categories(id: int, taskId: int):
    return ["Labor Category A", "Labor Category B"]

# GET /rest/time/{id}/tasks/{taskId}/locations
@router.get("/{id}/tasks/{taskId}/locations", response_model=List)
def get_task_locations(id: int, taskId: int):
    return ["Location A", "Location B"]

# GET /rest/time/{id}/validate
@router.get("/{id}/validate")
def validate_timesheet(id: int):
    return {"valid": True}
