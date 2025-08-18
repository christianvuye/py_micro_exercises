"""
Create a Team class and Player class that work together.

Requirements for Player class:
- Initialize with name, position, and skill_level (1-10)
- Create method get_player_info() that returns formatted string

Requirements for Team class:
- Initialize with team_name and empty list of players
- Create method add_player(player) that adds a Player object to the team
- Create method remove_player(player_name) that removes player by name
- Create method get_team_average() that calculates average skill level
- Create method get_roster() that returns list of all player names

Test your classes:
player1 = Player("Alice", "Forward", 8)
player2 = Player("Bob", "Defender", 6)
team = Team("Eagles")
team.add_player(player1)
team.add_player(player2)
print(team.get_team_average())  # Should print 7.0
print(team.get_roster())        # Should print ['Alice', 'Bob']
"""


class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

    def get_player_info(self):
        return f"Name: {self.name}, position: {self.position}, skill level: {self.skill_level}"


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        for player in self.players:
            if player_name == player.name:
                self.players.remove(player)
                break  # no need to keep searching the list if the player name has been found

    def get_roster(self):
        roster = []
        for player in self.players:
            roster.append(player.name)
        return roster

    def get_team_average(self):
        average = 0
        for player in self.players:
            average += player.skill_level
        return average / len(self.players)


player1 = Player("Alice", "Forward", 8)
player2 = Player("Bob", "Defender", 6)
team = Team("Eagles")
team.add_player(player1)
team.add_player(player2)
print(team.get_team_average())  # Should print 7.0
print(team.get_roster())  # Should print ['Alice', 'Bob']

print(team.players)  # prints the objects
for player in team.players:
    print(player.name)  # This should print "Alice" then "Bob"
