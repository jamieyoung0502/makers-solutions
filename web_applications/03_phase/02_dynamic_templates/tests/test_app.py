from playwright.sync_api import Page, expect
import pytest

"""
We can get an emoji from the /emoji page
"""


# def test_get_emoji(page, test_web_address):  # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")


# def test_get_goodbye(page, test_web_address):
#     page.goto(f"http://{test_web_address}/goodbye")
#     strong_tag = page.locator("strong")
#     expect(strong_tag).to_have_text("Bye!")


def test_get_albums(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    titles = page.locator(".album_title")
    years = page.locator(".album_year")

    expect(titles).to_have_text(
        [
            "Title: Midnights",
            "Title: reputation",
            "Title: Going Blue",
            "Title: folklore",
        ]
    )

    expect(years).to_have_text(
        [
            "Release Date: 2022",
            "Release Date: 2017",
            "Release Date: 2019",
            "Release Date: 2020",
        ]
    )


def test_get_single_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/album/1")
    title = page.locator(".album_title")
    year = page.locator(".album_year")
    artist = page.locator(".artist")
    expect(title).to_have_text("Title: Midnights")
    expect(year).to_have_text("Release Date: 2022")
    expect(artist).to_have_text("Artist: Taylor Swift")


def test_click_album_link(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Midnights by Taylor Swift'")
    title = page.locator(".album_title")
    year = page.locator(".album_year")
    artist = page.locator(".artist")
    expect(title).to_have_text("Title: Midnights")
    expect(year).to_have_text("Release Date: 2022")
    expect(artist).to_have_text("Artist: Taylor Swift")
