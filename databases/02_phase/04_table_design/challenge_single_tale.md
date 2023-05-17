# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.
```

```
Nouns:

movies, user, favourite, title, genre, release_year
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record    | Properties        |
| --------- | ----------------- |
| user      |                   |
| movie     | title, genre      |
| favourite | user_id, movie_id |

Name of the table (always plural): `users`

Name of the table (always plural): `movies`
Column names: `title`, `genre`

Name of the table (always plural): `favourites`
Column names: `user_id`, `movie_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# USERS:

id: SERIAL PRIMARY KEY

# FAVOURITES:

id: SERIAL PRIMARY KEY
user_id: SERIAL FOREIGN KEY
movie_id: SERIAL FOREIGN KEY

# MOVIES:

id: SERIAL PRIMARY KEY
title: text
genre: text
```

## 4. Write the SQL

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    genre text
);

CREATE TABLE favourites (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < users_table.sql
psql -h 127.0.0.1 database_name < movies_table.sql
psql -h 127.0.0.1 database_name < favourites_table.sql
```
