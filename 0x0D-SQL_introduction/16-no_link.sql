-- Filename: list_records.sql

-- List all records with a name value in 'second_table'
SELECT score, name FROM `second_table`
WHERE name IS NOT NULL
ORDER BY score DESC;
