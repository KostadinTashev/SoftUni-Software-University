CREATE FUNCTION fn_count_employees_by_town(IN town_name VARCHAR(20))
RETURNS INT AS
$$
	DECLARE
		town_count INT;
	BEGIN
		SELECT 
			COUNT(*)
		FROM
			employees AS e
		JOIN
			addresses AS a
		USING
			(address_id)
		JOIN
			towns AS t
		USING
			(town_id)
		WHERE
			t.name = town_name
		INTO
			town_count;
		RETURN town_count;
	END
$$
LANGUAGE plpgsql;

-- CREATE FUNCTION fn_count_employees_by_town(IN town_name VARCHAR(20))
-- RETURNS INT AS
-- $$
-- 	BEGIN
-- 		RETURN
-- 		(
-- 			SELECT 
-- 				COUNT(*)
-- 			FROM
-- 				employees AS e
-- 			JOIN
-- 				addresses AS a
-- 			USING
-- 				(address_id)
-- 			JOIN
-- 				towns AS t
-- 			USING
-- 				(town_id)
-- 			WHERE
-- 				t.name = town_name
-- 		);
-- 	END
-- $$
-- LANGUAGE plpgsql;