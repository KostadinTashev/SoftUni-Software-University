SELECT
    CONCAT_WS(' ', c.first_name, c.last_name) AS coach_full_name,
    CONCAT_WS(' ', pl.first_name, pl.last_name) AS player_full_name,
    t.name AS team_name,
    sd.passing,
    sd.shooting,
    sd.speed
FROM
    coaches AS c
JOIN
    players_coaches AS plc
ON
    c.id = plc.coach_id
JOIN
    players AS pl
ON
    plc.player_id = pl.id
JOIN
    teams AS t
ON
    pl.team_id = t.id
JOIN
    skills_data AS sd
ON
    pl.skills_data_id = sd.id
ORDER BY
    coach_full_name,
    player_full_name DESC;