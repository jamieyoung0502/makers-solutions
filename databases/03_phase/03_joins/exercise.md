Use a SELECT query with a JOIN to retrieve all the posts associated with the tag 'travel'.

You should get the following result set:

```sql
 id |          title
----+-------------------------
  4 | My weekend in Edinburgh
  6 | A foodie week in Spain
```

```sql
SELECT
	posts.id,
	posts.title
FROM
	posts
	JOIN posts_tags ON posts_tags.post_id = posts.id
	JOIN tags ON tags.id = posts_tags.tag_id
WHERE
	tags.name = 'travel';
```
