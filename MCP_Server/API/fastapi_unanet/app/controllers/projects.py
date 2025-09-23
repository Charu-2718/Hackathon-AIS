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

# Fees
@router.get("/{id}/fees")
def get_project_fees(id: int):
    return [f for f in dd.ProjectFees if f.ProjectId == id]

# Fundings
@router.get("/{id}/fundings")
def get_project_fundings(id: int):
    return [f for f in dd.ProjectFundings if f.ProjectId == id]

# History
@router.get("/{id}/history")
def get_project_history(id: int):
    return [h for h in dd.ProjectHistories if h.ProjectId == id]

# Locations
@router.get("/{id}/locations")
def get_project_locations(id: int):
    return [l for l in dd.ProjectLocations if l.ProjectId == id]

# Milestones
@router.get("/{id}/milestones")
def get_project_milestones(id: int):
    return [m for m in dd.ProjectMilestones if m.ProjectId == id]

# Notes
@router.get("/{id}/notes")
def get_project_notes(id: int):
    return [n for n in dd.ProjectNotes if n.ProjectId == id]

# Organizations
@router.get("/{id}/organizations")
def get_project_organizations(id: int):
    return [o for o in dd.ProjectOrganizations if o.ProjectId == id]

# Periods
@router.get("/{id}/periods")
def get_project_periods(id: int):
    return [p for p in dd.ProjectPeriods if p.ProjectId == id]

# Project Types
@router.get("/{id}/project-types")
def get_project_types(id: int):
    return [t for t in dd.ProjectTypes if t.ProjectId == id]

# Rates
@router.get("/{id}/rates")
def get_project_rates(id: int):
    return [r for r in dd.ProjectRates if r.ProjectId == id]

# Resources
@router.get("/{id}/resources")
def get_project_resources(id: int):
    return [r for r in dd.ProjectResources if r.ProjectId == id]

# Revenues
@router.get("/{id}/revenues")
def get_project_revenues(id: int):
    return [r for r in dd.ProjectRevenues if r.ProjectId == id]

# Tasks
@router.get("/{id}/tasks")
def get_project_tasks(id: int):
    return [t for t in dd.ProjectTasks if t.ProjectId == id]

# Teams
@router.get("/{id}/teams")
def get_project_teams(id: int):
    return [t for t in dd.ProjectTeams if t.ProjectId == id]
