import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album

app = Flask(__name__)


@app.route("/emoji", methods=["GET"])
def get_emoji():
    return render_template("emoji.html", emoji=":)")


@app.route("/goodbye", methods=["GET"])
def get_goodbye():
    return render_template("goodbye.html", goodbye="Bye!")


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    return render_template(
        "albums.html", albums=album_repository.all(), artists=artist_repository.all()
    )


@app.route("/album/<int:id>")
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


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
