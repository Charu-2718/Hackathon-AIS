namespace UnanetApiSample.Models
{
    public class TimesheetAttachment
    {
        public int Id { get; set; }
        public int TimesheetId { get; set; }
        public string FileName { get; set; } = "";
    }
}
