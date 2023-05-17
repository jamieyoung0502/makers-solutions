from lib.post import Post

class PostRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_with_tag_name(self, tag_name):
        query="""
        SELECT
            posts.id,
            posts.title
        FROM
            posts
            JOIN posts_tags ON posts_tags.post_id = posts.id
            JOIN tags ON tags.id = posts_tags.tag_id
        WHERE
            tags.name = %s;
        """
        rows = self._connection.execute(query, [tag_name])
        return [Post(row['id'], row['title']) for row in rows]