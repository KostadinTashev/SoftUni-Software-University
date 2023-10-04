WITH row_number AS (
  SELECT
    c.country_name,
    p.peak_name,
    p.elevation,
    m.mountain_range,
    ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS peak_rank
  FROM countries c
  LEFT JOIN 
    mountains_countries mc 
  USING
    (country_code)
  LEFT JOIN 
    peaks p 
  USING
    (mountain_id)
  LEFT JOIN
    mountains m 
  ON 
    p.mountain_id = m.id
)

SELECT
  r.country_name,
  COALESCE(r.peak_name, '(no highest peak)') AS peak_name,
  COALESCE(CAST(r.elevation AS VARCHAR), '0') AS elevation,
  COALESCE(r.mountain_range, '(no mountain)') AS mountain_range
FROM 
    row_number r
WHERE 
    r.peak_rank = 1
ORDER BY 
    r.country_name ASC,
     r.elevation DESC;
