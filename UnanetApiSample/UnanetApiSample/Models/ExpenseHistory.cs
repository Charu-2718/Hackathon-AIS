namespace UnanetApiSample.Models
{
    public class ExpenseHistory
    {
        public int Id { get; set; }
        public int ExpenseId { get; set; }
        public string Status { get; set; } = "";
        public DateTime Date { get; set; }
    }
}
