from datetime import date, timedelta
from app.models.ProjectsModels import ProjectFee,ProjectFunding,ProjectHistory,ProjectLocation,ProjectMilestone,ProjectNote,ProjectOrganization,ProjectPeriod,ProjectRate,ProjectResource,ProjectRevenue,ProjectTask,ProjectTeam,ProjectTypeAssignment
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
    Contract(Id=3, Name="Contract C", Status="Active"),
    Contract(Id=4, Name="Contract D", Status="Active"),
    Contract(Id=5, Name="Contract E", Status="Closed"),
    Contract(Id=6, Name="Contract F", Status="Active"),
    Contract(Id=7, Name="Contract G", Status="Active"),
    Contract(Id=8, Name="Contract H", Status="Closed"),
    Contract(Id=9, Name="Contract I", Status="Active"),
    Contract(Id=10, Name="Contract J", Status="Closed"),
]

# -----------------
# Contract Clauses
# -----------------
ContractClauses = [
    ContractClause(Id=1, ContractId=1, Text="Clause A1"),
    ContractClause(Id=2, ContractId=1, Text="Clause A2"),
    ContractClause(Id=3, ContractId=2, Text="Clause B1"),
    ContractClause(Id=4, ContractId=3, Text="Clause C1"),
    ContractClause(Id=5, ContractId=3, Text="Clause C2"),
    ContractClause(Id=6, ContractId=4, Text="Clause D1"),
    ContractClause(Id=7, ContractId=5, Text="Clause E1"),
    ContractClause(Id=8, ContractId=6, Text="Clause F1"),
    ContractClause(Id=9, ContractId=7, Text="Clause G1"),
    ContractClause(Id=10, ContractId=8, Text="Clause H1"),
]

# -----------------
# Contract Mods
# -----------------
ContractMods = [
    ContractMod(ModNumber=1, ContractId=1, Description="Mod 1 for Contract A"),
    ContractMod(ModNumber=2, ContractId=2, Description="Mod 1 for Contract B"),
    ContractMod(ModNumber=3, ContractId=3, Description="Mod 1 for Contract C"),
    ContractMod(ModNumber=4, ContractId=3, Description="Mod 2 for Contract C"),
    ContractMod(ModNumber=5, ContractId=4, Description="Mod 1 for Contract D"),
    ContractMod(ModNumber=6, ContractId=5, Description="Mod 1 for Contract E"),
    ContractMod(ModNumber=7, ContractId=6, Description="Mod 1 for Contract F"),
    ContractMod(ModNumber=8, ContractId=7, Description="Mod 1 for Contract G"),
    ContractMod(ModNumber=9, ContractId=8, Description="Mod 1 for Contract H"),
    ContractMod(ModNumber=10, ContractId=9, Description="Mod 1 for Contract I"),
]

# -----------------
# Wage Determinations
# -----------------
WageDeterminations = [
    WageDetermination(Id=1, ContractId=1, Name="WD 1"),
    WageDetermination(Id=2, ContractId=2, Name="WD 2"),
    WageDetermination(Id=3, ContractId=3, Name="WD 3"),
    WageDetermination(Id=4, ContractId=4, Name="WD 4"),
    WageDetermination(Id=5, ContractId=5, Name="WD 5"),
    WageDetermination(Id=6, ContractId=6, Name="WD 6"),
    WageDetermination(Id=7, ContractId=7, Name="WD 7"),
    WageDetermination(Id=8, ContractId=8, Name="WD 8"),
    WageDetermination(Id=9, ContractId=9, Name="WD 9"),
    WageDetermination(Id=10, ContractId=10, Name="WD 10"),
]

# -----------------
# Additional Item Types
# -----------------
AdditionalItemTypes = [
    Attachment(Id=1, Name="Item Type A"),
    Attachment(Id=2, Name="Item Type B"),
    Attachment(Id=3, Name="Item Type C"),
    Attachment(Id=4, Name="Item Type D"),
    Attachment(Id=5, Name="Item Type E"),
    Attachment(Id=6, Name="Item Type F"),
]

# -----------------
# Billing Analysts
# -----------------
BillingAnalysts = [
    BillingAnalyst(Id=1, Name="Analyst A"),
    BillingAnalyst(Id=2, Name="Analyst B"),
    BillingAnalyst(Id=3, Name="Analyst C"),
    BillingAnalyst(Id=4, Name="Analyst D"),
    BillingAnalyst(Id=5, Name="Analyst E"),
    BillingAnalyst(Id=6, Name="Analyst F"),
]

# -----------------
# Contract Managers
# -----------------
ContractManagers = [
    ContractManager(Id=1, Name="Manager A"),
    ContractManager(Id=2, Name="Manager B"),
    ContractManager(Id=3, Name="Manager C"),
    ContractManager(Id=4, Name="Manager D"),
    ContractManager(Id=5, Name="Manager E"),
    ContractManager(Id=6, Name="Manager F"),
]

# -----------------
# Owning Organizations
# -----------------
OwningOrganizations = [
    OwningOrganization(Id=1, Name="Org A"),
    OwningOrganization(Id=2, Name="Org B"),
    OwningOrganization(Id=3, Name="Org C"),
    OwningOrganization(Id=4, Name="Org D"),
    OwningOrganization(Id=5, Name="Org E"),
    OwningOrganization(Id=6, Name="Org F"),
]

# -----------------
# Master Contracts
# -----------------
MasterContracts = [
    MasterContract(Id=1, OwningOrgId=1, Name="Master Contract A"),
    MasterContract(Id=2, OwningOrgId=2, Name="Master Contract B"),
    MasterContract(Id=3, OwningOrgId=3, Name="Master Contract C"),
    MasterContract(Id=4, OwningOrgId=4, Name="Master Contract D"),
    MasterContract(Id=5, OwningOrgId=5, Name="Master Contract E"),
    MasterContract(Id=6, OwningOrgId=6, Name="Master Contract F"),
]

# -----------------
# Provisions
# -----------------
Provisions = [
    Provision(Id=1, Name="Provision A"),
    Provision(Id=2, Name="Provision B"),
    Provision(Id=3, Name="Provision C"),
    Provision(Id=4, Name="Provision D"),
    Provision(Id=5, Name="Provision E"),
    Provision(Id=6, Name="Provision F"),
]

# -----------------
# Contract Statuses
# -----------------
ContractStatuses = [
    ContractStatus(Id=1, Name="Active"),
    ContractStatus(Id=2, Name="Closed"),
    ContractStatus(Id=3, Name="Pending"),
    ContractStatus(Id=4, Name="Suspended"),
]

# -----------------
# Contract Types
# -----------------
ContractTypes = [
    ContractType(Id=1, Name="Fixed Price"),
    ContractType(Id=2, Name="Time & Materials"),
    ContractType(Id=3, Name="Cost Reimbursement"),
    ContractType(Id=4, Name="Incentive"),
]
# -----------------
# Expenses
# -----------------
Expenses = [
    Expense(Id=1, ProjectId=1, Amount=150.75, Description="Office supplies"),
    Expense(Id=2, ProjectId=2, Amount=300.00, Description="Client entertainment"),
    Expense(Id=3, ProjectId=1, Amount=1200.00, Description="Flight tickets"),
    Expense(Id=4, ProjectId=3, Amount=85.50, Description="Team lunch"),
    Expense(Id=5, ProjectId=4, Amount=450.25, Description="Hotel stay"),
    Expense(Id=6, ProjectId=2, Amount=60.00, Description="Taxi fare"),
    Expense(Id=7, ProjectId=3, Amount=250.75, Description="Conference registration"),
    Expense(Id=8, ProjectId=5, Amount=99.99, Description="Software subscription"),
    Expense(Id=9, ProjectId=1, Amount=35.00, Description="Courier charges"),
    Expense(Id=10, ProjectId=4, Amount=175.40, Description="Stationery purchase"),
]

# -----------------
# Expense Attachments
# -----------------
ExpenseAttachments = [
    ExpenseAttachment(Id=1, ExpenseId=1, FileName="receipt1.pdf"),
    ExpenseAttachment(Id=2, ExpenseId=2, FileName="receipt2.pdf"),
    ExpenseAttachment(Id=3, ExpenseId=3, FileName="boardingpass.jpg"),
    ExpenseAttachment(Id=4, ExpenseId=4, FileName="restaurant_bill.png"),
    ExpenseAttachment(Id=5, ExpenseId=5, FileName="hotel_invoice.pdf"),
    ExpenseAttachment(Id=6, ExpenseId=6, FileName="taxi_receipt.pdf"),
    ExpenseAttachment(Id=7, ExpenseId=7, FileName="conference_ticket.pdf"),
    ExpenseAttachment(Id=8, ExpenseId=8, FileName="subscription_invoice.pdf"),
    ExpenseAttachment(Id=9, ExpenseId=9, FileName="courier_slip.jpg"),
    ExpenseAttachment(Id=10, ExpenseId=10, FileName="stationery_bill.pdf"),
]

# -----------------
# Expense Details
# -----------------
ExpenseDetails = [
    ExpenseDetail(Id=1, ExpenseId=1, Description="Pens and notepads"),
    ExpenseDetail(Id=2, ExpenseId=2, Description="Dinner with client"),
    ExpenseDetail(Id=3, ExpenseId=3, Description="Round trip to New York"),
    ExpenseDetail(Id=4, ExpenseId=4, Description="Lunch at Italian restaurant"),
    ExpenseDetail(Id=5, ExpenseId=5, Description="3 nights hotel booking"),
    ExpenseDetail(Id=6, ExpenseId=6, Description="Airport to office"),
    ExpenseDetail(Id=7, ExpenseId=7, Description="Tech conference fees"),
    ExpenseDetail(Id=8, ExpenseId=8, Description="Monthly SaaS license"),
    ExpenseDetail(Id=9, ExpenseId=9, Description="Parcel delivery"),
    ExpenseDetail(Id=10, ExpenseId=10, Description="Printer ink and paper"),
]

# -----------------
# Expense Types
# -----------------
ExpenseTypes = [
    ExpenseType(Id=1, Name="Travel"),
    ExpenseType(Id=2, Name="Office"),
    ExpenseType(Id=3, Name="Accommodation"),
    ExpenseType(Id=4, Name="Meals"),
    ExpenseType(Id=5, Name="Entertainment"),
    ExpenseType(Id=6, Name="Subscription"),
    ExpenseType(Id=7, Name="Transport"),
    ExpenseType(Id=8, Name="Training"),
]

# -----------------
# Expense Histories
# -----------------
ExpenseHistories = [
    ExpenseHistory(Id=1, ExpenseId=1, Status="Pending", Date=date.today() - timedelta(days=2)),
    ExpenseHistory(Id=2, ExpenseId=1, Status="Approved", Date=date.today() - timedelta(days=1)),
    ExpenseHistory(Id=3, ExpenseId=3, Status="Pending", Date=date.today() - timedelta(days=3)),
    ExpenseHistory(Id=4, ExpenseId=3, Status="Rejected", Date=date.today() - timedelta(days=2)),
    ExpenseHistory(Id=5, ExpenseId=5, Status="Pending", Date=date.today() - timedelta(days=4)),
    ExpenseHistory(Id=6, ExpenseId=5, Status="Approved", Date=date.today() - timedelta(days=1)),
]

# -----------------
# Meal Caps
# -----------------
MealCaps = [
    MealCap(ExpenseId=1, MaxAmount=50.00),
    MealCap(ExpenseId=2, MaxAmount=75.00),
    MealCap(ExpenseId=4, MaxAmount=60.00),
    MealCap(ExpenseId=6, MaxAmount=40.00),
]

# -----------------
# Payment Methods
# -----------------
PaymentMethods = [
    PaymentMethod(ExpenseId=1, Method="Credit Card"),
    PaymentMethod(ExpenseId=2, Method="Bank Transfer"),
    PaymentMethod(ExpenseId=3, Method="Cash"),
    PaymentMethod(ExpenseId=4, Method="Credit Card"),
    PaymentMethod(ExpenseId=5, Method="Debit Card"),
    PaymentMethod(ExpenseId=6, Method="Mobile Wallet"),
    PaymentMethod(ExpenseId=7, Method="Credit Card"),
]

# -----------------
# Expense Project Types
# -----------------
ExpenseProjectTypes = [
    ProjectType(Id=1, Name="Internal"),
    ProjectType(Id=2, Name="Client"),
    ProjectType(Id=3, Name="R&D"),
    ProjectType(Id=4, Name="Training"),
]

# -----------------
# VAT Locations
# -----------------
VatLocations = [
    VatLocation(Id=1, Name="India"),
    VatLocation(Id=2, Name="USA"),
    VatLocation(Id=3, Name="UK"),
    VatLocation(Id=4, Name="Germany"),
    VatLocation(Id=5, Name="Australia"),
    VatLocation(Id=6, Name="Singapore"),
]
# -----------------
# Projects
# -----------------
Projects = [
    Project(Id=1, Name="Project Alpha", Client="Client X"),
    Project(Id=2, Name="Project Beta", Client="Client Y"),
    Project(Id=3, Name="Project Gamma", Client="Client Z"),
    Project(Id=4, Name="Project Delta", Client="Client A"),
    Project(Id=5, Name="Project Epsilon", Client="Client B"),
    Project(Id=6, Name="Project Zeta", Client="Client C"),
    Project(Id=7, Name="Project Eta", Client="Client D"),
    Project(Id=8, Name="Project Theta", Client="Client E"),
    Project(Id=9, Name="Project Iota", Client="Client F"),
    Project(Id=10, Name="Project Kappa", Client="Client G"),
]

ProjectAccounts = [
    ProjectAccount(Id=1, ProjectId=1, Name="Account A"),
    ProjectAccount(Id=2, ProjectId=2, Name="Account B"),
    ProjectAccount(Id=3, ProjectId=3, Name="Account C"),
    ProjectAccount(Id=4, ProjectId=4, Name="Account D"),
    ProjectAccount(Id=5, ProjectId=5, Name="Account E"),
    ProjectAccount(Id=6, ProjectId=6, Name="Account F"),
    ProjectAccount(Id=7, ProjectId=7, Name="Account G"),
    ProjectAccount(Id=8, ProjectId=8, Name="Account H"),
    ProjectAccount(Id=9, ProjectId=9, Name="Account I"),
    ProjectAccount(Id=10, ProjectId=10, Name="Account J"),
]

ProjectAlerts = [
    ProjectAlert(Id=1, ProjectId=1, Message="Deadline approaching"),
    ProjectAlert(Id=2, ProjectId=2, Message="Budget exceeded"),
    ProjectAlert(Id=3, ProjectId=3, Message="Client feedback pending"),
    ProjectAlert(Id=4, ProjectId=4, Message="Testing delayed"),
    ProjectAlert(Id=5, ProjectId=5, Message="Resource shortage"),
    ProjectAlert(Id=6, ProjectId=6, Message="New requirement added"),
    ProjectAlert(Id=7, ProjectId=7, Message="Approval required"),
    ProjectAlert(Id=8, ProjectId=8, Message="Phase 1 completed"),
    ProjectAlert(Id=9, ProjectId=9, Message="Data migration pending"),
    ProjectAlert(Id=10, ProjectId=10, Message="Documentation incomplete"),
]

# -----------------
# Projects - Additional Data
# -----------------
ProjectFees = [
    ProjectFee(Id=1, ProjectId=1, Description="Fee A1", Amount=5000.0),
    ProjectFee(Id=2, ProjectId=2, Description="Fee B1", Amount=3000.0),
    ProjectFee(Id=3, ProjectId=3, Description="Fee C1", Amount=4500.0),
    ProjectFee(Id=4, ProjectId=4, Description="Fee D1", Amount=2500.0),
    ProjectFee(Id=5, ProjectId=5, Description="Fee E1", Amount=6000.0),
    ProjectFee(Id=6, ProjectId=6, Description="Fee F1", Amount=7000.0),
    ProjectFee(Id=7, ProjectId=7, Description="Fee G1", Amount=3200.0),
    ProjectFee(Id=8, ProjectId=8, Description="Fee H1", Amount=2800.0),
    ProjectFee(Id=9, ProjectId=9, Description="Fee I1", Amount=5200.0),
    ProjectFee(Id=10, ProjectId=10, Description="Fee J1", Amount=3900.0),
]

ProjectFundings = [
    ProjectFunding(Id=1, ProjectId=1, Source="Funding Source A", Amount=10000.0),
    ProjectFunding(Id=2, ProjectId=2, Source="Funding Source B", Amount=15000.0),
    ProjectFunding(Id=3, ProjectId=3, Source="Funding Source C", Amount=12000.0),
    ProjectFunding(Id=4, ProjectId=4, Source="Funding Source D", Amount=18000.0),
    ProjectFunding(Id=5, ProjectId=5, Source="Funding Source E", Amount=9000.0),
    ProjectFunding(Id=6, ProjectId=6, Source="Funding Source F", Amount=14000.0),
    ProjectFunding(Id=7, ProjectId=7, Source="Funding Source G", Amount=20000.0),
    ProjectFunding(Id=8, ProjectId=8, Source="Funding Source H", Amount=11000.0),
    ProjectFunding(Id=9, ProjectId=9, Source="Funding Source I", Amount=17500.0),
    ProjectFunding(Id=10, ProjectId=10, Source="Funding Source J", Amount=9500.0),
]

ProjectHistories = [
    ProjectHistory(Id=1, ProjectId=1, ChangeDescription="Created project", ChangedBy="Admin"),
    ProjectHistory(Id=2, ProjectId=1, ChangeDescription="Updated budget", ChangedBy="Manager A"),
    ProjectHistory(Id=3, ProjectId=2, ChangeDescription="Updated scope", ChangedBy="Manager B"),
    ProjectHistory(Id=4, ProjectId=3, ChangeDescription="Assigned team", ChangedBy="Admin"),
    ProjectHistory(Id=5, ProjectId=4, ChangeDescription="Extended deadline", ChangedBy="Manager C"),
    ProjectHistory(Id=6, ProjectId=5, ChangeDescription="Added milestone", ChangedBy="Admin"),
    ProjectHistory(Id=7, ProjectId=6, ChangeDescription="Client approval received", ChangedBy="Manager D"),
    ProjectHistory(Id=8, ProjectId=7, ChangeDescription="Changed rate type", ChangedBy="Manager E"),
]

ProjectLocations = [
    ProjectLocation(Id=1, ProjectId=1, Address="123 Main St", City="Mumbai", Country="India"),
    ProjectLocation(Id=2, ProjectId=2, Address="456 Park Ave", City="New York", Country="USA"),
    ProjectLocation(Id=3, ProjectId=3, Address="789 King Rd", City="Toronto", Country="Canada"),
    ProjectLocation(Id=4, ProjectId=4, Address="101 Queen St", City="London", Country="UK"),
    ProjectLocation(Id=5, ProjectId=5, Address="202 Lake Rd", City="Berlin", Country="Germany"),
    ProjectLocation(Id=6, ProjectId=6, Address="303 Hill St", City="Sydney", Country="Australia"),
    ProjectLocation(Id=7, ProjectId=7, Address="404 Palm Ave", City="Singapore", Country="Singapore"),
    ProjectLocation(Id=8, ProjectId=8, Address="505 Rose St", City="Paris", Country="France"),
]

ProjectMilestones = [
    ProjectMilestone(Id=1, ProjectId=1, Name="Milestone 1", DueDate=str(date.today() + timedelta(days=30))),
    ProjectMilestone(Id=2, ProjectId=2, Name="Milestone 2", DueDate=str(date.today() + timedelta(days=45))),
    ProjectMilestone(Id=3, ProjectId=3, Name="Milestone 3", DueDate=str(date.today() + timedelta(days=60))),
    ProjectMilestone(Id=4, ProjectId=4, Name="Milestone 4", DueDate=str(date.today() + timedelta(days=90))),
    ProjectMilestone(Id=5, ProjectId=5, Name="Milestone 5", DueDate=str(date.today() + timedelta(days=120))),
]

ProjectNotes = [
    ProjectNote(Id=1, ProjectId=1, Content="Note A1", Author="Admin"),
    ProjectNote(Id=2, ProjectId=2, Content="Note B1", Author="Manager B"),
    ProjectNote(Id=3, ProjectId=3, Content="Kick-off scheduled", Author="Manager C"),
    ProjectNote(Id=4, ProjectId=4, Content="Budget constraints", Author="Admin"),
    ProjectNote(Id=5, ProjectId=5, Content="Scope discussion", Author="Manager D"),
]

ProjectOrganizations = [
    ProjectOrganization(Id=1, ProjectId=1, OrgName="Org A", Role="Client"),
    ProjectOrganization(Id=2, ProjectId=2, OrgName="Org B", Role="Partner"),
    ProjectOrganization(Id=3, ProjectId=3, OrgName="Org C", Role="Vendor"),
    ProjectOrganization(Id=4, ProjectId=4, OrgName="Org D", Role="Client"),
    ProjectOrganization(Id=5, ProjectId=5, OrgName="Org E", Role="Sponsor"),
]

ProjectPeriods = [
    ProjectPeriod(Id=1, ProjectId=1, StartDate=str(date.today()), EndDate=str(date.today() + timedelta(days=90))),
    ProjectPeriod(Id=2, ProjectId=2, StartDate=str(date.today()), EndDate=str(date.today() + timedelta(days=120))),
    ProjectPeriod(Id=3, ProjectId=3, StartDate=str(date.today()), EndDate=str(date.today() + timedelta(days=150))),
    ProjectPeriod(Id=4, ProjectId=4, StartDate=str(date.today()), EndDate=str(date.today() + timedelta(days=180))),
]

ProjectTypes = [
    ProjectTypeAssignment(Id=1, ProjectId=1, TypeName="Internal"),
    ProjectTypeAssignment(Id=2, ProjectId=2, TypeName="Client"),
    ProjectTypeAssignment(Id=3, ProjectId=3, TypeName="Research"),
    ProjectTypeAssignment(Id=4, ProjectId=4, TypeName="Training"),
    ProjectTypeAssignment(Id=5, ProjectId=5, TypeName="Maintenance"),
]

ProjectRates = [
    ProjectRate(Id=1, ProjectId=1, RateType="Standard", Value=100.0),
    ProjectRate(Id=2, ProjectId=2, RateType="Premium", Value=150.0),
    ProjectRate(Id=3, ProjectId=3, RateType="Discounted", Value=80.0),
    ProjectRate(Id=4, ProjectId=4, RateType="Standard", Value=110.0),
    ProjectRate(Id=5, ProjectId=5, RateType="Premium", Value=160.0),
]

ProjectResources = [
    ProjectResource(Id=1, ProjectId=1, ResourceName="Alice Smith", Role="Developer"),
    ProjectResource(Id=2, ProjectId=2, ResourceName="Bob Johnson", Role="Tester"),
    ProjectResource(Id=3, ProjectId=3, ResourceName="Charlie Brown", Role="Designer"),
    ProjectResource(Id=4, ProjectId=4, ResourceName="David Lee", Role="Project Manager"),
    ProjectResource(Id=5, ProjectId=5, ResourceName="Eva Green", Role="Analyst"),
]

ProjectRevenues = [
    ProjectRevenue(Id=1, ProjectId=1, Amount=20000.0, Period="Q1 2025"),
    ProjectRevenue(Id=2, ProjectId=2, Amount=30000.0, Period="Q1 2025"),
    ProjectRevenue(Id=3, ProjectId=3, Amount=25000.0, Period="Q2 2025"),
    ProjectRevenue(Id=4, ProjectId=4, Amount=40000.0, Period="Q2 2025"),
]

ProjectTasks = [
    ProjectTask(Id=1, ProjectId=1, TaskName="Design", Status="Completed"),
    ProjectTask(Id=2, ProjectId=1, TaskName="Development", Status="In Progress"),
    ProjectTask(Id=3, ProjectId=2, TaskName="Testing", Status="Pending"),
    ProjectTask(Id=4, ProjectId=3, TaskName="Deployment", Status="In Progress"),
    ProjectTask(Id=5, ProjectId=4, TaskName="UAT", Status="Pending"),
]

ProjectTeams = [
    ProjectTeam(Id=1, ProjectId=1, MemberName="Alice Smith", Role="Lead"),
    ProjectTeam(Id=2, ProjectId=1, MemberName="Bob Johnson", Role="Member"),
    ProjectTeam(Id=3, ProjectId=2, MemberName="Charlie Brown", Role="Lead"),
    ProjectTeam(Id=4, ProjectId=3, MemberName="David Lee", Role="Lead"),
    ProjectTeam(Id=5, ProjectId=4, MemberName="Eva Green", Role="Member"),
]


# -----------------
# Timesheets
# -----------------
Timesheets = [
    Timesheet(Id=1, EmployeeId=101, Date=date.today(), HoursWorked=8),
    Timesheet(Id=2, EmployeeId=102, Date=date.today() - timedelta(days=1), HoursWorked=6.5),
    Timesheet(Id=3, EmployeeId=103, Date=date.today() - timedelta(days=2), HoursWorked=7),
    Timesheet(Id=4, EmployeeId=104, Date=date.today() - timedelta(days=3), HoursWorked=9),
    Timesheet(Id=5, EmployeeId=105, Date=date.today() - timedelta(days=4), HoursWorked=8.5),
    Timesheet(Id=6, EmployeeId=106, Date=date.today() - timedelta(days=5), HoursWorked=7.5),
    Timesheet(Id=7, EmployeeId=107, Date=date.today() - timedelta(days=6), HoursWorked=8),
    Timesheet(Id=8, EmployeeId=108, Date=date.today() - timedelta(days=7), HoursWorked=6),
    Timesheet(Id=9, EmployeeId=109, Date=date.today() - timedelta(days=8), HoursWorked=7.5),
    Timesheet(Id=10, EmployeeId=110, Date=date.today() - timedelta(days=9), HoursWorked=8),
]

TimesheetAdjustments = [
    TimesheetAdjustment(Id=1, TimesheetId=1, Reason="Correction"),
    TimesheetAdjustment(Id=2, TimesheetId=2, Reason="Overtime"),
    TimesheetAdjustment(Id=3, TimesheetId=3, Reason="Leave adjustment"),
    TimesheetAdjustment(Id=4, TimesheetId=4, Reason="Error fix"),
    TimesheetAdjustment(Id=5, TimesheetId=5, Reason="Holiday work"),
]

TimesheetAttachments = [
    TimesheetAttachment(Id=1, TimesheetId=1, FileName="timesheet1.pdf"),
    TimesheetAttachment(Id=2, TimesheetId=2, FileName="timesheet2.pdf"),
    TimesheetAttachment(Id=3, TimesheetId=3, FileName="timesheet3.pdf"),
    TimesheetAttachment(Id=4, TimesheetId=4, FileName="timesheet4.pdf"),
]

TimesheetAudits = [
    TimesheetAudit(Id=1, TimesheetId=1, Action="Submitted", Date=date.today() - timedelta(days=1)),
    TimesheetAudit(Id=2, TimesheetId=2, Action="Approved", Date=date.today() - timedelta(days=2)),
    TimesheetAudit(Id=3, TimesheetId=3, Action="Rejected", Date=date.today() - timedelta(days=3)),
    TimesheetAudit(Id=4, TimesheetId=4, Action="Submitted", Date=date.today() - timedelta(days=4)),
    TimesheetAudit(Id=5, TimesheetId=5, Action="Approved", Date=date.today() - timedelta(days=5)),
]

# -----------------
# People
# -----------------
People = [
    Person(Id=1, Name="Alice Smith", Email="alice@example.com"),
    Person(Id=2, Name="Bob Johnson", Email="bob@example.com"),
    Person(Id=3, Name="Charlie Brown", Email="charlie@example.com"),
    Person(Id=4, Name="David Lee", Email="david@example.com"),
    Person(Id=5, Name="Eva Green", Email="eva@example.com"),
    Person(Id=6, Name="Frank Miller", Email="frank@example.com"),
    Person(Id=7, Name="Grace Taylor", Email="grace@example.com"),
    Person(Id=8, Name="Henry Adams", Email="henry@example.com"),
    Person(Id=9, Name="Ivy Wilson", Email="ivy@example.com"),
    Person(Id=10, Name="Jack White", Email="jack@example.com"),
]

AccrualPlans = [
    AccrualPlan(Id=1, PersonId=1, PlanName="Vacation Plan"),
    AccrualPlan(Id=2, PersonId=1, PlanName="Sick Leave"),
    AccrualPlan(Id=3, PersonId=2, PlanName="Maternity Leave"),
    AccrualPlan(Id=4, PersonId=3, PlanName="Vacation Plan"),
    AccrualPlan(Id=5, PersonId=4, PlanName="Paternity Leave"),
]

Alternates = [
    Alternate(Id=1, PersonId=1, Name="Manager A"),
    Alternate(Id=2, PersonId=2, Name="Manager B"),
    Alternate(Id=3, PersonId=3, Name="Manager C"),
    Alternate(Id=4, PersonId=4, Name="Manager D"),
]

ApprovalGroups = [
    ApprovalGroup(Id=1, PersonId=1, Type="Approver"),
    ApprovalGroup(Id=2, PersonId=1, Type="ExpenseReport"),
    ApprovalGroup(Id=3, PersonId=2, Type="Timesheet"),
    ApprovalGroup(Id=4, PersonId=3, Type="Leave"),
]

PersonAttachments = [
    PersonAttachment(Id=1, PersonId=1, FileName="resume.pdf"),
    PersonAttachment(Id=2, PersonId=2, FileName="id_card.pdf"),
    PersonAttachment(Id=3, PersonId=3, FileName="offer_letter.pdf"),
]

AvailableAlternates = [
    Alternate(Id=5, PersonId=1, Name="Alt A"),
    Alternate(Id=6, PersonId=2, Name="Alt B"),
    Alternate(Id=7, PersonId=3, Name="Alt C"),
]

BenefitsValues = [
    BenefitsValue(Id=1, PersonId=1, PackageName="Standard Benefits"),
    BenefitsValue(Id=2, PersonId=2, PackageName="Premium Benefits"),
    BenefitsValue(Id=3, PersonId=3, PackageName="Executive Benefits"),
]

Rates = [
    Rate(Id=1, PersonId=1, Amount=100.0),
    Rate(Id=2, PersonId=2, Amount=120.0),
    Rate(Id=3, PersonId=3, Amount=95.0),
    Rate(Id=4, PersonId=4, Amount=110.0),
]

Skills = [
    Skill(Id=1, PersonId=1, SkillName="Python"),
    Skill(Id=2, PersonId=1, SkillName="FastAPI"),
    Skill(Id=3, PersonId=2, SkillName="React"),
    Skill(Id=4, PersonId=3, SkillName="Docker"),
    Skill(Id=5, PersonId=4, SkillName="Kubernetes"),
]

PeopleSummaries = [
    PersonSummary(Id=1, Name="Alice Smith"),
    PersonSummary(Id=2, Name="Bob Johnson"),
    PersonSummary(Id=3, Name="Charlie Brown"),
    PersonSummary(Id=4, Name="David Lee"),
    PersonSummary(Id=5, Name="Eva Green"),
]

