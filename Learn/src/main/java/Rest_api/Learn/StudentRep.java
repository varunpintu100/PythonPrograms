package Rest_api.Learn;

import java.util.ArrayList;
import java.util.List;

public class StudentRep {
	
	List<students_info> Students;
	public StudentRep()
	{
		Students = new ArrayList<>();
		students_info student = new students_info();
		student.setName("varun");
		student.setPoints(100);
		students_info student1 = new students_info();
		student1.setName("vedhanth");
		student1.setPoints(80);
		Students.add(student);
		Students.add(student1);
	}
	public List<students_info> getStudents()
	{
		return Students;
	}
	public students_info getStudent(int points)
	{
		for(students_info s : Students)
		{
			if(s.getPoints()==points)
				return s;
		}
		
		return null;
	}
}
