-- 9-cities_by_state_join.sql
-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
