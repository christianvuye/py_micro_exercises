"""
Create a GameSession class that manages player statistics.

Requirements:
- Initialize with player_name, starting_level (default: 1), starting_score (default: 0)
- In __init__, calculate player_rank based on starting_level:
  * Level 1-10: "Beginner"
  * Level 11-25: "Intermediate" 
  * Level 26+: "Advanced"
- Create method level_up() that increases level by 1 and updates rank accordingly
- Create method add_score(points) that adds to current score
- Create method get_player_summary() that returns formatted string with all stats

Test your class:
player = GameSession("Alex", 15, 1500)
print(player.get_player_summary())  # Should show Intermediate rank
player.level_up()
player.add_score(500)
print(player.get_player_summary())  # Should show updated stats
"""

class GameSession:
    def __init__(self, player_name, starting_level=1, starting_score=0):
        self.player_name = player_name
        self.starting_level = max(1, starting_level)
        self.starting_score = max(0, starting_score)
        self.player_rank = self._calculate_rank()

    def _calculate_rank(self):        
        if 1 <= self.starting_level <= 10:
            return "Beginner"
        elif 11 <= self.starting_level <= 25:
            return "Intermediate"
        elif self.starting_level >= 26:
            return "Advanced"

    def level_up(self):
        self.starting_level += 1
        self.player_rank = self._calculate_rank()
    
    def add_score(self, points):
        self.starting_score += points
    
    def get_player_summary(self):
        return f"Player name: {self.player_name}, current level: {self.starting_level}, rank: {self.player_rank}, score: {self.starting_score}"

player = GameSession("Alex", 15, 1500)
print(player.get_player_summary())  # Should show Intermediate rank
player.level_up()
player.add_score(500)
print(player.get_player_summary())  # Should show updated stats