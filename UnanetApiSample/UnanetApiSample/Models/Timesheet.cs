namespace UnanetApiSample.Models
{
    public class Timesheet
    {
        public int Id { get; set; }
        public int EmployeeId { get; set; }
        public DateTime Date { get; set; }
        public double HoursWorked { get; set; }
    }
}
