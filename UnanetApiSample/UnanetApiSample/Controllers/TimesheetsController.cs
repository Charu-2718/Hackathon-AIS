using Microsoft.AspNetCore.Mvc;
using UnanetApiSample.Data;
using UnanetApiSample.Models;
using System.Linq;

namespace UnanetApiSample.Controllers
{
    [ApiController]
    [Route("rest/time")]
    public class TimesheetsController : ControllerBase
    {
        // GET /rest/time
        [HttpGet]
        public IActionResult GetTimesheets()
        {
            return Ok(DummyData.Timesheets);
        }

        // GET /rest/time/{id}
        [HttpGet("{id}")]
        public IActionResult GetTimesheet(int id)
        {
            var timesheet = DummyData.Timesheets.FirstOrDefault(t => t.Id == id);
            if (timesheet == null)
                return NotFound(new { error = "Timesheet not found" });

            return Ok(timesheet);
        }

        // GET /rest/time/{id}/adjustments
        [HttpGet("{id}/adjustments")]
        public IActionResult GetTimesheetAdjustments(int id)
        {
            var adjustments = DummyData.TimesheetAdjustments.Where(a => a.TimesheetId == id).ToList();
            return Ok(adjustments);
        }

        // GET /rest/time/{id}/attachment/{attachmentId}
        [HttpGet("{id}/attachment/{attachmentId}")]
        public IActionResult GetTimesheetAttachment(int id, int attachmentId)
        {
            var attachment = DummyData.TimesheetAttachments.FirstOrDefault(a => a.Id == attachmentId && a.TimesheetId == id);
            if (attachment == null)
                return NotFound(new { error = "Timesheet attachment not found" });

            return Ok(attachment);
        }

        // GET /rest/time/{id}/attachments
        [HttpGet("{id}/attachments")]
        public IActionResult GetTimesheetAttachments(int id)
        {
            var attachments = DummyData.TimesheetAttachments.Where(a => a.TimesheetId == id).ToList();
            return Ok(attachments);
        }

        // GET /rest/time/{id}/audit
        [HttpGet("{id}/audit")]
        public IActionResult GetTimesheetAudit(int id)
        {
            var audit = DummyData.TimesheetAudits.Where(a => a.TimesheetId == id).ToList();
            return Ok(audit);
        }

        // GET /rest/time/{id}/auto-fill
        [HttpGet("{id}/auto-fill")]
        public IActionResult GetAutoFill(int id)
        {
            return Ok(new[] { "Auto Fill Row A", "Auto Fill Row B" });
        }

        // GET /rest/time/{id}/auto-fill/deleted
        [HttpGet("{id}/auto-fill/deleted")]
        public IActionResult GetDeletedAutoFill(int id)
        {
            return Ok(new[] { "Deleted Auto Fill Row A", "Deleted Auto Fill Row B" });
        }

        // GET /rest/time/{id}/history
        [HttpGet("{id}/history")]
        public IActionResult GetTimesheetHistory(int id)
        {
            return Ok(new[] { "History A", "History B" });
        }

        // GET /rest/time/{id}/items/audit
        [HttpGet("{id}/items/audit")]
        public IActionResult GetItemsAudit(int id)
        {
            return Ok(new[] { "Item Audit A", "Item Audit B" });
        }

        // GET /rest/time/{id}/offline
        [HttpGet("{id}/offline")]
        public IActionResult GetOfflineTimesheet(int id)
        {
            return Ok(new { OfflineData = "Offline timesheet data content" });
        }

        // GET /rest/time/{id}/project-types
        [HttpGet("{id}/project-types")]
        public IActionResult GetTimesheetProjectTypes(int id)
        {
            return Ok(DummyData.ExpenseProjectTypes);
        }

        // GET /rest/time/{id}/projects
        [HttpGet("{id}/projects")]
        public IActionResult GetTimesheetProjects(int id)
        {
            return Ok(DummyData.Projects);
        }

        // GET /rest/time/{id}/projects/{projectId}/labor-categories
        [HttpGet("{id}/projects/{projectId}/labor-categories")]
        public IActionResult GetProjectLaborCategories(int id, int projectId)
        {
            return Ok(new[] { "Labor Category A", "Labor Category B" });
        }

        // GET /rest/time/{id}/projects/{projectId}/locations
        [HttpGet("{id}/projects/{projectId}/locations")]
        public IActionResult GetProjectLocations(int id, int projectId)
        {
            return Ok(new[] { "Location A", "Location B" });
        }

        // GET /rest/time/{id}/tasks/{taskId}/labor-categories
        [HttpGet("{id}/tasks/{taskId}/labor-categories")]
        public IActionResult GetTaskLaborCategories(int id, int taskId)
        {
            return Ok(new[] { "Labor Category A", "Labor Category B" });
        }

        // GET /rest/time/{id}/tasks/{taskId}/locations
        [HttpGet("{id}/tasks/{taskId}/locations")]
        public IActionResult GetTaskLocations(int id, int taskId)
        {
            return Ok(new[] { "Location A", "Location B" });
        }

        // GET /rest/time/{id}/validate
        [HttpGet("{id}/validate")]
        public IActionResult ValidateTimesheet(int id)
        {
            return Ok(new { valid = true });
        }
    }
}
