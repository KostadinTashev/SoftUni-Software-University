CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
) AS
$$
BEGIN
    team_name :=(
    SELECT
        t.name
    FROM
        teams AS t
    JOIN
        players AS pl
    ON
        t.id = pl.team_id
    WHERE
        CONCAT_WS(' ', pl.first_name, pl.last_name) = player_name);
    IF team_name IS NULL THEN
        team_name = 'The player currently has no team';
    END IF;
END;
$$
LANGUAGE plpgsql;