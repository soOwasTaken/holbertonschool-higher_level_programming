-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_genres.name AS genre, count(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;