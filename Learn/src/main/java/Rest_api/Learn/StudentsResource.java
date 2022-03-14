package Rest_api.Learn;
import java.util.List;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("Students")
public class StudentsResource 
{
	StudentRep repo = new StudentRep();
	@GET
	@Produces(MediaType.APPLICATION_XML)
	public List<students_info> get_info()
	{
		System.out.println("The get_info method is called ");
		
		return repo.getStudents();
		}
}
