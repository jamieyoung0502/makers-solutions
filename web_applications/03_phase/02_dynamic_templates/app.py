import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album

app = Flask(__name__)


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    return render_template(
        "albums.html", albums=album_repository.all(), artists=artist_repository.all()
    )


@app.route("/albums/<int:id>")
def get_single_album(id):
    album_id = id
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(album_id)
    return render_template(
        "album.html",
        album=album_repository.find(album_id),
        artist=artist_repository.find(album.artist_id),
    )


@app.route("/artists/<int:id>")
def get_single_artist(id):
    artist_id = id
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    return render_template("artist.html", artist=artist_repository.find(artist_id))


@app.route("/artists")
def get_all_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    return render_template("artists.html", artists=artist_repository.all())


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
