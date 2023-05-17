DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

INSERT INTO posts (title, content) VALUES ('post title', 'post content');


-- Then the table with the foreign key second.
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    name text,
    content text,
-- The foreign key name is always {other_table_singular}_id
    post_id int,
    constraint fk_post foreign key(post_id)
        references posts(id)
        on delete cascade
);

INSERT INTO comments (name, content, post_id) VALUES ('Adrian', 'great post', 1);
INSERT INTO comments (name, content, post_id) VALUES ('Nish', 'crap post', 1);
