from lib.comment import Comment
from lib.post import Post

class PostRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_with_comments(self, post_id):
        query = """
        SELECT
            posts.id AS post_id,
            posts.title,
            posts.content AS post_content,
            comments.id AS comment_id,
            comments.name,
            comments.content AS comment_content
        FROM
            comments
            JOIN posts ON posts.id = comments.post_id
        WHERE
            posts.id = %s;
        """
        rows = self._connection.execute(query, [post_id])

        comments = [Comment(row["comment_id"], row["name"], row["comment_content"], row["post_id"])  for row in rows]

        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)
