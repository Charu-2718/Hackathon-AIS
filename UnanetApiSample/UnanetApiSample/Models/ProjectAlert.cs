namespace UnanetApiSample.Models
{
    public class ProjectAlert
    {
        public int Id { get; set; }
        public int ProjectId { get; set; }
        public string Message { get; set; } = "";
    }
}
