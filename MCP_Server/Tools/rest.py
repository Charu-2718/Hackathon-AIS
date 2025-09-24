import pandas as pd

def fetch_table_contract():
    endpoints = [
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
        "/rest/contracts/types/{id}",
    ]

    intents = [
        "Retrieve a complete list of all contracts available in the system, including basic contract details such as ID, title, and status.",
        "Retrieve detailed information about a specific contract by its unique ID, including parties, dates, and key metadata.",
        "List all clauses associated with a specific contract, showing each clause’s title, type, and description.",
        "Retrieve the details of a specific contract clause by its clause ID within a contract, including text, type, and applicable rules.",
        "List all modifications made to a specific contract, including mod number, description, and dates of changes.",
        "Retrieve detailed information about a specific contract modification by its mod number, including changes and effective date.",
        "List all projects linked to a specific contract, showing project names, IDs, and associated budget information.",
        "Retrieve all available expense types for a specific contract, including description and applicable rules.",
        "List all labor categories available for a specific contract, including rates, roles, and classification.",
        "Retrieve a list of all tasks available under a specific contract, including task descriptions and assigned roles.",
        "List all wage determinations applicable to a specific contract, including classification, rates, and effective dates.",
        "Retrieve detailed information about a specific wage determination by ID, including labor category, pay rate, and rules.",
        "List all types of additional items that can be associated with contracts, including their description and usage rules.",
        "Retrieve a list of all billing analysts responsible for contracts, including their contact information and roles.",
        "Retrieve all contract clauses available across all contracts, including their titles, types, and descriptions.",
        "Retrieve details of a specific contract clause by its global ID, including text, type, and applicable rules.",
        "List all agencies associated with contract clauses, including agency name, ID, and relevant clause information.",
        "Retrieve detailed information about a specific agency related to contract clauses, including rules and applicable contracts.",
        "Retrieve a list of all fields defined in the contract clause import template, including name, type, and required status.",
        "List all contract managers responsible for managing contracts, including their contact details and assigned contracts.",
        "Retrieve all organizations that own or manage contracts in the system, including names, IDs, and associated contracts.",
        "List all master contracts associated with a specific owning organization, including contract ID, title, and status.",
        "Retrieve all contract provisions, including provision ID, text, type, and applicable contracts.",
        "List all contract statuses available in the system, including status ID, name, and description.",
        "Retrieve detailed information about a specific contract status by ID, including name, description, and rules.",
        "List all contract types defined in the system, including type ID, name, and description.",
        "Retrieve detailed information about a specific contract type by ID, including name, description, and applicable rules.",
    ]

    data = {
        "ID": list(range(1, len(endpoints) + 1)),
        "API Endpoint": endpoints,
        "Intents": intents,
    }
    return pd.DataFrame(data)

def fetch_table_expenses():
    endpoints = [
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
        "/rest/expenses/vat-locations/{id}",
    ]

    intents = [
        "Retrieve detailed information about a specific expense, including date, amount, and associated project or category.",
        "List all attachments associated with a specific expense, including file names and metadata.",
        "Retrieve a specific attachment for a particular expense by attachment ID, including file details.",
        "Get a specific expense detail by detail ID, including line items, descriptions, and amounts.",
        "List all available expense types for categorizing expenses, including descriptions and applicable rules.",
        "Retrieve the full history of a specific expense, including submission, approval, and modification events.",
        "Get the meal cap information applicable to a specific expense, including limits and rules.",
        "List all available payment methods for a specific expense, including method type and details.",
        "Retrieve all available project types associated with a specific expense, including project classifications.",
        "List all projects linked to a specific expense, including project IDs and names.",
        "Validate a specific expense to ensure all required fields, amounts, and approvals are correct.",
        "List all projects by their owners, including project IDs, names, and responsible personnel.",
        "Retrieve all VAT (Value Added Tax) locations available for expenses, including names and IDs.",
        "Get detailed information about a specific VAT location by its ID, including applicable rules and address.",
    ]

    data = {
        "ID": list(range(1, len(endpoints) + 1)),
        "API Endpoint": endpoints,
        "Intents": intents,
    }
    return pd.DataFrame(data)

def fetch_table_people():
    endpoints = [
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
        "/rest/people/list",
    ]

    intents = [
        "Retrieve a complete list of all people in the system, including basic details such as name, ID, and role.",
        "Get detailed information about a specific person by their unique ID, including personal and professional details.",
        "List all accrual plans associated with a specific person, showing plan names, balances, and types.",
        "Retrieve detailed information about a specific accrual plan for a person by plan ID, including dates and balances.",
        "List all alternate contacts for a specific person, including names, roles, and contact information.",
        "List all approval groups where the person acts as an approver, including group names and responsibilities.",
        "List all expense report approval groups associated with a specific person as a submitter.",
        "List all expense request approval groups associated with a specific person as a submitter.",
        "List all leave approval groups associated with a specific person as a submitter.",
        "List all time approval groups associated with a specific person as a submitter.",
        "Retrieve all attachments associated with a specific person, including file names, types, and metadata.",
        "Get a specific attachment for a person by attachment ID, including detailed file information.",
        "List all alternates available for a person, including names and roles, for approval or delegation purposes.",
        "Retrieve all benefit values for a specific person, including benefit type, amount, and eligibility.",
        "Get detailed information about a specific benefit value by ID for a person.",
        "Retrieve the classification information of a person for a specific date, including role and position details.",
        "Get payroll details for a specific person, including salary, deductions, and payment history.",
        "List all pay rates associated with a person, including rate type, amount, and effective dates.",
        "Get a specific pay rate for a person by rate ID, including details and applicability.",
        "List all skills associated with a person, including skill names, levels, and certifications.",
        "Retrieve a summary list of people, including key details like name, ID, and department.",
    ]

    data = {
        "ID": list(range(1, len(endpoints) + 1)),
        "API Endpoint": endpoints,
        "Intents": intents,
    }
    return pd.DataFrame(data)

def fetch_table_projects():
    endpoints = [
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
        "/rest/projects/{id}/expense-types/{expense_type_id}",
    ]

    intents = [
        "Retrieve detailed information about a specific project, including project ID, name, description, and status.",
        "List all accounts associated with a specific project, including account IDs and details.",
        "List all alternate billing managers for a specific project, including their names and roles.",
        "Retrieve the primary billing manager for a project, including contact details and responsibilities.",
        "List all alternate billing viewers for a specific project, including names and permissions.",
        "Retrieve the primary billing viewer for a project, including roles and access details.",
        "List all alternate customers for a project, including customer names and IDs.",
        "Retrieve the primary customer for a project, including detailed contact and role information.",
        "List all alternate document viewers for a project, including names and permissions.",
        "Retrieve the primary document viewer for a project, including access and responsibility details.",
        "List all alternate leads associated with a project, including names and roles.",
        "Retrieve the primary lead for a project, including contact details and assigned responsibilities.",
        "List all alternate managers for a project, including names and roles.",
        "Retrieve the primary manager for a project, including contact details and responsibilities.",
        "List all alternate PO (Purchase Order) viewers for a project, including names and access permissions.",
        "Retrieve the primary PO viewer for a project, including role and contact information.",
        "List all alternate PR (Purchase Request) viewers for a project, including names and permissions.",
        "Retrieve the primary PR viewer for a project, including responsibilities and contact details.",
        "List all alternate project approvers, including names and approval roles.",
        "Retrieve the primary project approver for a project, including responsibilities and contact details.",
        "List all alternate resource assigners for a project, including names and roles.",
        "Retrieve the primary resource assigner for a project, including role and responsibilities.",
        "List all alternate resource planners for a project, including names and assigned tasks.",
        "Retrieve the primary resource planner for a project, including responsibilities and contact info.",
        "List all alternate resource requestors for a project, including names and roles.",
        "Retrieve the primary resource requestor for a project, including responsibilities and contact info.",
        "List all alternate viewers for a project, including access permissions and names.",
        "Retrieve the primary viewer for a project, including role and access details.",
        "Retrieve the alert configuration for a project, including settings and thresholds.",
        "List all alerts associated with a project, including alert types, dates, and status.",
        "Retrieve the budget history for a project, including historical budgets and changes over time.",
        "Get a specific budget snapshot for a project, including snapshot ID, amounts, and date.",
        "List all cost rates associated with a project, including labor rates and overheads.",
        "Retrieve a specific expense budget for a project, including budget ID, amount, and allocations.",
        "Retrieve a specific expense plan for a project, including plan ID, type, and budget allocations.",
        "List all expense types available for a project, including type names and descriptions.",
        "Retrieve detailed information about a specific expense type for a project, including type ID and rules.",
    ]

    data = {
        "ID": list(range(1, len(endpoints) + 1)),
        "API Endpoint": endpoints,
        "Intents": intents,
    }
    return pd.DataFrame(data)

def fetch_table_timesheets():
    endpoints = [
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
        "/rest/time/{id}/validate",
    ]

    intents = [
        "Retrieve a complete list of all timesheets in the system, including basic timesheet IDs, periods, and status.",
        "Get detailed information for a specific timesheet by ID, including employee, hours, and approval status.",
        "List all adjustments applied to a specific timesheet, including adjustment type, amount, and reason.",
        "Retrieve a specific attachment associated with a timesheet by attachment ID, including file details.",
        "List all attachments for a specific timesheet, including file names, types, and metadata.",
        "Get the full audit log for a specific timesheet, showing changes, approvals, and submissions.",
        "Show auto-fill options applied to a specific timesheet, including generated hours and adjustments.",
        "List deleted auto-fill entries for a specific timesheet, including who deleted them and when.",
        "Retrieve the complete history for a specific timesheet, including submission, approval, and modification events.",
        "Get the audit log for individual items in a timesheet, including changes and responsible personnel.",
        "Retrieve offline timesheet data for a specific timesheet, useful for offline review or processing.",
        "List all project types associated with a timesheet, including names and classifications of project categories.",
        "List all projects linked to a specific timesheet, including project IDs, names, and relevant hours.",
        "Get labor categories associated with a project in a timesheet, including category names, roles, and rates.",
        "Retrieve all locations associated with a project in a timesheet, including site names and codes.",
        "Get labor categories for a specific task within a timesheet, including names, roles, and applicable rates.",
        "Get locations for a specific task within a timesheet, including site details and codes.",
        "Validate a specific timesheet to ensure all required fields, hours, and approvals are correct and complete.",
    ]

    data = {
        "ID": list(range(1, len(endpoints) + 1)),
        "API Endpoint": endpoints,
        "Intents": intents,
    }
    return pd.DataFrame(data)


# print("Contracts:", df_contract.shape)
# print("Expenses:", df_expenses.shape)
# print("People:", df_people.shape)
# print("Projects:", df_projects.shape)
# print("Timesheets:", fetch_table_timesheets().shape)
