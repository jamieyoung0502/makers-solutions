from lib.album import Album
class AlbumRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def find(self, id):
        query = """
        SELECT *
        FROM albums
        WHERE id = %s
        """
        album = self._connection.execute(query, [id])[0]
        return Album(album["id"], album["title"], album["release_year"], album["artist_id"])

    def create(self, new_album):
        query = """
        INSERT INTO albums
        (title, release_year, artist_id)
        VALUES(%s, %s, %s)
        """
        self._connection.execute(query, [new_album.title, new_album.release_year, new_album.artist_id])
        return None

    def delete(self, id):
        query = """
        DELETE FROM albums
        WHERE id = %s
        """
        self._connection.execute(query, [id])
        return None
