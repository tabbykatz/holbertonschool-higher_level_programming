-- 101-avg_temperatures.sql
-- Write a script that displays the average temperature 
SELECT city, AVG(value) AS "avg_temp" FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
