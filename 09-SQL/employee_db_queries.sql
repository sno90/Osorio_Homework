
-- List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary 
FROM employees e
LEFT JOIN salaries s 
ON e.emp_no = s.emp_no;

-- List employees who were hired in 1986.
SELECT * FROM employees 
WHERE hire_date BETWEEN '1986/01/01' and '1987/01/31';

-- List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT d.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM dept_manager dm 
LEFT JOIN employees e ON dm.emp_no = e.emp_no
LEFT JOIN departments d ON d.dept_no = dm.dept_no

-- List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e 
LEFT JOIN dept_employee de ON de.emp_no = e.emp_no
LEFT JOIN departments d ON d.dept_no=de.dept_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees 
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_employee de
LEFT JOIN employees e ON e.emp_no = de.emp_no
LEFT JOIN departments d ON d.dept_no = de.dept_no
WHERE dept_name = 'Sales';

-- List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_employee de
LEFT JOIN employees e ON e.emp_no = de.emp_no
LEFT JOIN departments d ON d.dept_no = de.dept_no
WHERE dept_name = 'Sales' OR dept_name = 'Development';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select e.last_name, count(e.last_name)
FROM employees e
GROUP BY e.last_name
ORDER BY count(e.last_name) ASC;

