-- 9-full_creation.sql
-- creates a table second_table, add rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
				
) ENGINE=INNODB;
INSERT INTO second_table
VALUES (1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
