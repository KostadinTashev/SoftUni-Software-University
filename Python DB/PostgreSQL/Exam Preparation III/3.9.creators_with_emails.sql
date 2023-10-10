SELECT
    CONCAT(cr.first_name, ' ', cr.last_name) AS "full_name",
    cr.email AS "email",
    MAX(bg.rating) AS "rating"
FROM
    creators AS cr
JOIN
    creators_board_games AS cbg
ON
    cr.id = cbg.creator_id
JOIN
    board_games AS bg
ON
    cbg.board_game_id = bg.id
WHERE
    cr.email LIKE '%.com'
GROUP BY
   "full_name",
   "email"
ORDER BY
    "full_name" ASC;