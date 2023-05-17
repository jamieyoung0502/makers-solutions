from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/albums_artists_tables.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    # Assert on the results
    assert artists == [
        Artist(1, "Taylor Swift", "Pop"),
        Artist(2, "Victoria Bigelow", "Mopey")
    ]
