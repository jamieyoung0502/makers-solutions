from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_all_records(db_connection):
    # re-seed each time for testing purposes
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()

    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_find_specific_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    assert album == Album(1, 'Doolittle', 1989, 1)

"""
When we call AlbumRepository#create
Add a new album
List all albums to show new album
"""

def test_create_new_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Jasmine', 2023, 1)
    result = repository.create(album)
    assert result == None

    albums = repository.all()

    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Jasmine', 2023, 1)
    ]

"""
When we call AlbumRepository#delete
Delete an album
List all albums to show album is gone
"""

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    result = repository.delete(1)
    assert result == None

    albums = repository.all()
    assert albums == [
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]



