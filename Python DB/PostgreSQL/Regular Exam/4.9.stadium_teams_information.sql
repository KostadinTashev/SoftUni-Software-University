CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    IN stadium_name VARCHAR(30)
) RETURNS TABLE (team_name VARCHAR(50))
AS
$$
BEGIN
    RETURN QUERY
    SELECT
        t.name
    FROM
        teams AS t
    JOIN
        stadiums AS st
    ON
        t.stadium_id = st.id
    WHERE
        st.name = stadium_name
    ORDER BY
        t.name;
END;
$$
LANGUAGE plpgsql;