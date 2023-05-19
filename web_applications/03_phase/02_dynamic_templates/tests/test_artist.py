from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""


def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"


"""
We can format artists to strings nicely
"""


def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"


"""
We can compare two identical artists
And have them be equal
"""


def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2


"""
We can assess the validity of an artist
"""


def test_artist_validity():
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "TayTay", "").is_valid() == False
    assert Artist(1, "", "Pop").is_valid() == False
    assert Artist(1, "TayTay", None).is_valid() == False
    assert Artist(1, None, "Pop").is_valid() == False
    assert Artist(1, "TayTay", "Pop").is_valid() == True
    assert Artist(None, "TayTay", "Pop").is_valid() == True


"""
We can generate errors for an invalid artist
"""


def test_artist_errors():
    assert (
        Artist(1, "", "").generate_errors()
        == "Name can't be blank, Genre can't be blank"
    )
    assert Artist(1, "TayTay", "").generate_errors() == "Genre can't be blank"
    assert Artist(1, "", "Pop").generate_errors() == "Name can't be blank"
    assert Artist(1, "TayTay", None).generate_errors() == "Genre can't be blank"
    assert Artist(1, None, "Pop").generate_errors() == "Name can't be blank"
    assert Artist(1, "TayTay", "Pop").generate_errors() == None
    assert Artist(None, "TayTay", "Pop").generate_errors() == None
