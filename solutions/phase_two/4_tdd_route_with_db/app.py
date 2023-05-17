import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

app = Flask(__name__)


@app.route("/albums", methods=["POST"])
def post_create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    if has_missing_album_params(request.form):
        return "submit a valid title, release year and artist id", 400

    if (
        not request.form["release_year"].isnumeric()
        or len(request.form["release_year"]) != 4
    ):
        raise TypeError("release year should be an integer, four numbers in length")

    repository.create(
        Album(
            None,
            request.form["title"],
            request.form["release_year"],
            request.form["artist_id"],
        )
    )
    return "Album created successfully."


@app.route("/albums", methods=["GET"])
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(f"{album}" for album in repository.all())


@app.route("/artists", methods=["GET"])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(f"{artist}" for artist in repository.all())


@app.route("/artists", methods=["POST"])
def post_create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.create(Artist(None, request.form["name"], request.form["genre"]))
    return "Artist created successfully."


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))


def has_missing_album_params(form):
    return "title" not in form or "release_year" not in form or "artist_id" not in form
