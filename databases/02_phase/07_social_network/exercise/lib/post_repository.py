from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        return [Post(row["id"], row["title"], row["content"], row["views"], row["user_id"]) for row in rows]

    def find(self, post_id):
        query = """
        SELECT *
        FROM posts
        WHERE id = %s
        """
        post = self._connection.execute(query, [post_id])[0]
        return Post(post["id"], post["title"], post["content"], post["views"], post["user_id"])

    def create(self, post):
        query = """
        INSERT INTO posts
        (title, content, views, user_id)
        VALUES (%s, %s, %s, %s)
        """
        post = self._connection.execute(query, [post.title, post.content, post.views, post.user_id])

    def update(self, col_name, new_value, post_id):
        query = """
        UPDATE posts
        SET {} = %s
        WHERE id = %s;
        """.format(col_name)

        self._connection.execute(query, [new_value, post_id])

    def delete(self, post_id):
        query = """
        DELETE FROM posts
        WHERE id = %s;
        """
        self._connection.execute(query, [post_id])