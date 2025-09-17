using Microsoft.AspNetCore.Mvc;
using UnanetApiSample.Data;
using UnanetApiSample.Models;
using System.Linq;

namespace UnanetApiSample.Controllers
{
    [ApiController]
    [Route("rest/projects")]
    public class ProjectsController : ControllerBase
    {
        // GET /rest/projects/{id}
        [HttpGet("{id}")]
        public IActionResult GetProject(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var project = DummyData.Projects.FirstOrDefault(p => p.Id == id);
            if (project == null)
                return NotFound(new { error = "Project not found" });

            return Ok(project);
        }

        // GET /rest/projects/{id}/accounts
        [HttpGet("{id}/accounts")]
        public IActionResult GetProjectAccounts(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var accounts = DummyData.ProjectAccounts.Where(a => a.ProjectId == id).ToList();
            return Ok(accounts);
        }

        // Example of multiple admin endpoints, using dummy data
        [HttpGet("{id}/admin/billing-managers/alternate")]
        public IActionResult GetAlternateBillingManagers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Manager A", "Alternate Manager B" });

        [HttpGet("{id}/admin/billing-managers/primary")]
        public IActionResult GetPrimaryBillingManager(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Manager" });

        [HttpGet("{id}/admin/billing-viewers/alternate")]
        public IActionResult GetAlternateBillingViewers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Viewer A", "Alternate Viewer B" });

        [HttpGet("{id}/admin/billing-viewers/primary")]
        public IActionResult GetPrimaryBillingViewer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Viewer" });

        [HttpGet("{id}/admin/customers/alternates")]
        public IActionResult GetAlternateCustomers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Customer A", "Alternate Customer B" });

        [HttpGet("{id}/admin/customers/primary")]
        public IActionResult GetPrimaryCustomer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Customer" });

        [HttpGet("{id}/admin/document-viewers/alternate")]
        public IActionResult GetAlternateDocumentViewers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Doc Viewer A", "Alternate Doc Viewer B" });

        [HttpGet("{id}/admin/document-viewers/primary")]
        public IActionResult GetPrimaryDocumentViewer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Document Viewer" });

        [HttpGet("{id}/admin/leads/alternate")]
        public IActionResult GetAlternateLeads(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Lead A", "Alternate Lead B" });

        [HttpGet("{id}/admin/leads/primary")]
        public IActionResult GetPrimaryLead(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Lead" });

        [HttpGet("{id}/admin/managers/alternate")]
        public IActionResult GetAlternateManagers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Manager A", "Alternate Manager B" });

        [HttpGet("{id}/admin/managers/primary")]
        public IActionResult GetPrimaryManager(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Manager" });

        [HttpGet("{id}/admin/po-viewers/alternate")]
        public IActionResult GetAlternatePoViewers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate PO Viewer A", "Alternate PO Viewer B" });

        [HttpGet("{id}/admin/po-viewers/primary")]
        public IActionResult GetPrimaryPoViewer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary PO Viewer" });

        [HttpGet("{id}/admin/pr-viewers/alternate")]
        public IActionResult GetAlternatePrViewers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate PR Viewer A", "Alternate PR Viewer B" });

        [HttpGet("{id}/admin/pr-viewers/primary")]
        public IActionResult GetPrimaryPrViewer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary PR Viewer" });

        [HttpGet("{id}/admin/project-approvers/alternates")]
        public IActionResult GetAlternateProjectApprovers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Approver A", "Alternate Approver B" });

        [HttpGet("{id}/admin/project-approvers/primary")]
        public IActionResult GetPrimaryProjectApprover(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Approver" });

        [HttpGet("{id}/admin/resource-assigners/alternate")]
        public IActionResult GetAlternateResourceAssigners(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Assigner A", "Alternate Assigner B" });

        [HttpGet("{id}/admin/resource-assigners/primary")]
        public IActionResult GetPrimaryResourceAssigner(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Assigner" });

        [HttpGet("{id}/admin/resource-planners/alternate")]
        public IActionResult GetAlternateResourcePlanners(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Planner A", "Alternate Planner B" });

        [HttpGet("{id}/admin/resource-planners/primary")]
        public IActionResult GetPrimaryResourcePlanner(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Planner" });

        [HttpGet("{id}/admin/resource-requestors/alternate")]
        public IActionResult GetAlternateResourceRequestors(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Requestor A", "Alternate Requestor B" });

        [HttpGet("{id}/admin/resource-requestors/primary")]
        public IActionResult GetPrimaryResourceRequestor(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Requestor" });

        [HttpGet("{id}/admin/viewers/alternate")]
        public IActionResult GetAlternateViewers(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alternate Viewer A", "Alternate Viewer B" });

        [HttpGet("{id}/admin/viewers/primary")]
        public IActionResult GetPrimaryViewer(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Name = "Primary Viewer" });

        [HttpGet("{id}/alert-config")]
        public IActionResult GetAlertConfig(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Config = "Default Alert Config" });

        [HttpGet("{id}/alerts")]
        public IActionResult GetAlerts(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(DummyData.ProjectAlerts.Where(a => a.ProjectId == id).ToList());

        [HttpGet("{id}/budget-history")]
        public IActionResult GetBudgetHistory(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Budget history A", "Budget history B" });

        [HttpGet("{id}/budget-snapshots/{budgetSnapshotId}")]
        public IActionResult GetBudgetSnapshot(int id, int budgetSnapshotId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { SnapshotId = budgetSnapshotId, Description = "Snapshot Description" });

        [HttpGet("{id}/cost-rates")]
        public IActionResult GetCostRates(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Cost Rate A", "Cost Rate B" });

        [HttpGet("{id}/expense-budgets/{expBudgetId}")]
        public IActionResult GetExpenseBudget(int id, int expBudgetId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { BudgetId = expBudgetId, Amount = 1000 });

        [HttpGet("{id}/expense-plans/{expPlanId}")]
        public IActionResult GetExpensePlan(int id, int expPlanId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { PlanId = expPlanId, Name = "Expense Plan Name" });

        [HttpGet("{id}/expense-types")]
        public IActionResult GetExpenseTypes(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(DummyData.ExpenseTypes);

        [HttpGet("{id}/expense-types/{expenseTypeId}")]
        public IActionResult GetExpenseType(int id, int expenseTypeId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(DummyData.ExpenseTypes.FirstOrDefault(e => e.Id == expenseTypeId));

        [HttpGet("{id}/fees")]
        public IActionResult GetFees(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Fee A", "Fee B" });

        [HttpGet("{id}/fees/{feeMethodId}")]
        public IActionResult GetFee(int id, int feeMethodId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { FeeMethodId = feeMethodId, Description = "Fee Method Description" });

        [HttpGet("{id}/fixed-price-items")]
        public IActionResult GetFixedPriceItems(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Fixed Price Item A", "Fixed Price Item B" });

        [HttpGet("{id}/fixed-price-items/{fixedPriceItemId}")]
        public IActionResult GetFixedPriceItem(int id, int fixedPriceItemId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { FixedPriceItemId = fixedPriceItemId, Description = "Fixed Price Item Description" });

        [HttpGet("{id}/invoice-setup")]
        public IActionResult GetInvoiceSetup(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { Setup = "Invoice Setup Data" });

        [HttpGet("{id}/invoice-setup/valid-addresses")]
        public IActionResult GetValidAddresses(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Address A", "Address B" });

        [HttpGet("{id}/invoice-setup/valid-contacts")]
        public IActionResult GetValidContacts(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Contact A", "Contact B" });

        [HttpGet("{id}/items")]
        public IActionResult GetItems(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Item A", "Item B" });

        [HttpGet("{id}/items/{itemId}")]
        public IActionResult GetItem(int id, int itemId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { ItemId = itemId, Name = "Item Name" });

        [HttpGet("{id}/items/{itemId}/uoms")]
        public IActionResult GetItemUoms(int id, int itemId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "UOM A", "UOM B" });

        [HttpGet("{id}/labor-categories")]
        public IActionResult GetLaborCategories(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Labor Category A", "Labor Category B" });

        [HttpGet("{id}/labor-categories/{laborCatAssignmentId}/rates")]
        public IActionResult GetLaborCategoryRates(int id, int laborCatAssignmentId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Rate A", "Rate B" });

        [HttpGet("{id}/locations")]
        public IActionResult GetLocations(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Location A", "Location B" });

        [HttpGet("{id}/notes")]
        public IActionResult GetNotes(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Note A", "Note B" });

        [HttpGet("{id}/notes/{noteId}")]
        public IActionResult GetNote(int id, int noteId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { NoteId = noteId, Content = "Note Content" });

        [HttpGet("{id}/notes/{noteId}/attachments")]
        public IActionResult GetNoteAttachments(int id, int noteId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Attachment A", "Attachment B" });

        [HttpGet("{id}/notes/{noteId}/attachments/{noteAttachmentId}")]
        public IActionResult GetNoteAttachment(int id, int noteId, int noteAttachmentId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { AttachmentId = noteAttachmentId, FileName = "Attachment.pdf" });

        [HttpGet("{id}/notes/{noteId}/audit")]
        public IActionResult GetNoteAudit(int id, int noteId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Audit A", "Audit B" });

        [HttpGet("{id}/notes/{noteId}/comments")]
        public IActionResult GetNoteComments(int id, int noteId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Comment A", "Comment B" });

        [HttpGet("{id}/notes/{noteId}/comments/{commentId}/attachments")]
        public IActionResult GetNoteCommentAttachments(int id, int noteId, int commentId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Comment Attachment A", "Comment Attachment B" });

        [HttpGet("{id}/notes/{noteId}/comments/{commentId}/attachments/{attachmentId}")]
        public IActionResult GetNoteCommentAttachment(int id, int noteId, int commentId, int attachmentId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { AttachmentId = attachmentId, FileName = "CommentAttachment.pdf" });

        [HttpGet("{id}/notes/{noteId}/comments/{noteCommentId}")]
        public IActionResult GetNoteComment(int id, int noteId, int noteCommentId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { CommentId = noteCommentId, Content = "Comment Content" });

        [HttpGet("{id}/organization-assignments")]
        public IActionResult GetOrganizationAssignments(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Assignment A", "Assignment B" });

        [HttpGet("{id}/pay-codes")]
        public IActionResult GetPayCodes(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Pay Code A", "Pay Code B" });

        [HttpGet("{id}/people-assignments/{assignId}")]
        public IActionResult GetPeopleAssignment(int id, int assignId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { AssignmentId = assignId, Details = "Assignment Details" });

        [HttpGet("{id}/people-assignments/defaults/person/{personId}/{date}")]
        public IActionResult GetPersonAssignmentDefaults(int id, int personId, string date, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { PersonId = personId, Date = date, DefaultAssignment = "Default Assignment Data" });

        [HttpGet("{id}/people-plans/{planId}")]
        public IActionResult GetPeoplePlan(int id, int planId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { PlanId = planId, Name = "People Plan" });

        [HttpGet("{id}/plan-sets")]
        public IActionResult GetPlanSets(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Plan Set A", "Plan Set B" });

        [HttpGet("{id}/plan-sets/{planSetId}/history")]
        public IActionResult GetPlanSetHistory(int id, int planSetId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "History A", "History B" });

        [HttpGet("{id}/pre-billed-labor")]
        public IActionResult GetPreBilledLabor(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Labor A", "Labor B" });

        [HttpGet("{id}/pre-billed-labor/{preBilledLaborId}")]
        public IActionResult GetPreBilledLaborById(int id, int preBilledLaborId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { LaborId = preBilledLaborId, Name = "Pre-billed Labor" });

        [HttpGet("{id}/tasks")]
        public IActionResult GetTasks(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Task A", "Task B" });

        [HttpGet("{id}/tasks/{taskId}")]
        public IActionResult GetTask(int id, int taskId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { TaskId = taskId, Name = "Task Name" });

        [HttpGet("{id}/tasks/{taskId}/accounts")]
        public IActionResult GetTaskAccounts(int id, int taskId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Account A", "Account B" });

        [HttpGet("{id}/tasks/{taskId}/budget-history")]
        public IActionResult GetTaskBudgetHistory(int id, int taskId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Budget History A", "Budget History B" });

        [HttpGet("{id}/tasks/{taskId}/budget-snapshots/{budgetSnapshotId}")]
        public IActionResult GetTaskBudgetSnapshot(int id, int taskId, int budgetSnapshotId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new { SnapshotId = budgetSnapshotId, Description = "Snapshot Description" });

        [HttpGet("{id}/tasks/{taskId}/cost-rates")]
        public IActionResult GetTaskCostRates(int id, int taskId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Cost Rate A", "Cost Rate B" });

        [HttpGet("{id}/tasks/{taskId}/predecessors")]
        public IActionResult GetTaskPredecessors(int id, int taskId, [FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Predecessor A", "Predecessor B" });

        [HttpGet("account-categories")]
        public IActionResult GetAccountCategories([FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Account Category A", "Account Category B" });

        [HttpGet("alerts")]
        public IActionResult GetAlertsGlobal([FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Alert A", "Alert B" });

        [HttpGet("invoice-setup/approval-groups")]
        public IActionResult GetApprovalGroups([FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Approval Group A", "Approval Group B" });

        [HttpGet("tasks/account-categories")]
        public IActionResult GetTaskAccountCategories([FromHeader(Name = "X-Una-App")] string? appHeader)
            => Ok(new[] { "Task Account Category A", "Task Account Category B" });
    }
}
