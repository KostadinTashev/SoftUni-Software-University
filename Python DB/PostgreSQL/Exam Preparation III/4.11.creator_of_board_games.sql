CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    first_name_of_a_game_creator VARCHAR(30)
) RETURNS INT
AS
$$
BEGIN
    RETURN (
    SELECT
        COUNT(*)
    FROM
        creators AS cr
    JOIN
        creators_board_games AS cbg
    ON
        cr.id = cbg.creator_id
    WHERE
        cr.first_name = first_name_of_a_game_creator);
END;
$$
LANGUAGE plpgsql;