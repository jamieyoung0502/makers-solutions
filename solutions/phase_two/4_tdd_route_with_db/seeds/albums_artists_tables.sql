DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;

CREATE TABLE artists (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	genre VARCHAR(255)
);

INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Victoria Bigelow', 'Mopey');

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;

CREATE TABLE albums (
	id SERIAL PRIMARY KEY,
	title text,
	release_year int,
	artist_id int,
	CONSTRAINT fk_artist FOREIGN KEY (artist_id) REFERENCES artists (id) ON DELETE CASCADE
);

INSERT INTO albums (title, release_year) VALUES ('Midnights', 2022, 1);
INSERT INTO albums (title, release_year) VALUES ('reputation', 2017, 1);
INSERT INTO albums (title, release_year) VALUES ('Going Blue', 2019, 2);
