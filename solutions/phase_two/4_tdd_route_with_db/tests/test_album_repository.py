from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_all_records(db_connection):
    # re-seed each time for testing purposes
    db_connection.seed("seeds/albums_artists_tables.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()

    assert albums == [
        Album(1, 'Midnights', 2022, 1),
        Album(2, 'reputation', 2017, 1),
        Album(3, 'Going Blue', 2019, 2),
    ]

"""
When we call AlbumRepository#create
Add a new album
List all albums to show new album
"""

def test_create_new_record(db_connection):
    db_connection.seed("seeds/albums_artists_tables.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'folklore', 2020, 1)
    result = repository.create(album)
    assert result == None

    albums = repository.all()

    assert albums == [
        Album(1, 'Midnights', 2022, 1),
        Album(2, 'reputation', 2017, 1),
        Album(3, 'Going Blue', 2019, 2),
        Album(4, 'folklore', 2020, 1)
    ]

