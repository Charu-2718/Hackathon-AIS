namespace UnanetApiSample.Models
{
    public class TimesheetAudit
    {
        public int Id { get; set; }
        public int TimesheetId { get; set; }
        public string Action { get; set; } = "";
        public DateTime Date { get; set; }
    }
}
