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


"""
We can assess the validity of an album
"""


def test_album_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "", "", None).is_valid() == False
    assert Album(1, "Best Of", "", 1).is_valid() == False
    assert Album(1, "", "2023", 1).is_valid() == False
    assert Album(1, "Best Of", None, 1).is_valid() == False
    assert Album(1, None, "2023", 1).is_valid() == False
    assert Album(1, "Best Of", "2023", "").is_valid() == False
    assert Album(1, "Best Of", "2023", None).is_valid() == False
    assert Album(None, "Best Of", "2023", "").is_valid() == False
    assert Album(None, "Best Of", "2023", None).is_valid() == False
    assert Album(1, "Best Of", "2023", 1).is_valid() == True
    assert Album(None, "Best Of", "2023", 1).is_valid() == True


"""
We can generate errors for an invalid album
"""


def test_album_errors():
    assert (
        Album(1, "", "", "").generate_errors()
        == "Title can't be blank, Release Year can't be blank, Artist can't be blank"
    )
    assert (
        Album(1, "", "", None).generate_errors()
        == "Title can't be blank, Release Year can't be blank, Artist can't be blank"
    )
    assert Album(1, "Best Of", "", 1).generate_errors() == "Release Year can't be blank"
    assert Album(1, "", "2023", 1).generate_errors() == "Title can't be blank"
    assert Album(1, None, "2023", 1).generate_errors() == "Title can't be blank"
    assert (
        Album(1, "Best Of", None, 1).generate_errors() == "Release Year can't be blank"
    )
    assert Album(1, "Best Of", "2023", "").generate_errors() == "Artist can't be blank"
    assert (
        Album(1, "Best Of", "2023", None).generate_errors() == "Artist can't be blank"
    )
    assert (
        Album(None, "Best Of", "2023", "").generate_errors() == "Artist can't be blank"
    )
    assert (
        Album(None, "Best Of", "2023", None).generate_errors()
        == "Artist can't be blank"
    )
    assert Album(1, "Best Of", "2023", 1).generate_errors() == None
    assert Album(None, "Best Of", "2023", 1).generate_errors() == None
