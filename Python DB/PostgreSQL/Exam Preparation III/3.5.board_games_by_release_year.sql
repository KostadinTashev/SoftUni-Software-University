SELECT
    b.name AS "name",
    b.rating AS "rating"
FROM
    board_games AS b
ORDER BY
    b.release_year ASC,
    b.name DESC;