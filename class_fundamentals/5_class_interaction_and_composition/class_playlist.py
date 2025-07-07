"""
Create a Playlist class that manages music tracks.

Requirements:
- Initialize with playlist_name and an empty list of tracks
- Create method add_track(track_name) that adds a track to the list
- Create method remove_track(track_name) that removes a track if it exists
- Create method get_track_count() that returns number of tracks
- Create method is_empty() that returns True if no tracks exist

Test your class:
playlist = Playlist("My Favorites")
playlist.add_track("Song A")
playlist.add_track("Song B")
print(playlist.get_track_count())  # Should print 2
print(playlist.is_empty())         # Should print False
playlist.remove_track("Song A")
print(playlist.get_track_count())  # Should print 1
"""

class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.tracks = []
    
    def add_track(self, track_name):
        self.tracks.append(track_name)
    
    def remove_track(self, track_name):
        if track_name in self.tracks:
            self.tracks.remove(track_name)
        else:
            print(f"{track_name} is not in the playlist")
    
    def get_track_count(self):
        return len(self.tracks)

    def is_empty(self):
        return len(self.tracks) == 0

playlist = Playlist("My Favorites")
playlist.add_track("Song A")
playlist.add_track("Song B")
print(playlist.get_track_count())  # Should print 2
print(playlist.is_empty())         # Should print False
playlist.remove_track("Song A")
print(playlist.get_track_count())  # Should print 1