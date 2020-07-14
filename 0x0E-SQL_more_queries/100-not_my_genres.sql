-- 100-not_my_genres.sql
--  uses the hbtn_0d_tvshows database to list all genres not linked to the show
--  Dexter
SELECT DISTINCT tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name NOT IN (
SELECT g.name FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
	AND t.show_id = s.id
	AND s.title = "Dexter"
) ORDER BY tv_genres.name;
