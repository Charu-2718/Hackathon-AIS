namespace UnanetApiSample.Models
{
    public class TimesheetAdjustment
    {
        public int Id { get; set; }
        public int TimesheetId { get; set; }
        public string Reason { get; set; } = "";
    }
}
