SELECT
    pl.id,
    CONCAT_WS(' ', pl.first_name, pl.last_name) AS full_name,
    pl.age,
    pl.position,
    pl.salary,
    sd.pace,
    sd.shooting
FROM
    players AS pl
JOIN
    skills_data AS sd
ON
    pl.skills_data_id = sd.id
WHERE
    pl.position = 'A'
        AND
    pl.team_id IS NULL
        AND
    (sd.pace + sd.shooting) > 130;