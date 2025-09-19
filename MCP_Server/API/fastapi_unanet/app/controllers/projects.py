from fastapi import APIRouter, HTTPException
from typing import List
from app.data import dummy_data as dd

router = APIRouter(prefix="/rest/projects", tags=["Projects"])

# GET /rest/projects/{id}
@router.get("/{id}")
def get_project(id: int):
    project = next((p for p in dd.Projects if p.Id == id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# GET /rest/projects/{id}/accounts
@router.get("/{id}/accounts", response_model=List)
def get_project_accounts(id: int):
    accounts = [a for a in dd.ProjectAccounts if a.ProjectId == id]
    return accounts

# Admin endpoints examples
@router.get("/{id}/admin/billing-managers/alternate")
def get_alternate_billing_managers(id: int):
    return ["Alternate Manager A", "Alternate Manager B"]

@router.get("/{id}/admin/billing-managers/primary")
def get_primary_billing_manager(id: int):
    return {"Name": "Primary Manager"}

@router.get("/{id}/admin/billing-viewers/alternate")
def get_alternate_billing_viewers(id: int):
    return ["Alternate Viewer A", "Alternate Viewer B"]

@router.get("/{id}/admin/billing-viewers/primary")
def get_primary_billing_viewer(id: int):
    return {"Name": "Primary Viewer"}

@router.get("/{id}/admin/customers/alternates")
def get_alternate_customers(id: int):
    return ["Alternate Customer A", "Alternate Customer B"]

@router.get("/{id}/admin/customers/primary")
def get_primary_customer(id: int):
    return {"Name": "Primary Customer"}

@router.get("/{id}/admin/document-viewers/alternate")
def get_alternate_document_viewers(id: int):
    return ["Alternate Doc Viewer A", "Alternate Doc Viewer B"]

@router.get("/{id}/admin/document-viewers/primary")
def get_primary_document_viewer(id: int):
    return {"Name": "Primary Document Viewer"}

@router.get("/{id}/admin/leads/alternate")
def get_alternate_leads(id: int):
    return ["Alternate Lead A", "Alternate Lead B"]

@router.get("/{id}/admin/leads/primary")
def get_primary_lead(id: int):
    return {"Name": "Primary Lead"}

@router.get("/{id}/admin/managers/alternate")
def get_alternate_managers(id: int):
    return ["Alternate Manager A", "Alternate Manager B"]

@router.get("/{id}/admin/managers/primary")
def get_primary_manager(id: int):
    return {"Name": "Primary Manager"}

@router.get("/{id}/admin/po-viewers/alternate")
def get_alternate_po_viewers(id: int):
    return ["Alternate PO Viewer A", "Alternate PO Viewer B"]

@router.get("/{id}/admin/po-viewers/primary")
def get_primary_po_viewer(id: int):
    return {"Name": "Primary PO Viewer"}

@router.get("/{id}/admin/pr-viewers/alternate")
def get_alternate_pr_viewers(id: int):
    return ["Alternate PR Viewer A", "Alternate PR Viewer B"]

@router.get("/{id}/admin/pr-viewers/primary")
def get_primary_pr_viewer(id: int):
    return {"Name": "Primary PR Viewer"}

@router.get("/{id}/admin/project-approvers/alternates")
def get_alternate_project_approvers(id: int):
    return ["Alternate Approver A", "Alternate Approver B"]

@router.get("/{id}/admin/project-approvers/primary")
def get_primary_project_approver(id: int):
    return {"Name": "Primary Approver"}

@router.get("/{id}/admin/resource-assigners/alternate")
def get_alternate_resource_assigners(id: int):
    return ["Alternate Assigner A", "Alternate Assigner B"]

@router.get("/{id}/admin/resource-assigners/primary")
def get_primary_resource_assigner(id: int):
    return {"Name": "Primary Assigner"}

@router.get("/{id}/admin/resource-planners/alternate")
def get_alternate_resource_planners(id: int):
    return ["Alternate Planner A", "Alternate Planner B"]

@router.get("/{id}/admin/resource-planners/primary")
def get_primary_resource_planner(id: int):
    return {"Name": "Primary Planner"}

@router.get("/{id}/admin/resource-requestors/alternate")
def get_alternate_resource_requestors(id: int):
    return ["Alternate Requestor A", "Alternate Requestor B"]

@router.get("/{id}/admin/resource-requestors/primary")
def get_primary_resource_requestor(id: int):
    return {"Name": "Primary Requestor"}

@router.get("/{id}/admin/viewers/alternate")
def get_alternate_viewers(id: int):
    return ["Alternate Viewer A", "Alternate Viewer B"]

@router.get("/{id}/admin/viewers/primary")
def get_primary_viewer(id: int):
    return {"Name": "Primary Viewer"}

# Alerts & Config
@router.get("/{id}/alert-config")
def get_alert_config(id: int):
    return {"Config": "Default Alert Config"}

@router.get("/{id}/alerts", response_model=List)
def get_alerts(id: int):
    return [a for a in dd.ProjectAlerts if a.ProjectId == id]

# Budget & Cost
@router.get("/{id}/budget-history")
def get_budget_history(id: int):
    return ["Budget history A", "Budget history B"]

@router.get("/{id}/budget-snapshots/{budget_snapshot_id}")
def get_budget_snapshot(id: int, budget_snapshot_id: int):
    return {"SnapshotId": budget_snapshot_id, "Description": "Snapshot Description"}

@router.get("/{id}/cost-rates")
def get_cost_rates(id: int):
    return ["Cost Rate A", "Cost Rate B"]

# Expense & Fee
@router.get("/{id}/expense-budgets/{exp_budget_id}")
def get_expense_budget(id: int, exp_budget_id: int):
    return {"BudgetId": exp_budget_id, "Amount": 1000}

@router.get("/{id}/expense-plans/{exp_plan_id}")
def get_expense_plan(id: int, exp_plan_id: int):
    return {"PlanId": exp_plan_id, "Name": "Expense Plan Name"}

@router.get("/{id}/expense-types", response_model=List)
def get_expense_types(id: int):
    return dd.ExpenseTypes

@router.get("/{id}/expense-types/{expense_type_id}")
def get_expense_type(id: int, expense_type_id: int):
    return next((e for e in dd.ExpenseTypes if e.Id == expense_type_id), None)
