UPDATE
    coaches AS c
SET
    salary = c.salary * c.coach_level
FROM (
    SELECT
        pc.coach_id,
        COUNT(pc.player_id) AS player_count
    FROM
        players_coaches AS pc
    GROUP BY
        pc.coach_id) AS pco
WHERE
    c.first_name LIKE 'C%'
        AND
    c.id = pco.coach_id
        AND
    pco.player_count > 0;