-- use the CASCADE option to automatically drop the "posts" table when the "users" table is dropped:
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
-- it is common practice to create a sequence object to automatically generate unique values for a primary key column.
-- This helps ensure that each record in the table has a unique identifier, which is necessary for indexing, referencing,
-- and updating records. The sequence object is usually named after the column it is associated with, followed by "_seq" or
-- a similar suffix, to make it clear what its purpose is.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email_address text
);

INSERT INTO users (username, email_address) VALUES ('adrian', 'adrian@gmail.com');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then the table with the foreign key second.
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO posts (title, content, views, user_id) VALUES ('snakes, rubies and tdd', 'hello world', 1, 1);
