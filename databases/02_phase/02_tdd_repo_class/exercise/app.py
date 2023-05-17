from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.find(1)

if not isinstance(artists, Artist):
    for artist in artists:
        print(artist)
else:
    print(artists)
