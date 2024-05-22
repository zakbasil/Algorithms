/*

Anton wants to fetch the students who are not allocated 
to a class in his school.
He wrote a query to fetch all students unallocated, 
using SQL query.
But the result of the query had all the students, 
he coulld see allocated and unallocated students in the list.
Help him find the solution.

*/


SELECT *
FROM Students
LEFT JOIN Class
ON Students.classId = Class.Id
