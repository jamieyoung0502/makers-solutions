## Describe the Problem

> As a user
> So that I can keep track of my music listening
> I want to add tracks I've listened to and see a list of them.

## Design the Class Interface

```python
class Spotify:
    # User-facing properties:
    #   name: string
    def __init__(self, name_of_playlist):
        # Parameters:
        #   name_of_playlist: string
        #   tracks: dictionary
        # Side effects:
        #   Creates a dictionary associated with the object into which we will save a track (key) and its artist and date added (values)
        #   e.g. { "rock" : { "don't stop me now" : { "artist" : "queen", "added" : datetime.utcnow()}}}
        pass # No code here yet

    def add_track(self, track, artist):
        # Parameters:
        #   track: string
        #   artist: string
        # Returns:
        #   Nothing
        # Side effects:
        #   add track to dictionary, and call list all tracks to show dictionary has been updated
        pass

    def list_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   tuples within list: List of all tracks and artists associated with the playlist
        # Side effects:
        #   Does not add empty strings to playlist; throw an error if wrong data type given
        pass
```

## Example tests

```python

"""
Initially, there are no tracks
# show an empty list
"""
playlist = Spotify("techno")
playlist.list_tracks() # => []

"""
Given an empty string
# there is no change to the playlist
"""

playlist = Spotify("techno")
playlist.add_track("", "")
playlist.list_tracks() # => []

"""
Given an track
# playlist is updated and is reflected in the list of tracks
"""

playlist = Spotify("rock")
playlist.add_track("don't stop me now", "queen")
playlist.list_tracks() # => [("don't stop me now", "queen")]


"""
Given an track
# playlist is updated with more than one track which are reflected in the list of tracks, with the most recent being first
"""

playlist = Spotify("rock")
playlist.add_track("don't stop me now", "queen")
playlist.add_track("back in black", "acdc")
playlist.list_tracks() # => [("back in black", "acdc"), ("don't stop me now", "queen")]
```
