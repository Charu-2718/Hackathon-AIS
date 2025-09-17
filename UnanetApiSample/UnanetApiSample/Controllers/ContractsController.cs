using Microsoft.AspNetCore.Mvc;
using UnanetApiSample.Data;
using UnanetApiSample.Models;
using System.Linq;

namespace UnanetApiSample.Controllers
{
    [ApiController]
    [Route("rest/contracts")]
    public class ContractsController : ControllerBase
    {
        // GET /rest/contracts
        [HttpGet]
        public IActionResult GetContracts([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.Contracts);
        }

        // GET /rest/contracts/{id}
        [HttpGet("{id}")]
        public IActionResult GetContract(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var contract = DummyData.Contracts.FirstOrDefault(c => c.Id == id);
            if (contract == null)
                return NotFound(new { error = "Contract not found" });

            return Ok(contract);
        }

        // GET /rest/contracts/{id}/contract-clauses
        [HttpGet("{id}/contract-clauses")]
        public IActionResult GetContractClauses(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var clauses = DummyData.ContractClauses.Where(cc => cc.ContractId == id).ToList();
            return Ok(clauses);
        }

        // GET /rest/contracts/{id}/contract-clauses/{clauseId}
        [HttpGet("{id}/contract-clauses/{clauseId}")]
        public IActionResult GetContractClause(int id, int clauseId, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var clause = DummyData.ContractClauses.FirstOrDefault(cc => cc.Id == clauseId && cc.ContractId == id);
            if (clause == null)
                return NotFound(new { error = "Contract clause not found" });

            return Ok(clause);
        }

        // GET /rest/contracts/{id}/mods
        [HttpGet("{id}/mods")]
        public IActionResult GetContractMods(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var mods = DummyData.ContractMods.Where(m => m.ContractId == id).ToList();
            return Ok(mods);
        }

        // GET /rest/contracts/{id}/mods/{modNumber}
        [HttpGet("{id}/mods/{modNumber}")]
        public IActionResult GetContractMod(int id, int modNumber, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var mod = DummyData.ContractMods.FirstOrDefault(m => m.ContractId == id && m.ModNumber == modNumber);
            if (mod == null)
                return NotFound(new { error = "Contract mod not found" });

            return Ok(mod);
        }

        // GET /rest/contracts/{id}/projects
        [HttpGet("{id}/projects")]
        public IActionResult GetContractProjects(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            // This is dummy data, assuming all projects relate to all contracts
            return Ok(DummyData.Projects);
        }

        // GET /rest/contracts/{id}/projects/available/expense-types
        [HttpGet("{id}/projects/available/expense-types")]
        public IActionResult GetAvailableExpenseTypes(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.ExpenseTypes);
        }

        // GET /rest/contracts/{id}/projects/available/labor-categories
        [HttpGet("{id}/projects/available/labor-categories")]
        public IActionResult GetAvailableLaborCategories(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(new[] { "Labor Category A", "Labor Category B" });
        }

        // GET /rest/contracts/{id}/projects/available/tasks
        [HttpGet("{id}/projects/available/tasks")]
        public IActionResult GetAvailableTasks(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(new[] { "Task A", "Task B" });
        }

        // GET /rest/contracts/{id}/wage-determinations
        [HttpGet("{id}/wage-determinations")]
        public IActionResult GetWageDeterminations(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var wageDets = DummyData.WageDeterminations.Where(wd => wd.ContractId == id).ToList();
            return Ok(wageDets);
        }

        // GET /rest/contracts/{id}/wage-determinations/{wageDeterminationId}
        [HttpGet("{id}/wage-determinations/{wageDeterminationId}")]
        public IActionResult GetWageDetermination(int id, int wageDeterminationId, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var wd = DummyData.WageDeterminations.FirstOrDefault(w => w.Id == wageDeterminationId && w.ContractId == id);
            if (wd == null)
                return NotFound(new { error = "Wage determination not found" });

            return Ok(wd);
        }

        // GET /rest/contracts/additional-item-types
        [HttpGet("additional-item-types")]
        public IActionResult GetAdditionalItemTypes([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.AdditionalItemTypes);
        }

        // GET /rest/contracts/billing-analysts
        [HttpGet("billing-analysts")]
        public IActionResult GetBillingAnalysts([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.BillingAnalysts);
        }

        // GET /rest/contracts/contract-clauses
        [HttpGet("contract-clauses")]
        public IActionResult GetAllContractClauses([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.ContractClauses);
        }

        // GET /rest/contracts/contract-clauses/{id}
        [HttpGet("contract-clauses/{id}")]
        public IActionResult GetContractClauseById(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var clause = DummyData.ContractClauses.FirstOrDefault(c => c.Id == id);
            if (clause == null)
                return NotFound(new { error = "Contract clause not found" });

            return Ok(clause);
        }

        // GET /rest/contracts/contract-clauses/agencies
        [HttpGet("contract-clauses/agencies")]
        public IActionResult GetContractClauseAgencies([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(new[] { "Agency A", "Agency B" });
        }

        // GET /rest/contracts/contract-clauses/agencies/{id}
        [HttpGet("contract-clauses/agencies/{id}")]
        public IActionResult GetContractClauseAgency(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(new { Id = id, Name = "Agency " + id });
        }

        // GET /rest/contracts/contract-clauses/import/definition
        [HttpGet("contract-clauses/import/definition")]
        public IActionResult GetImportFieldDefinition([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(new { Fields = new[] { "Field1", "Field2" } });
        }

        // GET /rest/contracts/contract-managers
        [HttpGet("contract-managers")]
        public IActionResult GetContractManagers([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.ContractManagers);
        }

        // GET /rest/contracts/owning-organizations
        [HttpGet("owning-organizations")]
        public IActionResult GetOwningOrganizations([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.OwningOrganizations);
        }

        // GET /rest/contracts/owning-organizations/{owningOrgId}/master-contracts
        [HttpGet("owning-organizations/{owningOrgId}/master-contracts")]
        public IActionResult GetMasterContracts(int owningOrgId, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var masters = DummyData.MasterContracts.Where(m => m.OwningOrgId == owningOrgId).ToList();
            return Ok(masters);
        }

        // GET /rest/contracts/provisions
        [HttpGet("provisions")]
        public IActionResult GetProvisions([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.Provisions);
        }

        // GET /rest/contracts/statuses
        [HttpGet("statuses")]
        public IActionResult GetStatuses([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.ContractStatuses);
        }

        // GET /rest/contracts/statuses/{id}
        [HttpGet("statuses/{id}")]
        public IActionResult GetStatusById(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var status = DummyData.ContractStatuses.FirstOrDefault(s => s.Id == id);
            if (status == null)
                return NotFound(new { error = "Status not found" });

            return Ok(status);
        }

        // GET /rest/contracts/types
        [HttpGet("types")]
        public IActionResult GetTypes([FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            return Ok(DummyData.ContractTypes);
        }

        // GET /rest/contracts/types/{id}
        [HttpGet("types/{id}")]
        public IActionResult GetTypeById(int id, [FromHeader(Name = "X-Una-App")] string? appHeader)
        {
            if (string.IsNullOrEmpty(appHeader))
                return Unauthorized(new { error = "Missing X-Una-App header" });

            var type = DummyData.ContractTypes.FirstOrDefault(t => t.Id == id);
            if (type == null)
                return NotFound(new { error = "Contract type not found" });

            return Ok(type);
        }
    }
}
