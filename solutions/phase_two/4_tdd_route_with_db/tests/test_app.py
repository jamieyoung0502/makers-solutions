import pytest
"""
POST /albums
    Parameters:
        title: "folklore"
        release_year: 2020
        artist_id: 1
    Expected response (200 OK):
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/albums_artists_tables.sql")
    post_response = web_client.post('/albums', data={
        'title': 'folklore',
        'release_year': 2020,
        'artist_id': 1
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Album created successfully.'

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        'Album(1, Midnights, 2022, 1)\n' \
        'Album(2, reputation, 2017, 1)\n' \
        'Album(3, Going Blue, 2019, 2)\n' \
        'Album(4, folklore, 2020, 1)'
"""
GET /artists
    Parameters: none
    Expected response (200 OK):
        "Taylor Swift, Victoria Bigelow"
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        'Artist(1, Taylor Swift, Pop)\n' \
        'Artist(2, Victoria Bigelow, Mopey)'

"""
POST /artists
    Parameters:
        name: "Kate"
        genre: "Heavy Metal"
    Expected response (200 OK):
"""
def test_post_artist(web_client):
    post_response = web_client.post('/artists', data={
        'name' : 'Kate',
        'genre' : 'Heavy Metal'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Artist created successfully.'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        'Artist(1, Taylor Swift, Pop)\n' \
        'Artist(2, Victoria Bigelow, Mopey)\n' \
        'Artist(3, Kate, Heavy Metal)'

"""
POST /albums
    Parameters:
        title: "folklore"
        release_year: "bananas"
        artist_id: 1
    Expected response (400 Bad Request):
"""
def test_post_invalid_album(db_connection, web_client):
    db_connection.seed("seeds/albums_artists_tables.sql")

    with pytest.raises(TypeError) as error:
        response = web_client.post('/albums', data={
            'title': 'folklore',
            'release_year': "bananas",
            'artist_id': 1
        })
        print(response.error, response.data)
        error_message = str(error.value)
        assert error_message == "release year should be an integer, four numbers in length"
        assert response.status_code == 400