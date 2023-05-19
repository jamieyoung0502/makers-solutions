from playwright.sync_api import Page, expect
import pytest


def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/albums")
    titles = page.locator(".album_title")
    years = page.locator(".album_year")

    expect(titles).to_have_text(
        ["Title: Midnights", "Title: reputation", "Title: Going Blue"]
    )

    expect(years).to_have_text(
        ["Release Date: 2022", "Release Date: 2017", "Release Date: 2019"]
    )


def test_get_single_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    title = page.locator(".album_title")
    year = page.locator(".album_year")
    artist = page.locator(".album_artist")
    expect(title).to_have_text("Title: Midnights")
    expect(year).to_have_text("Release Date: 2022")
    expect(artist).to_have_text("Artist: Taylor Swift")


def test_click_album_link(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Midnights by Taylor Swift'")
    title = page.locator(".album_title")
    year = page.locator(".album_year")
    artist = page.locator(".album_artist")
    expect(title).to_have_text("Title: Midnights")
    expect(year).to_have_text("Release Date: 2022")
    expect(artist).to_have_text("Artist: Taylor Swift")


"""
When I go to /artists/1
I see the name and genre of the given artist:
Name: Taylor Swift
Genre: Pop
"""


def test_get_single_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    name = page.locator(".name")
    genre = page.locator(".genre")
    expect(name).to_have_text("Name: Taylor Swift")
    expect(genre).to_have_text("Genre: Pop")


"""
When I go to /artists
I see a list of all of the artists
["Name: Taylor Swift", "Name: Victoria Bigelow"]
["Genre: Pop", "Genre: Mopey"]
"""


def test_get_all_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/artists")
    names = page.locator(".name")
    genres = page.locator(".genre")
    expect(names).to_have_text(["Name: Taylor Swift", "Name: Victoria Bigelow"])
    expect(genres).to_have_text(["Genre: Pop", "Genre: Mopey"])


"""
We go to the /artists page
And we click on a link "Taylor Swift"
We go to the artist's page
I see the name and genre of the given artist:
Name: Taylor Swift
Genre: Pop
"""


def test_artist_link(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Taylor Swift'")
    name = page.locator(".name")
    genre = page.locator(".genre")
    expect(name).to_have_text("Name: Taylor Swift")
    expect(genre).to_have_text("Genre: Pop")


"""
When we create a new album
We see it in the albums index
"""


def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/spotify.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add Album")
    page.fill("input[name='title']", "The Best Of")
    page.fill("input[name='release_year']", "2023")
    page.get_by_label("artist").select_option("Taylor Swift")
    page.click("text=Create Album")

    title = page.locator(".album_title")
    year = page.locator(".album_year")
    artist = page.locator(".album_artist")

    expect(title).to_have_text("Title: The Best Of")
    expect(year).to_have_text("Release Date: 2023")
    expect(artist).to_have_text("Artist: Taylor Swift")
