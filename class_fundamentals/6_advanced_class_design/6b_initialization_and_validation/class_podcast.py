"""
Create a Podcast class with flexible initialization.

Requirements:
- Initialize with title (required), host (default: "Unknown Host"), and duration_minutes (default: 30)
- Store all as instance variables
- Create a method get_podcast_info() that returns a formatted string like:
  "Podcast: [title] hosted by [host], Duration: [duration] minutes"

Test your class with these calls:
podcast1 = Podcast("Tech Talk")
podcast2 = Podcast("Daily News", "Sarah Chen")
podcast3 = Podcast("Deep Dive", "Alex Smith", 90)

All three should work and display appropriate information.
"""

class Podcast:
    def __init__(self, title, host="Unknown Host", duration_minutes=30):
        self.title = title
        self.host = host
        self.duration_minutes = duration_minutes
    
    def get_podcast_info(self):
        return f"Podcast: {self.title} hosted by {self.host}, Duration: {self.duration_minutes} minutes"

podcast1 = Podcast("Tech Talk")
podcast2 = Podcast("Daily News", "Sarah Chen")
podcast3 = Podcast("Deep Dive", "Alex Smith", 90)

print(podcast1.get_podcast_info())
print(podcast2.get_podcast_info())
print(podcast3.get_podcast_info())