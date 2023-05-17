from datetime import datetime

class Spotify():

    def __init__(self, name_of_playlist):
        self._name = name_of_playlist
        self._tracks = { self._name : {} }

    def list_tracks(self):
        if self._tracks != { self._name : {}}:
            tracks = [
                (self._tracks[playlist][artist]['track'], artist)
                for playlist in self._tracks
                for artist in self._tracks[playlist].keys()
            ]
            return sorted(tracks, key=lambda track: self._tracks[self._name][track[1]]['added'], reverse=True)
        else:
            return []

    def add_track(self, track, artist):
        if track != "" and artist != "":
            self._tracks[self._name].update(
                { artist : {"track" : track,
                    "added" : datetime.utcnow()
                    }
                })