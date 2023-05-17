from lib.spotify import Spotify

"""
Initially, there are no tracks
# show an empty list
"""

def test_spotify_initially_no_tracks():
    playlist = Spotify("techno")
    actual = playlist.list_tracks()
    expected = []
    assert expected == actual


"""
Given an empty string
# there is no change to the playlist
"""

def test_spotify_empty_string_does_not_update_list():
    playlist = Spotify("techno")
    playlist.add_track("", "")
    actual = playlist.list_tracks()
    expected = []
    assert expected == actual

"""
Given an track
# playlist is updated and is reflected in the list of tracks
"""

def test_spotify_adding_single_track_reflected_in_list():
    playlist = Spotify("rock")
    playlist.add_track("don't stop me now", "queen")
    actual = playlist.list_tracks()
    expected = [("don't stop me now", "queen")]
    assert expected == actual

"""
Given multiple tracks
# playlist is updated with more than one track which are reflected in the list of tracks, with the most recent being first
"""

def test_spotify_adding_multiple_tracks_reflected_in_list_most_recent_first():
    playlist = Spotify("rock")
    playlist.add_track("don't stop me now", "queen")
    playlist.add_track("back in black", "acdc")
    actual = playlist.list_tracks()
    expected = [("back in black", "acdc"), ("don't stop me now", "queen")]
    assert expected == actual

"""
Given multiple tracks with the same name
# playlist is updated with more than one track which are reflected in the list of tracks, with the most recent being first
"""

def test_spotify_adding_multiple_tracks_with_same_track_are_both_added():
    playlist = Spotify("rock")
    playlist.add_track("don't stop me now", "queen")
    playlist.add_track("don't stop me now", "acdc")
    actual = playlist.list_tracks()
    expected = [("don't stop me now", "acdc"), ("don't stop me now", "queen")]
    assert expected == actual