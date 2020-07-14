-- 4-never_empty.sql
-- creates the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
) ENGINE=INNODB;
