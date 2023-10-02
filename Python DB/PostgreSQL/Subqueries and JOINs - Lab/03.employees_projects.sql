SELECT 
	e.employee_id AS employee_id,
	CONCAT_WS(' ', e.first_name, e.last_name) AS full_name,
	p.project_id AS project_id,
	p.name AS project_name
FROM
	employees AS e
JOIN 
	employees_projects AS ep
ON
	e.employee_id = ep.employee_id
JOIN
	projects AS p
ON
	ep.project_id = p.project_id
WHERE
	project_id = 1

-- SELECT 
-- 	e.employee_id AS employee_id,
-- 	CONCAT_WS(' ', e.first_name, e.last_name) AS full_name,
-- 	p.project_id AS project_id,
-- 	p.name AS project_name
-- FROM
-- 	employees AS e
-- JOIN 
-- 	employees_projects AS ep
-- USING
-- 	(employee_id)
-- JOIN
-- 	projects AS p
-- USING
-- 	(project_id)
-- WHERE
-- 	project_id = 1