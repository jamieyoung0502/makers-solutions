# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Sort names route
POST /sort-names
    Parameters:
        names: string

GET /names?add=Eddie
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /sort-names
#    Parameters:
#       names: Adrian,Kate
#    Expected response (200 OK):
"""
Adrian, Kate
"""

# POST /sort-names
#    Parameters:
#       names: Kate,adrian
#    Expected response (200 OK):
"""
Adrian, Kate
"""

# POST /sort-names
#    Parameters:
#       names: Adrian
#    Expected response (200 OK):
"""
Adrian
"""

# POST /sort-names
#   Parameters: none
#   Expected response (400 Bad Request):
"""
Please provide a string of names
"""

# GET /names?add=Eddie
#   Expected response (200 OK)
"""
Alice, Eddie, Julia, Karim
"""

# GET /names?add=Eddie,Leo
#   Expected response (200 OK)
"""
Alice, Eddie, Julia, Karim, Leo
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /sort-names
  Parameters:
    names: Kate,Adrian
  Expected response (200 OK):
  "Adrian, Kate"
"""
def test_post_sort_name(web_client):
    response = web_client.post('/sort-names', data={'names': 'Kate,Adrian'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Adrian, Kate'

"""
POST /sort-names
  Parameters:
    names: Kate,adrian
  Expected response (200 OK):
  "Adrian, Kate"
"""
def test_post_sort_name(web_client):
    response = web_client.post('/sort-names', data={'names': 'Kate,adrian'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Adrian, Kate'

"""
POST /sort-names
  Parameters:
    names: Adrian
  Expected response (200 OK):
  "Adrian"
"""
def test_post_sort_name(web_client):
    response = web_client.post('/sort-names', data={'names': 'Adrian'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Adrian'

"""
POST /sort-names
  Parameters: ''
  Expected response 200:
  "Please enter names"
"""
def test_post_sort_name(web_client):
    response = web_client.post('/sort-names', data={'names': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Please enter names'

"""
POST /sort-names
  Parameters: none
  Expected response (400 Bad Request):
"""
def test_post_sort_name(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400

"""
GET /names?add=Eddie
  Expected response: (200 OK)
  Alice, Eddie, Julia, Karim
"""
def test_get_add_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'
```
