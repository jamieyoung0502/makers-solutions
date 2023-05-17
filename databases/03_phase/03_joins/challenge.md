Use SQL to insert a new tag 'sql' and associate the post titled 'SQL basics' with this tag.

Then use a SELECT query with a JOIN to retrieve all posts associated with the tag 'sql' and verify the above worked.

```sql
INSERT INTO tags (name)
		VALUES('sql');

INSERT INTO posts_tags (post_id, tag_id)
		VALUES(7, 5);

SELECT
	posts.id,
	posts.title
FROM
	posts
	JOIN posts_tags ON posts_tags.post_id = posts.id
	JOIN tags ON tags.id = posts_tags.tag_id
WHERE
	tags.name = 'sql';
```
