-- a script that lists all records of second_table
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;