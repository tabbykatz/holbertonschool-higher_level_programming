-- 16-no_link.sql
-- lists all records of the table second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
