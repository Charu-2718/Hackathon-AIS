from datetime import date, timedelta
from app.models.attachment import Attachment
from app.models.billing_analyst import BillingAnalyst
from app.models.contract import Contract
from app.models.contract_clause import ContractClause
from app.models.contract_manager import ContractManager
from app.models.contract_mod import ContractMod
from app.models.contract_status import ContractStatus
from app.models.contract_type import ContractType
from app.models.expense import Expense
from app.models.expense_attachment import ExpenseAttachment
from app.models.expense_detail import ExpenseDetail
from app.models.expense_history import ExpenseHistory
from app.models.expense_type import ExpenseType
from app.models.master_contract import MasterContract
from app.models.meal_cap import MealCap
from app.models.owning_organization import OwningOrganization
from app.models.payment_method import PaymentMethod
from app.models.people import (
    AccrualPlan,
    Alternate,
    ApprovalGroup,
    BenefitsValue,
    Person,
    PersonAttachment,
    PersonSummary,
    Rate,
    Skill,
)
from app.models.project import Project
from app.models.project_account import ProjectAccount
from app.models.project_alert import ProjectAlert
from app.models.project_type import ProjectType
from app.models.provision import Provision
from app.models.timesheet import Timesheet
from app.models.timesheet_adjustment import TimesheetAdjustment
from app.models.timesheet_attachment import TimesheetAttachment
from app.models.timesheet_audit import TimesheetAudit
from app.models.vat_location import VatLocation
from app.models.wage_determination import WageDetermination

# -----------------
# Contracts
# -----------------
Contracts = [
    Contract(Id=1, Name="Contract A", Status="Active"),
    Contract(Id=2, Name="Contract B", Status="Closed"),
]

ContractClauses = [
    ContractClause(Id=1, ContractId=1, Text="Clause A1"),
    ContractClause(Id=2, ContractId=1, Text="Clause A2"),
    ContractClause(Id=3, ContractId=2, Text="Clause B1"),
]

ContractMods = [
    ContractMod(ModNumber=1, ContractId=1, Description="Mod 1 for Contract A"),
    ContractMod(ModNumber=2, ContractId=2, Description="Mod 1 for Contract B"),
]

WageDeterminations = [
    WageDetermination(Id=1, ContractId=1, Name="WD 1"),
    WageDetermination(Id=2, ContractId=2, Name="WD 2"),
]

AdditionalItemTypes = [
    Attachment(Id=1, Name="Item Type A"),
    Attachment(Id=2, Name="Item Type B"),
]

BillingAnalysts = [
    BillingAnalyst(Id=1, Name="Analyst A"),
    BillingAnalyst(Id=2, Name="Analyst B"),
]

ContractManagers = [
    ContractManager(Id=1, Name="Manager A"),
    ContractManager(Id=2, Name="Manager B"),
]

OwningOrganizations = [
    OwningOrganization(Id=1, Name="Org A"),
    OwningOrganization(Id=2, Name="Org B"),
]

MasterContracts = [
    MasterContract(Id=1, OwningOrgId=1, Name="Master Contract A"),
    MasterContract(Id=2, OwningOrgId=2, Name="Master Contract B"),
]

Provisions = [
    Provision(Id=1, Name="Provision A"),
    Provision(Id=2, Name="Provision B"),
]

ContractStatuses = [
    ContractStatus(Id=1, Name="Active"),
    ContractStatus(Id=2, Name="Closed"),
]

ContractTypes = [
    ContractType(Id=1, Name="Fixed Price"),
    ContractType(Id=2, Name="Time & Materials"),
]

# -----------------
# Expenses
# -----------------
Expenses = [
    Expense(Id=1, ProjectId=1, Amount=150.75, Description="Office supplies"),
    Expense(Id=2, ProjectId=2, Amount=300.00, Description="Client entertainment"),
]

ExpenseAttachments = [
    ExpenseAttachment(Id=1, ExpenseId=1, FileName="receipt1.pdf"),
    ExpenseAttachment(Id=2, ExpenseId=2, FileName="receipt2.pdf"),
]

ExpenseDetails = [
    ExpenseDetail(Id=1, ExpenseId=1, Description="Detail A"),
    ExpenseDetail(Id=2, ExpenseId=2, Description="Detail B"),
]

ExpenseTypes = [
    ExpenseType(Id=1, Name="Travel"),
    ExpenseType(Id=2, Name="Office"),
]

ExpenseHistories = [
    ExpenseHistory(Id=1, ExpenseId=1, Status="Pending", Date=date.today() - timedelta(days=2)),
    ExpenseHistory(Id=2, ExpenseId=1, Status="Approved", Date=date.today() - timedelta(days=1)),
]

MealCaps = [
    MealCap(ExpenseId=1, MaxAmount=50.00),
]

PaymentMethods = [
    PaymentMethod(ExpenseId=1, Method="Credit Card"),
    PaymentMethod(ExpenseId=2, Method="Bank Transfer"),
]

ExpenseProjectTypes = [
    ProjectType(Id=1, Name="Internal"),
    ProjectType(Id=2, Name="Client"),
]

VatLocations = [
    VatLocation(Id=1, Name="India"),
    VatLocation(Id=2, Name="USA"),
]

# -----------------
# Projects
# -----------------
Projects = [
    Project(Id=1, Name="Project Alpha", Client="Client X"),
    Project(Id=2, Name="Project Beta", Client="Client Y"),
]

ProjectAccounts = [
    ProjectAccount(Id=1, ProjectId=1, Name="Account A"),
    ProjectAccount(Id=2, ProjectId=2, Name="Account B"),
]

ProjectAlerts = [
    ProjectAlert(Id=1, ProjectId=1, Message="Alert 1"),
    ProjectAlert(Id=2, ProjectId=2, Message="Alert 2"),
]

# -----------------
# Timesheets
# -----------------
Timesheets = [
    Timesheet(Id=1, EmployeeId=101, Date=date.today(), HoursWorked=8),
    Timesheet(Id=2, EmployeeId=102, Date=date.today() - timedelta(days=1), HoursWorked=6.5),
]

TimesheetAdjustments = [
    TimesheetAdjustment(Id=1, TimesheetId=1, Reason="Correction"),
]

TimesheetAttachments = [
    TimesheetAttachment(Id=1, TimesheetId=1, FileName="timesheet1.pdf"),
]

TimesheetAudits = [
    TimesheetAudit(Id=1, TimesheetId=1, Action="Submitted", Date=date.today() - timedelta(days=1)),
]

# -----------------
# People
# -----------------
People = [
    Person(Id=1, Name="Alice Smith", Email="alice@example.com"),
    Person(Id=2, Name="Bob Johnson", Email="bob@example.com"),
]

AccrualPlans = [
    AccrualPlan(Id=1, PersonId=1, PlanName="Vacation Plan"),
    AccrualPlan(Id=2, PersonId=1, PlanName="Sick Leave"),
]

Alternates = [
    Alternate(Id=1, PersonId=1, Name="Manager A"),
    Alternate(Id=2, PersonId=2, Name="Manager B"),
]

ApprovalGroups = [
    ApprovalGroup(Id=1, PersonId=1, Type="Approver"),
    ApprovalGroup(Id=2, PersonId=1, Type="ExpenseReport"),
]

PersonAttachments = [
    PersonAttachment(Id=1, PersonId=1, FileName="resume.pdf"),
]

AvailableAlternates = [
    Alternate(Id=3, PersonId=1, Name="Alt A"),
    Alternate(Id=4, PersonId=2, Name="Alt B"),
]

BenefitsValues = [
    BenefitsValue(Id=1, PersonId=1, PackageName="Standard Benefits"),
]

Rates = [
    Rate(Id=1, PersonId=1, Amount=100.0),
    Rate(Id=2, PersonId=2, Amount=120.0),
]

Skills = [
    Skill(Id=1, PersonId=1, SkillName="Python"),
    Skill(Id=2, PersonId=1, SkillName="FastAPI"),
]

PeopleSummaries = [
    PersonSummary(Id=1, Name="Alice Smith"),
    PersonSummary(Id=2, Name="Bob Johnson"),
]
