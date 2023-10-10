SELECT
    cr.id AS "id",
    CONCAT_WS(' ', cr.first_name, cr.last_name) AS "creator_name",
    cr.email AS "email"
FROM
    creators AS cr
LEFT JOIN
    creators_board_games as cdb
ON
    cr.id = cdb.creator_id
WHERE
    cdb.creator_id IS NULL
ORDER BY
    "creator_name" ASC;