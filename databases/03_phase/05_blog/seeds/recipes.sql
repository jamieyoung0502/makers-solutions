-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title text,
    cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (title, cooking_time, rating) VALUES ('recipe1', 20, 5);
INSERT INTO recipes (title, cooking_time, rating) VALUES ('recipe2', 60, 3);
INSERT INTO recipes (title, cooking_time, rating) VALUES ('recipe3', 10, 5);
INSERT INTO recipes (title, cooking_time, rating) VALUES ('recipe4', 15, 5);
INSERT INTO recipes (title, cooking_time, rating) VALUES ('recipe5', 30, 4);
