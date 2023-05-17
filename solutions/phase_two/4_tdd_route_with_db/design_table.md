# Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
Nouns:

album, title, release year, artist, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record | Properties                     |
| ------ | ------------------------------ |
| album  | title, release year, artist_id |
| artist | name                           |

Name of the table (always plural): `albums, artists`

Column names: `title`, `release_year`, `artist_id`
Column names: `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
id: SERIAL
title: text
release_year: int
artist_id: int

id: SERIAL
name: text
```

## 4. Write the SQL

```sql
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int,
      constraint fk_artist foreign key(artist_id)
        references artists(id)
        on delete cascade
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_library < albums_artists_tables.sql
```
