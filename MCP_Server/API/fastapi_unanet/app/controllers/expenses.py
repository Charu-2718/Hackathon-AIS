from fastapi import APIRouter, HTTPException
from typing import List
from app.data import dummy_data as dd

router = APIRouter(prefix="/rest/expenses", tags=["Expenses"])

# GET /rest/expenses/{id}
@router.get("/{id}")
def get_expense(id: int):
    expense = next((e for e in dd.Expenses if e.Id == id), None)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

# GET /rest/expenses/{id}/attachments
@router.get("/{id}/attachments", response_model=List)
def get_expense_attachments(id: int):
    attachments = [a for a in dd.ExpenseAttachments if a.ExpenseId == id]
    return attachments

# GET /rest/expenses/{id}/attachments/{attachment_id}
@router.get("/{id}/attachments/{attachment_id}")
def get_expense_attachment(id: int, attachment_id: int):
    attachment = next((a for a in dd.ExpenseAttachments if a.Id == attachment_id and a.ExpenseId == id), None)
    if not attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return attachment

# GET /rest/expenses/{id}/details/{detail_id}
@router.get("/{id}/details/{detail_id}")
def get_expense_detail(id: int, detail_id: int):
    detail = next((d for d in dd.ExpenseDetails if d.Id == detail_id and d.ExpenseId == id), None)
    if not detail:
        raise HTTPException(status_code=404, detail="Expense detail not found")
    return detail

# GET /rest/expenses/{id}/expense-types
@router.get("/{id}/expense-types", response_model=List)
def get_expense_types(id: int):
    return dd.ExpenseTypes

# GET /rest/expenses/{id}/history
@router.get("/{id}/history", response_model=List)
def get_expense_history(id: int):
    history = [h for h in dd.ExpenseHistories if h.ExpenseId == id]
    return history

# GET /rest/expenses/{id}/meal-caps
@router.get("/{id}/meal-caps")
def get_meal_caps(id: int):
    cap = next((m for m in dd.MealCaps if m.ExpenseId == id), None)
    if not cap:
        raise HTTPException(status_code=404, detail="Meal cap not found")
    return cap

# GET /rest/expenses/{id}/payment-methods
@router.get("/{id}/payment-methods", response_model=List)
def get_payment_methods(id: int):
    methods = [m for m in dd.PaymentMethods if m.ExpenseId == id]
    return methods

# GET /rest/expenses/{id}/project-types
@router.get("/{id}/project-types", response_model=List)
def get_project_types(id: int):
    return dd.ExpenseProjectTypes

# GET /rest/expenses/{id}/projects
@router.get("/{id}/projects", response_model=List)
def get_expense_projects(id: int):
    return dd.Projects

# GET /rest/expenses/{id}/validate
@router.get("/{id}/validate")
def validate_expense(id: int):
    return {"valid": True}

# GET /rest/expenses/projects
@router.get("/projects", response_model=List)
def get_projects_by_owner():
    return dd.Projects

# GET /rest/expenses/vat-locations
@router.get("/vat-locations", response_model=List)
def get_vat_locations():
    return dd.VatLocations

# GET /rest/expenses/vat-locations/{id}
@router.get("/vat-locations/{id}")
def get_vat_location(id: int):
    location = next((v for v in dd.VatLocations if v.Id == id), None)
    if not location:
        raise HTTPException(status_code=404, detail="VAT location not found")
    return location
