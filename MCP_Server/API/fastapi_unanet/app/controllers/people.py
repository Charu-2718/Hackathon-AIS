# app/controllers/people.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.data import dummy_data as dd

router = APIRouter(prefix="/rest/people", tags=["People"])

@router.get("/", response_model=List)
def get_people():
    return dd.People

@router.get("/{id}")
def get_person(id: int):
    person = next((p for p in dd.People if p.Id == id), None)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.get("/{id}/accrual-plans", response_model=List)
def get_person_accrual_plans(id: int):
    return [a for a in dd.AccrualPlans if a.PersonId == id]

@router.get("/{id}/accrual-plans/{personAccrualPlanId}")
def get_person_accrual_plan(id: int, personAccrualPlanId: int):
    plan = next((a for a in dd.AccrualPlans if a.PersonId == id and a.Id == personAccrualPlanId), None)
    if not plan:
        raise HTTPException(status_code=404, detail="Accrual plan not found")
    return plan

@router.get("/{id}/alternates", response_model=List)
def get_person_alternates(id: int):
    return [a for a in dd.Alternates if a.PersonId == id]

@router.get("/{id}/approval-groups/approver", response_model=List)
def get_person_approver_groups(id: int):
    return [g for g in dd.ApprovalGroups if g.PersonId == id and g.Type == "Approver"]

@router.get("/{id}/approval-groups/submitter/expense-report", response_model=List)
def get_person_expense_report_groups(id: int):
    return [g for g in dd.ApprovalGroups if g.PersonId == id and g.Type == "ExpenseReport"]

@router.get("/{id}/approval-groups/submitter/expense-request", response_model=List)
def get_person_expense_request_groups(id: int):
    return [g for g in dd.ApprovalGroups if g.PersonId == id and g.Type == "ExpenseRequest"]

@router.get("/{id}/approval-groups/submitter/leave", response_model=List)
def get_person_leave_groups(id: int):
    return [g for g in dd.ApprovalGroups if g.PersonId == id and g.Type == "Leave"]

@router.get("/{id}/approval-groups/submitter/time", response_model=List)
def get_person_time_groups(id: int):
    return [g for g in dd.ApprovalGroups if g.PersonId == id and g.Type == "Time"]

@router.get("/{id}/attachments", response_model=List)
def get_person_attachments(id: int):
    return [a for a in dd.PersonAttachments if a.PersonId == id]

@router.get("/{id}/attachments/{attachmentId}")
def get_person_attachment(id: int, attachmentId: int):
    att = next((a for a in dd.PersonAttachments if a.Id == attachmentId and a.PersonId == id), None)
    if not att:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return att

@router.get("/{id}/available-alternates", response_model=List)
def get_available_alternates(id: int):
    return dd.AvailableAlternates

@router.get("/{id}/benefits-values", response_model=List)
def get_person_benefits(id: int):
    return [b for b in dd.BenefitsValues if b.PersonId == id]

@router.get("/{id}/benefits-values/{benefitsValueId}")
def get_person_benefit(id: int, benefitsValueId: int):
    bv = next((b for b in dd.BenefitsValues if b.PersonId == id and b.Id == benefitsValueId), None)
    if not bv:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return bv

@router.get("/{id}/classification/{date}")
def get_person_classification(id: int, date: str):
    return {"PersonId": id, "Date": date, "Classification": "Employee"}

@router.get("/{id}/payroll")
def get_person_payroll(id: int):
    return {"PersonId": id, "Payroll": "Payroll details"}

@router.get("/{id}/rates", response_model=List)
def get_person_rates(id: int):
    return [r for r in dd.Rates if r.PersonId == id]

@router.get("/{id}/rates/{rateId}")
def get_person_rate(id: int, rateId: int):
    rate = next((r for r in dd.Rates if r.PersonId == id and r.Id == rateId), None)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return rate

@router.get("/{id}/skills", response_model=List)
def get_person_skills(id: int):
    return [s for s in dd.Skills if s.PersonId == id]

@router.get("/list", response_model=List)
def get_people_list():
    return dd.PeopleSummaries
