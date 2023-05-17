from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
import textwrap


class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def process_albums_selection(self):
        print("We're going to print out the albums!")
        album_repository = AlbumRepository(self._connection)
        artist_repository = ArtistRepository(self._connection)

        albums = album_repository.all()
        for album in albums:
            artist = artist_repository.find(album.artist_id)
            print(f"{album.id}: {album.title} {album.release_year} by {artist.name}")

    def process_artists_selection(self):
        print("We're going to print out the artists!")
        artist_repository = ArtistRepository(self._connection)

        artists = artist_repository.all()
        for artist in artists:
            print(f"{artist.id}: {artist.name} {artist.genre}")

    def run(self):
        while True:
            # remove the common leading whitespace from each line of your multi-line string
            print(textwrap.dedent(
                """
                Welcome to the music library manager!

                What would you like to do?
                1 - List all albums
                2 - List all artists
                3 - Exit
                """
            ))

            # try/except block to handle exceptions that may be raised by the int() function when it tries to convert the user's input to an integer
            try:
                selection = int(input())
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if selection == 1:
                self.process_albums_selection()
            elif selection == 2:
                self.process_artists_selection()
            elif selection == 3:
                break
            else:
                print("Invalid selection. Please enter 1 or 2.")


if __name__ == "__main__":
    app = Application()
    app.run()
