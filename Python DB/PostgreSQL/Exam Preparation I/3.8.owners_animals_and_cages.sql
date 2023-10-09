SELECT
	CONCAT_WS(' - ', o.name, a.name) AS "Owners - Animals",
	o.phone_number AS "Phone Number",
	ac.cage_id AS "Cage ID"
FROM
	owners AS o
JOIN
	animals AS a
ON
    o.id = a.owner_id
JOIN
	animals_cages AS ac
ON
    a.id = ac.animal_id
JOIN
	animal_types AS at
ON
    a.animal_type_id = at.id
WHERE
    at.animal_type = 'Mammals'
ORDER BY
	o.name ASC,
    a.name DESC;