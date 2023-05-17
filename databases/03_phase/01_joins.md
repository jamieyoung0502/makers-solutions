Use the database music_library for the following exercises. You can load the seed file data in again with:

```bash
# From the starter project directory, in your terminal
; dropdb music_library
; createdb music_library
; psql -h 127.0.0.1 music_library < seeds/music_library.sql
```

# Exercise 1:

Using psql, use a JOIN query to select the id and title of all the albums from Taylor Swift.

```sql
 id |  title
----+----------
  6 | Lover
  7 | Folklore
```

Answer:

```sql
SELECT
	albums.id,
	albums.title
FROM
	albums
	JOIN artists ON artists.id = albums.artist_id
WHERE
	artists.name = 'Taylor Swift';
```

# Exercise 2

Use a JOIN query to find the id and title of the (only) album from Pixies released in 1988.

You should get the following result set:

```sql
 id |    title
----+-------------
  2 | Surfer Rosa
```

Answer:

```sql
SELECT
	albums.id,
	albums.title
FROM
	albums
	JOIN artists ON artists.id = albums.artist_id
WHERE
	artists.name = 'Pixies'
	AND albums.release_year = 1988;
```

# Challenge

Find the album_id and title of all albums from Nina Simone released after 1975.

You should get the following result set:

```sql
 album_id |       title
----------+--------------------
        9 | Baltimore
       11 | Fodder on My Wings
```

Answer:

```sql
SELECT
	albums.id AS album_id,
	albums.title
FROM
	albums
	JOIN artists ON artists.id = albums.artist_id
WHERE
	artists.name = 'Nina Simone'
	AND albums.release_year > 1975;
```
