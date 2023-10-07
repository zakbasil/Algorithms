SELECT Department, sum(Salary) as Salary
FROM employee
GROUP BY department
WHERE SUM(Salary) >= 50000;  