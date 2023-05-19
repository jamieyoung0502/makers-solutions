import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

app = Flask(__name__)


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    return render_template(
        "albums/index.html",
        albums=album_repository.all(),
        artists=artist_repository.all(),
    )


@app.route("/albums/<int:id>")
def get_single_album(id):
    album_id = id
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(album_id)
    return render_template(
        "albums/show.html",
        album=album_repository.find(album_id),
        artist=artist_repository.find(album.artist_id),
    )


@app.route("/artists/<int:id>")
def get_single_artist(id):
    artist_id = id
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    return render_template(
        "artists/show.html", artist=artist_repository.find(artist_id)
    )


@app.route("/artists")
def get_all_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    return render_template("artists/index.html", artists=artist_repository.all())


@app.route("/albums/new")
def get_new_album():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    return render_template("albums/new.html", artists=artist_repository.all())


@app.route("/albums", methods=["POST"])
def post_new_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    title = request.form["title"]
    release_year = request.form["release_year"]
    artist_id = request.form["artist"]
    album = Album(None, title, release_year, artist_id)

    if not album.is_valid():
        return (
            render_template(
                "albums/new.html", album=album, errors=album.generate_errors()
            ),
            400,
        )

    album = album_repository.create(album)
    return redirect(f"/albums/{album.id}")


@app.route("/artists/new")
def get_new_artist():
    return render_template("artists/new.html")


@app.route("/artists", methods=["POST"])
def post_new_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    name = request.form["name"]
    genre = request.form["genre"]
    artist = Artist(None, name, genre)

    if not artist.is_valid():
        return (
            render_template(
                "albums/new.html", album=album, errors=album.generate_errors()
            ),
            400,
        )

    artist = artist_repository.create(artist)
    return redirect(f"/artists/{artist.id}")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
