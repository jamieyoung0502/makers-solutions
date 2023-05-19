from unittest.mock import Mock
from lib.album import Album

"""
Album class constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    artist_mock = Mock()
    artist_mock.id.return_value = 1
    album = Album(1, "Test Title", "Test Year", artist_mock.id())
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == "Test Year"
    assert album.artist_id == 1


"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    artist_mock = Mock()
    artist_mock.id.return_value = 1
    album = Album(1, "Test Title", "Test Year", artist_mock.id())
    assert str(album) == "Album(1, Test Title, Test Year, 1)"


"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    artist_mock = Mock()
    artist_mock.id.return_value = 1
    album_1 = Album(1, "Test Title", "Test Year", artist_mock.id())
    album_2 = Album(1, "Test Title", "Test Year", artist_mock.id())
    assert album_1 == album_2