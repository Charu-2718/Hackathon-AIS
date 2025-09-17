namespace UnanetApiSample.Models
{
    public class Expense
    {
        public int Id { get; set; }
        public int ProjectId { get; set; }
        public decimal Amount { get; set; }
        public string Description { get; set; } = "";
    }
}
