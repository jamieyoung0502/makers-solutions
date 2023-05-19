from lib.artist import Artist


class ArtistRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        return [Artist(row["id"], row["name"], row["genre"]) for row in rows]

    def find(self, id):
        query = """
        SELECT *
        FROM artists
        WHERE id = %s
        """
        artist = self._connection.execute(query, [id])[0]
        return Artist(artist["id"], artist["name"], artist["genre"])

    def create(self, artist):
        rows = self._connection.execute(
            "INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id",
            [artist.name, artist.genre],
        )

        row = rows[0]
        artist.id = row["id"]
        return artist
