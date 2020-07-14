-- 5-unique_id.sql
-- Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
) ENGINE=INNODB;
