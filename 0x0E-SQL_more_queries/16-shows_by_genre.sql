-- script that lists all shows, and all genres linked to that show
-- If a show doesn’t have a genre, display NULL in the genre column

SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name  IS NULL OR tv_genres.name IS NOT NULL
ORDER BY title ASC, name;
