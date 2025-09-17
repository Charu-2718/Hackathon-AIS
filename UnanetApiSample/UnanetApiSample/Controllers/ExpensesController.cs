using Microsoft.AspNetCore.Mvc;
using UnanetApiSample.Data;
using UnanetApiSample.Models;
using System.Linq;

namespace UnanetApiSample.Controllers
{
    [ApiController]
    [Route("rest/expenses")]
    public class ExpensesController : ControllerBase
    {
        // GET /rest/expenses/{id}
        [HttpGet("{id}")]
        public IActionResult GetExpense(int id)
        {
            var expense = DummyData.Expenses.FirstOrDefault(e => e.Id == id);
            if (expense == null)
                return NotFound(new { error = "Expense not found" });

            return Ok(expense);
        }

        // GET /rest/expenses/{id}/attachments
        [HttpGet("{id}/attachments")]
        public IActionResult GetExpenseAttachments(int id)
        {
            var attachments = DummyData.ExpenseAttachments.Where(a => a.ExpenseId == id).ToList();
            return Ok(attachments);
        }

        // GET /rest/expenses/{id}/attachments/{attachmentId}
        [HttpGet("{id}/attachments/{attachmentId}")]
        public IActionResult GetExpenseAttachment(int id, int attachmentId)
        {
            var attachment = DummyData.ExpenseAttachments.FirstOrDefault(a => a.Id == attachmentId && a.ExpenseId == id);
            if (attachment == null)
                return NotFound(new { error = "Attachment not found" });

            return Ok(attachment);
        }

        // GET /rest/expenses/{id}/details/{detailId}
        [HttpGet("{id}/details/{detailId}")]
        public IActionResult GetExpenseDetail(int id, int detailId)
        {
            var detail = DummyData.ExpenseDetails.FirstOrDefault(d => d.Id == detailId && d.ExpenseId == id);
            if (detail == null)
                return NotFound(new { error = "Expense detail not found" });

            return Ok(detail);
        }

        // GET /rest/expenses/{id}/expense-types
        [HttpGet("{id}/expense-types")]
        public IActionResult GetExpenseTypes(int id)
        {
            return Ok(DummyData.ExpenseTypes);
        }

        // GET /rest/expenses/{id}/history
        [HttpGet("{id}/history")]
        public IActionResult GetExpenseHistory(int id)
        {
            var history = DummyData.ExpenseHistories.Where(h => h.ExpenseId == id).ToList();
            return Ok(history);
        }

        // GET /rest/expenses/{id}/meal-caps
        [HttpGet("{id}/meal-caps")]
        public IActionResult GetMealCaps(int id)
        {
            var cap = DummyData.MealCaps.FirstOrDefault(m => m.ExpenseId == id);
            if (cap == null)
                return NotFound(new { error = "Meal cap not found" });

            return Ok(cap);
        }

        // GET /rest/expenses/{id}/payment-methods
        [HttpGet("{id}/payment-methods")]
        public IActionResult GetPaymentMethods(int id)
        {
            var methods = DummyData.PaymentMethods.Where(m => m.ExpenseId == id).ToList();
            return Ok(methods);
        }

        // GET /rest/expenses/{id}/project-types
        [HttpGet("{id}/project-types")]
        public IActionResult GetProjectTypes(int id)
        {
            return Ok(DummyData.ExpenseProjectTypes);
        }

        // GET /rest/expenses/{id}/projects
        [HttpGet("{id}/projects")]
        public IActionResult GetExpenseProjects(int id)
        {
            return Ok(DummyData.Projects);
        }

        // GET /rest/expenses/{id}/validate
        [HttpGet("{id}/validate")]
        public IActionResult ValidateExpense(int id)
        {
            return Ok(new { valid = true });
        }

        // GET /rest/expenses/projects
        [HttpGet("projects")]
        public IActionResult GetProjectsByOwner()
        {
            return Ok(DummyData.Projects);
        }

        // GET /rest/expenses/vat-locations
        [HttpGet("vat-locations")]
        public IActionResult GetVatLocations()
        {
            return Ok(DummyData.VatLocations);
        }

        // GET /rest/expenses/vat-locations/{id}
        [HttpGet("vat-locations/{id}")]
        public IActionResult GetVatLocation(int id)
        {
            var location = DummyData.VatLocations.FirstOrDefault(v => v.Id == id);
            if (location == null)
                return NotFound(new { error = "VAT location not found" });

            return Ok(location);
        }
    }
}
