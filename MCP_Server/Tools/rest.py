import pandas as pd

def fetch_table_contract():
    data = {
        "ID": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
        ],
        "API Endpoint": [
            "/rest/contracts/",
            "/rest/contracts/{id}",
            "/rest/contracts/{id}/contract-clauses",
            "/rest/contracts/{id}/contract-clauses/{clause_id}",
            "/rest/contracts/{id}/mods",
            "/rest/contracts/{id}/mods/{mod_number}",
            "/rest/contracts/{id}/projects",
            "/rest/contracts/{id}/projects/available/expense-types",
            "/rest/contracts/{id}/projects/available/labor-categories",
            "/rest/contracts/{id}/projects/available/tasks",
            "/rest/contracts/{id}/wage-determinations",
            "/rest/contracts/{id}/wage-determinations/{wage_determination_id}",
            "/rest/contracts/additional-item-types",
            "/rest/contracts/billing-analysts",
            "/rest/contracts/contract-clauses",
            "/rest/contracts/contract-clauses/{id}",
            "/rest/contracts/contract-clauses/agencies",
            "/rest/contracts/contract-clauses/agencies/{id}",
            "/rest/contracts/contract-clauses/import/definition",
            "/rest/contracts/contract-managers",
            "/rest/contracts/owning-organizations",
            "/rest/contracts/owning-organizations/{owning_org_id}/master-contracts",
            "/rest/contracts/provisions",
            "/rest/contracts/statuses",
            "/rest/contracts/statuses/{id}",
            "/rest/contracts/types",
            "/rest/contracts/types/{id}"
        ],
        "Example Intent String": [
            "List all contracts.",
            "Get a specific contract's details.",
            "List all contract clauses.",
            "Get a specific contract clause.",
            "List contract modifications.",
            "Get a specific modification.",
            "List projects for a contract.",
            "List available expense types for a contract.",
            "List available labor categories for a contract.",
            "List available tasks for a contract.",
            "List wage determinations for a contract.",
            "Get a specific wage determination.",
            "List all additional item types.",
            "List all billing analysts.",
            "List all contract clauses.",
            "Get a specific contract clause.",
            "List all contract clause agencies.",
            "Get specific agency details.",
            "What fields are in the contract clause import definition?",
            "List all contract managers.",
            "List all owning organizations.",
            "List master contracts for an owning organization.",
            "List all provisions.",
            "List all contract statuses.",
            "Get a specific contract status.",
            "List all contract types.",
            "Get a specific contract type."
        ]
    }

    # Create a pandas DataFrame from the dictionary
    return pd.DataFrame(data)

def fetch_table_expenses():
    data = {
        "ID": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
        ],
        "API Endpoint": [
            "/rest/expenses/{id}",
            "/rest/expenses/{id}/attachments",
            "/rest/expenses/{id}/attachments/{attachment_id}",
            "/rest/expenses/{id}/details/{detail_id}",
            "/rest/expenses/{id}/expense-types",
            "/rest/expenses/{id}/history",
            "/rest/expenses/{id}/meal-caps",
            "/rest/expenses/{id}/payment-methods",
            "/rest/expenses/{id}/project-types",
            "/rest/expenses/{id}/projects",
            "/rest/expenses/{id}/validate",
            "/rest/expenses/projects",
            "/rest/expenses/vat-locations",
            "/rest/expenses/vat-locations/{id}"
        ],
        "Example Intent String": [
            "Get expense details.",
            "List expense attachments.",
            "Get a specific attachment.",
            "Get a specific detail.",
            "List expense types.",
            "Show expense history.",
            "What is the meal cap?",
            "List payment methods.",
            "What are the project types?",
            "List projects.",
            "Validate the expense.",
            "List projects by owner.",
            "List all VAT locations.",
            "Get a specific VAT location."
        ]
    }

    return pd.DataFrame(data)

def fetch_table_people():
    data = {
        "ID": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
        ],
        "API Endpoint": [
            "/rest/people",
            "/rest/people/{id}",
            "/rest/people/{id}/accrual-plans",
            "/rest/people/{id}/accrual-plans/{personAccrualPlanId}",
            "/rest/people/{id}/alternates",
            "/rest/people/{id}/approval-groups/approver",
            "/rest/people/{id}/approval-groups/submitter/expense-report",
            "/rest/people/{id}/approval-groups/submitter/expense-request",
            "/rest/people/{id}/approval-groups/submitter/leave",
            "/rest/people/{id}/approval-groups/submitter/time",
            "/rest/people/{id}/attachments",
            "/rest/people/{id}/attachments/{attachmentId}",
            "/rest/people/{id}/available-alternates",
            "/rest/people/{id}/benefits-values",
            "/rest/people/{id}/benefits-values/{benefitsValueId}",
            "/rest/people/{id}/classification/{date}",
            "/rest/people/{id}/payroll",
            "/rest/people/{id}/rates",
            "/rest/people/{id}/rates/{rateId}",
            "/rest/people/{id}/skills",
            "/rest/people/list"
        ],
        "Example Intent String": [
            "List all people.",
            "Get person details.",
            "List person's accrual plans.",
            "Get a specific accrual plan.",
            "List a person's alternates.",
            "List approver groups.",
            "List expense report approval groups.",
            "List expense request approval groups.",
            "List leave approval groups.",
            "List time approval groups.",
            "List person's attachments.",
            "Get a specific attachment.",
            "List available alternates.",
            "List person's benefits.",
            "Get a specific benefit.",
            "Get person's classification.",
            "Get person's payroll details.",
            "List person's rates.",
            "Get a specific rate.",
            "List person's skills.",
            "Get a summary of people."
        ]
    }

    return pd.DataFrame(data)

def fetch_table_projects():
    data = {
        "ID": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
        ],
        "API Endpoint": [
            "/rest/projects/{id}",
            "/rest/projects/{id}/accounts",
            "/rest/projects/{id}/admin/billing-managers/alternate",
            "/rest/projects/{id}/admin/billing-managers/primary",
            "/rest/projects/{id}/admin/billing-viewers/alternate",
            "/rest/projects/{id}/admin/billing-viewers/primary",
            "/rest/projects/{id}/admin/customers/alternates",
            "/rest/projects/{id}/admin/customers/primary",
            "/rest/projects/{id}/admin/document-viewers/alternate",
            "/rest/projects/{id}/admin/document-viewers/primary",
            "/rest/projects/{id}/admin/leads/alternate",
            "/rest/projects/{id}/admin/leads/primary",
            "/rest/projects/{id}/admin/managers/alternate",
            "/rest/projects/{id}/admin/managers/primary",
            "/rest/projects/{id}/admin/po-viewers/alternate",
            "/rest/projects/{id}/admin/po-viewers/primary",
            "/rest/projects/{id}/admin/pr-viewers/alternate",
            "/rest/projects/{id}/admin/pr-viewers/primary",
            "/rest/projects/{id}/admin/project-approvers/alternates",
            "/rest/projects/{id}/admin/project-approvers/primary",
            "/rest/projects/{id}/admin/resource-assigners/alternate",
            "/rest/projects/{id}/admin/resource-assigners/primary",
            "/rest/projects/{id}/admin/resource-planners/alternate",
            "/rest/projects/{id}/admin/resource-planners/primary",
            "/rest/projects/{id}/admin/resource-requestors/alternate",
            "/rest/projects/{id}/admin/resource-requestors/primary",
            "/rest/projects/{id}/admin/viewers/alternate",
            "/rest/projects/{id}/admin/viewers/primary",
            "/rest/projects/{id}/alert-config",
            "/rest/projects/{id}/alerts",
            "/rest/projects/{id}/budget-history",
            "/rest/projects/{id}/budget-snapshots/{budget_snapshot_id}",
            "/rest/projects/{id}/cost-rates",
            "/rest/projects/{id}/expense-budgets/{exp_budget_id}",
            "/rest/projects/{id}/expense-plans/{exp_plan_id}",
            "/rest/projects/{id}/expense-types",
            "/rest/projects/{id}/expense-types/{expense_type_id}"
        ],
        "Example Intent String": [
            "Get project details.",
            "List project accounts.",
            "List alternate billing managers.",
            "Get primary billing manager.",
            "List alternate billing viewers.",
            "Get primary billing viewer.",
            "List alternate customers.",
            "Get primary customer.",
            "List alternate document viewers.",
            "Get primary document viewer.",
            "List alternate leads.",
            "Get primary lead.",
            "List alternate managers.",
            "Get primary manager.",
            "List alternate PO viewers.",
            "Get primary PO viewer.",
            "List alternate PR viewers.",
            "Get primary PR viewer.",
            "List alternate project approvers.",
            "Get primary project approver.",
            "List alternate resource assigners.",
            "Get primary resource assigner.",
            "List alternate resource planners.",
            "Get primary resource planner.",
            "List alternate resource requestors.",
            "Get primary resource requestor.",
            "List alternate viewers.",
            "Get primary viewer.",
            "Get project alert configuration.",
            "List project alerts.",
            "Show budget history.",
            "Get a specific budget snapshot.",
            "List project cost rates.",
            "Get a specific expense budget.",
            "Get a specific expense plan.",
            "List project expense types.",
            "Get a specific expense type."
        ]
    }

    return pd.DataFrame(data)

def fetch_table_timesheets():
    data = {
        "ID": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
        ],
        "API Endpoint": [
            "/rest/time",
            "/rest/time/{id}",
            "/rest/time/{id}/adjustments",
            "/rest/time/{id}/attachment/{attachmentId}",
            "/rest/time/{id}/attachments",
            "/rest/time/{id}/audit",
            "/rest/time/{id}/auto-fill",
            "/rest/time/{id}/auto-fill/deleted",
            "/rest/time/{id}/history",
            "/rest/time/{id}/items/audit",
            "/rest/time/{id}/offline",
            "/rest/time/{id}/project-types",
            "/rest/time/{id}/projects",
            "/rest/time/{id}/projects/{projectId}/labor-categories",
            "/rest/time/{id}/projects/{projectId}/locations",
            "/rest/time/{id}/tasks/{taskId}/labor-categories",
            "/rest/time/{id}/tasks/{taskId}/locations",
            "/rest/time/{id}/validate"
        ],
        "Example Intent String": [
            "Get all timesheets.",
            "Get details for a specific timesheet.",
            "List timesheet adjustments.",
            "Get a specific timesheet attachment.",
            "List timesheet attachments.",
            "Get the timesheet audit log.",
            "Show auto-fill options for the timesheet.",
            "List deleted auto-fill data for the timesheet.",
            "View the history for this timesheet.",
            "Get the audit log for timesheet items.",
            "Retrieve the offline timesheet data.",
            "List available project types for the timesheet.",
            "List projects associated with the timesheet.",
            "Get labor categories for this project.",
            "Get locations for this project.",
            "Get labor categories for a specific task.",
            "Get locations for a specific task.",
            "Validate the timesheet."
        ]
    }

    # Create a pandas DataFrame from the dictionary
    return pd.DataFrame(data)