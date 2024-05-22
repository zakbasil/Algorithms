SELECT Department, sum(Salary) as SumSalary
FROM employee
GROUP BY department
HAVING SUM(Salary) >= 50000;