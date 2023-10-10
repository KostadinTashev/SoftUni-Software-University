SELECT
    b.id AS "id",
    b.name AS "name",
    b.release_year AS "release_year",
    c.name AS "category_name"
FROM
    board_games AS b
JOIN
    categories AS c
ON
    b.category_id = c.id
WHERE
    c.name = 'Strategy Games'
        OR
    c.name = 'Wargames'
ORDER BY
    b.release_year DESC;