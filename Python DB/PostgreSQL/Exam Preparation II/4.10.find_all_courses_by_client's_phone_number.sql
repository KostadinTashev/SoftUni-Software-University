CREATE OR REPLACE FUNCTION fn_courses_by_client(
	IN phone_num VARCHAR(20),
	OUT num_of_courses INT
) RETURNS INT AS
$$
BEGIN
    num_of_courses := (
        SELECT
            COUNT(co.id)
        FROM
            clients AS cl
        JOIN
            courses AS co
        ON
            cl.id = co.client_id
        WHERE
            cl.phone_number = phone_num
    );
END;
$$
LANGUAGE plpgsql;