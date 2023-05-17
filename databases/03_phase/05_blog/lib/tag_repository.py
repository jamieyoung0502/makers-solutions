from lib.tag import Tag

class TagRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_with_tag(self, post_title):
        query="""
        SELECT
            tags.id,
            tags.name
        FROM
            tags
            JOIN posts_tags ON posts_tags.tag_id = tags.id
            JOIN posts ON posts.id = posts_tags.post_id
        WHERE
            posts.title = %s;
        """
        rows = self._connection.execute(query, [post_title])
        return [Tag(row['id'], row['name']) for row in rows]
