using UnanetApiSample.Models;

namespace UnanetApiSample.Data
{
    public static class DummyData
    {
        // Contracts
        public static List<Contract> Contracts = new()
        {
            new Contract { Id = 1, Name = "Contract A", Status = "Active" },
            new Contract { Id = 2, Name = "Contract B", Status = "Closed" }
        };

        public static List<ContractClause> ContractClauses = new()
        {
            new ContractClause { Id = 1, ContractId = 1, Text = "Clause A1" },
            new ContractClause { Id = 2, ContractId = 1, Text = "Clause A2" },
            new ContractClause { Id = 3, ContractId = 2, Text = "Clause B1" }
        };

        public static List<ContractMod> ContractMods = new()
        {
            new ContractMod { ModNumber = 1, ContractId = 1, Description = "Mod 1 for Contract A" },
            new ContractMod { ModNumber = 2, ContractId = 2, Description = "Mod 1 for Contract B" }
        };

        public static List<WageDetermination> WageDeterminations = new()
        {
            new WageDetermination { Id = 1, ContractId = 1, Name = "WD 1" },
            new WageDetermination { Id = 2, ContractId = 2, Name = "WD 2" }
        };

        public static List<Models.Attachment> AdditionalItemTypes = new()
        {
            new Models.Attachment { Id = 1, Name = "Item Type A" },
            new Models.Attachment { Id = 2, Name = "Item Type B" }
        };

        public static List<BillingAnalyst> BillingAnalysts = new()
        {
            new BillingAnalyst { Id = 1, Name = "Analyst A" },
            new BillingAnalyst { Id = 2, Name = "Analyst B" }
        };

        public static List<ContractManager> ContractManagers = new()
        {
            new ContractManager { Id = 1, Name = "Manager A" },
            new ContractManager { Id = 2, Name = "Manager B" }
        };

        public static List<OwningOrganization> OwningOrganizations = new()
        {
            new OwningOrganization { Id = 1, Name = "Org A" },
            new OwningOrganization { Id = 2, Name = "Org B" }
        };

        public static List<MasterContract> MasterContracts = new()
        {
            new MasterContract { Id = 1, OwningOrgId = 1, Name = "Master Contract A" },
            new MasterContract { Id = 2, OwningOrgId = 2, Name = "Master Contract B" }
        };

        public static List<Provision> Provisions = new()
        {
            new Provision { Id = 1, Name = "Provision A" },
            new Provision { Id = 2, Name = "Provision B" }
        };

        public static List<ContractStatus> ContractStatuses = new()
        {
            new ContractStatus { Id = 1, Name = "Active" },
            new ContractStatus { Id = 2, Name = "Closed" }
        };

        public static List<ContractType> ContractTypes = new()
        {
            new ContractType { Id = 1, Name = "Fixed Price" },
            new ContractType { Id = 2, Name = "Time & Materials" }
        };

        // Expenses
        public static List<Expense> Expenses = new()
        {
            new Expense { Id = 1, ProjectId = 1, Amount = 150.75m, Description = "Office supplies" },
            new Expense { Id = 2, ProjectId = 2, Amount = 300.00m, Description = "Client entertainment" }
        };

        public static List<ExpenseAttachment> ExpenseAttachments = new()
        {
            new ExpenseAttachment { Id = 1, ExpenseId = 1, FileName = "receipt1.pdf" },
            new ExpenseAttachment { Id = 2, ExpenseId = 2, FileName = "receipt2.pdf" }
        };

        public static List<ExpenseDetail> ExpenseDetails = new()
        {
            new ExpenseDetail { Id = 1, ExpenseId = 1, Description = "Detail A" },
            new ExpenseDetail { Id = 2, ExpenseId = 2, Description = "Detail B" }
        };

        public static List<ExpenseType> ExpenseTypes = new()
        {
            new ExpenseType { Id = 1, Name = "Travel" },
            new ExpenseType { Id = 2, Name = "Office" }
        };

        public static List<ExpenseHistory> ExpenseHistories = new()
        {
            new ExpenseHistory { Id = 1, ExpenseId = 1, Status = "Pending", Date = DateTime.Today.AddDays(-2) },
            new ExpenseHistory { Id = 2, ExpenseId = 1, Status = "Approved", Date = DateTime.Today.AddDays(-1) }
        };

        public static List<MealCap> MealCaps = new()
        {
            new MealCap { ExpenseId = 1, MaxAmount = 50.00m }
        };

        public static List<PaymentMethod> PaymentMethods = new()
        {
            new PaymentMethod { ExpenseId = 1, Method = "Credit Card" },
            new PaymentMethod { ExpenseId = 2, Method = "Bank Transfer" }
        };

        public static List<ProjectType> ExpenseProjectTypes = new()
        {
            new ProjectType { Id = 1, Name = "Internal" },
            new ProjectType { Id = 2, Name = "Client" }
        };

        public static List<VatLocation> VatLocations = new()
        {
            new VatLocation { Id = 1, Name = "India" },
            new VatLocation { Id = 2, Name = "USA" }
        };

        // Projects
        public static List<Project> Projects = new()
        {
            new Project { Id = 1, Name = "Project Alpha", Client = "Client X" },
            new Project { Id = 2, Name = "Project Beta", Client = "Client Y" }
        };

        public static List<ProjectAccount> ProjectAccounts = new()
        {
            new ProjectAccount { Id = 1, ProjectId = 1, Name = "Account A" },
            new ProjectAccount { Id = 2, ProjectId = 2, Name = "Account B" }
        };

        public static List<ProjectAlert> ProjectAlerts = new()
        {
            new ProjectAlert { Id = 1, ProjectId = 1, Message = "Alert 1" },
            new ProjectAlert { Id = 2, ProjectId = 2, Message = "Alert 2" }
        };

        // Timesheets
        public static List<Timesheet> Timesheets = new()
        {
            new Timesheet { Id = 1, EmployeeId = 101, Date = DateTime.Today, HoursWorked = 8 },
            new Timesheet { Id = 2, EmployeeId = 102, Date = DateTime.Today.AddDays(-1), HoursWorked = 6.5 }
        };

        public static List<TimesheetAdjustment> TimesheetAdjustments = new()
        {
            new TimesheetAdjustment { Id = 1, TimesheetId = 1, Reason = "Correction" }
        };

        public static List<TimesheetAttachment> TimesheetAttachments = new()
        {
            new TimesheetAttachment { Id = 1, TimesheetId = 1, FileName = "timesheet1.pdf" }
        };

        public static List<TimesheetAudit> TimesheetAudits = new()
        {
            new TimesheetAudit { Id = 1, TimesheetId = 1, Action = "Submitted", Date = DateTime.Today.AddDays(-1) }
        };
    }
}
