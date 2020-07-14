-- 15-comedy_only.sql
--  lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
	AND t.show_id = s.id
	AND g.name = "Comedy"
ORDER BY s.title ASC;
;
