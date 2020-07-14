-- 14-my_genres.sql
-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
	AND t.show_id = s.id
	AND s.title = "Dexter"
ORDER BY g.name ASC;
; 
