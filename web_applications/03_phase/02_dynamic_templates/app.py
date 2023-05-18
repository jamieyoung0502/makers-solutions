import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

app = Flask(__name__)


@app.route("/emoji", methods=["GET"])
def get_emoji():
    return render_template("emoji.html", emoji=":)")


@app.route("/goodbye", methods=["GET"])
def get_goodbye():
    return render_template("goodbye.html", goodbye="Bye!")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
