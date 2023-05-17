# Music Web App Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Post a new album route
POST /albums
    Parameters:
        title: string
        release_year: int
        artist_id: int

# Get all artists route
GET /artists

# Post an new artist route
POST /artists
    Parameters:
        name: string
        genre: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /albums
#   Parameters:
#     title: "My Album Title"
#     release_year: 2021
#     artist_id: 3
#   Expected response (200 OK):
"""
Album created successfully.
"""

# POST /albums
#   Parameters:
#     title: "My Album Title"
#     release_year: "bananas"
#     artist_id: 3
#   Expected response (400 Bad Request):
"""
Please provide the correct album info.
"""

# GET /artists
#   Expected response (200 OK)
"""
Taylor Swift, Victoria Bigelow
"""

# Post an new artist route
# POST /artists
#   Parameters:
#     name: string
#     genre: string
"""
Artist created successfully
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
import textwrap

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
    assert get_response.data.decode('utf-8') == textwrap.dedent("""
        Album(1, "Midnights", 2022, 1),
        Album(2, "reputation", 2017, 1),
        Album(3, "Going Blue", 2019, 2),
        Album(4, "folklore", 2020, 1)
    """)

"""
POST /albums
    Parameters:
        title: "folklore"
        release_year: "bananas"
        artist_id: 1
    Expected response (400 Bad Request):
"""
def test_post_invalid_album(db_connection, web_client)
    db_connection.seed("seeds/albums_artists_tables.sql")

    with pytest.raises(TypeError) as error:
        response = web_client.post('/albums', data={
            'title': 'folklore',
            'release_year': "bananas",
            'artist_id': 1
        })
    assert response.status_code == 400
    assert str(error) == "release year should be an integer, four numbers in length"

"""
GET /artists
    Parameters: none
    Expected response (200 OK):
        "Taylor Swift, Victoria Bigelow"
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Taylor Swift, Victoria Bigelow'

"""
POST /artists
    Parameters:
        name: "Kate"
        genre: "Heavy Metal"
    Expected response (200 OK):
"""
def test_post_artist(web_client):
    post_response = web_client.post('/artists')
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Artist created successfully.'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == textwrap.dedent("""
        Artist(1, "Taylor Swift", "Pop"),
        Artist(2, "Victoria Bigelow", "Mopey"),
        Artist(3, "Kate", "Heavy Metal")
    """)
```
