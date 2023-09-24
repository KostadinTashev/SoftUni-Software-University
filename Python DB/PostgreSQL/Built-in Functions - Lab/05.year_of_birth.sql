SELECT 	
	first_name,
	last_name,
	EXTRACT('year' from born)
FROM
	authors;

-- SELECT 
-- 	first_name,
-- 	last_name,
-- 	to_char(born, 'YYYY') AS year
-- FROM
-- 	authors;
	