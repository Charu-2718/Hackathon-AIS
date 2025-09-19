from fastapi import APIRouter, HTTPException
from typing import List
from app.data import dummy_data as dd

router = APIRouter(prefix="/rest/contracts", tags=["Contracts"])

@router.get("/", response_model=List)
def get_contracts():
    return dd.Contracts

@router.get("/{id}")
def get_contract(id: int):
    contract = next((c for c in dd.Contracts if c.Id == id), None)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract

@router.get("/{id}/contract-clauses")
def get_contract_clauses(id: int):
    return [c for c in dd.ContractClauses if c.ContractId == id]

@router.get("/{id}/contract-clauses/{clause_id}")
def get_contract_clause(id: int, clause_id: int):
    clause = next((c for c in dd.ContractClauses if c.Id == clause_id and c.ContractId == id), None)
    if not clause:
        raise HTTPException(status_code=404, detail="Contract clause not found")
    return clause

@router.get("/{id}/mods")
def get_contract_mods(id: int):
    return [m for m in dd.ContractMods if m.ContractId == id]

@router.get("/{id}/mods/{mod_number}")
def get_contract_mod(id: int, mod_number: int):
    mod = next((m for m in dd.ContractMods if m.ContractId == id and m.ModNumber == mod_number), None)
    if not mod:
        raise HTTPException(status_code=404, detail="Contract mod not found")
    return mod

@router.get("/{id}/projects")
def get_contract_projects(id: int):
    return dd.Projects

@router.get("/{id}/projects/available/expense-types")
def get_available_expense_types(id: int):
    return dd.ExpenseTypes

@router.get("/{id}/projects/available/labor-categories")
def get_available_labor_categories(id: int):
    return ["Labor Category A", "Labor Category B"]

@router.get("/{id}/projects/available/tasks")
def get_available_tasks(id: int):
    return ["Task A", "Task B"]

@router.get("/{id}/wage-determinations")
def get_wage_determinations(id: int):
    return [w for w in dd.WageDeterminations if w.ContractId == id]

@router.get("/{id}/wage-determinations/{wage_determination_id}")
def get_wage_determination(id: int, wage_determination_id: int):
    wd = next((w for w in dd.WageDeterminations if w.Id == wage_determination_id and w.ContractId == id), None)
    if not wd:
        raise HTTPException(status_code=404, detail="Wage determination not found")
    return wd

@router.get("/additional-item-types")
def get_additional_item_types():
    return dd.AdditionalItemTypes

@router.get("/billing-analysts")
def get_billing_analysts():
    return dd.BillingAnalysts

@router.get("/contract-clauses")
def get_all_contract_clauses():
    return dd.ContractClauses

@router.get("/contract-clauses/{id}")
def get_contract_clause_by_id(id: int):
    clause = next((c for c in dd.ContractClauses if c.Id == id), None)
    if not clause:
        raise HTTPException(status_code=404, detail="Contract clause not found")
    return clause

@router.get("/contract-clauses/agencies")
def get_contract_clause_agencies():
    return ["Agency A", "Agency B"]

@router.get("/contract-clauses/agencies/{id}")
def get_contract_clause_agency(id: int):
    return {"Id": id, "Name": f"Agency {id}"}

@router.get("/contract-clauses/import/definition")
def get_import_field_definition():
    return {"Fields": ["Field1", "Field2"]}

@router.get("/contract-managers")
def get_contract_managers():
    return dd.ContractManagers

@router.get("/owning-organizations")
def get_owning_organizations():
    return dd.OwningOrganizations

@router.get("/owning-organizations/{owning_org_id}/master-contracts")
def get_master_contracts(owning_org_id: int):
    return [m for m in dd.MasterContracts if m.OwningOrgId == owning_org_id]

@router.get("/provisions")
def get_provisions():
    return dd.Provisions

@router.get("/statuses")
def get_statuses():
    return dd.ContractStatuses

@router.get("/statuses/{id}")
def get_status_by_id(id: int):
    status = next((s for s in dd.ContractStatuses if s.Id == id), None)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@router.get("/types")
def get_types():
    return dd.ContractTypes

@router.get("/types/{id}")
def get_type_by_id(id: int):
    type_ = next((t for t in dd.ContractTypes if t.Id == id), None)
    if not type_:
        raise HTTPException(status_code=404, detail="Contract type not found")
    return type_
