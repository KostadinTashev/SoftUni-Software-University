SELECT 
	SUBSTRING(description, 5, length(description)) AS "substring"
FROM 
	currencies;

-- SELECT 
-- 	SUBSTRING(description FROM 5) AS "substring"
-- FROM 
-- 	currencies;

-- SELECT 
-- 	RIGHT(description, -4) AS "substring"
-- FROM 
-- 	currencies;