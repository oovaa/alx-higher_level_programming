-- Filename: count_records_by_score.sql

-- List the number of records with the same score in 'second_table'
SELECT score, COUNT(*) AS count FROM `second_table` GROUP BY score;
