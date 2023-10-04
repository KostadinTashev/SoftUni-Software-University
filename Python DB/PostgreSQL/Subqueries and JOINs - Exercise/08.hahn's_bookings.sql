SELECT
	COUNT(*) AS "count"
FROM 
	bookings AS b
JOIN
	customers AS c
USING
	(customer_id)
WHERE
	c.last_name = 'Hahn'