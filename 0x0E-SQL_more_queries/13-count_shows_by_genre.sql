-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_genres.name AS genres, COUNT(tv_genres.id) AS numbers_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genres_id
GROUP BY genre
ORDER BY number_of_shows DESC;
