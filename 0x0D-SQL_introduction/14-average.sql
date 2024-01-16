-- Filename: compute_score_average.sql

-- Compute the score average of all records in 'second_table' with result column name as 'average'
SELECT AVG(score) AS average FROM `second_table`;
