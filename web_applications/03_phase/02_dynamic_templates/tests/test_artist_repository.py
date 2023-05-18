from lib.artist_repository import ArtistRepository
from lib.artist import Artist


def test_list_all_artists(db_connection):
    db_connection.seed("seeds/spotify.sql")
    repository = ArtistRepository(db_connection)

    result = repository.all()
    assert result == [
        Artist(1, "Taylor Swift", "Pop"),
        Artist(2, "Victoria Bigelow", "Mopey"),
    ]


def test_create_artist(db_connection):
    db_connection.seed("seeds/spotify.sql")
    repository = ArtistRepository(db_connection)
    create_result = repository.create(Artist(None, "Kate", "Heavy Metal"))
    assert create_result == None

    all_result = repository.all()
    assert all_result == [
        Artist(1, "Taylor Swift", "Pop"),
        Artist(2, "Victoria Bigelow", "Mopey"),
        Artist(3, "Kate", "Heavy Metal"),
    ]
