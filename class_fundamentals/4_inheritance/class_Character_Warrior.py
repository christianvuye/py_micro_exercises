"""
Practice inheritance with a game character system.

Requirements:
- Create a `Character` class with:
  - Attributes: `name`, `health` (set in __init__)
  - Method `is_alive()` that returns True if health > 0
  - Method `take_damage(amount)` that reduces health by amount

- Create a `Warrior` class that inherits from `Character`:
  - Additional attribute: `weapon` (set in __init__)
  - Inherit all Character methods WITHOUT modifying them
  - Add method `attack_power()` that returns health + 10 if weapon == "sword", else health + 5

Test Scenario:
character = Character("Basic Fighter", 100)
warrior = Warrior("Conan", 120, "sword")

print("=== Character ===")
print(f"Is alive: {character.is_alive()}")                     # Expected: True
character.take_damage(30)
print(f"Health after damage: {character.health}")              # Expected: 70

print("\n=== Warrior ===")
print(f"Is alive: {warrior.is_alive()}")                       # Expected: True
print(f"Attack power: {warrior.attack_power()}")               # Expected: 130
warrior.take_damage(50)
print(f"Health after damage: {warrior.health}")                # Expected: 70
print(f"Attack power after damage: {warrior.attack_power()}")  # Expected: 80
"""

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount

class Warrior(Character):
    def __init__(self, name, health, weapon):
        Character.__init__(self, name, health)
        self.weapon = weapon

    def attack_power(self):
        return self.health + 10 if self.weapon == "sword" else self.health + 5

character = Character("Basic Fighter", 100)
warrior = Warrior("Conan", 120, "sword")

print("=== Character ===")
print(f"Is alive: {character.is_alive()}")                     # Expected: True
character.take_damage(30)
print(f"Health after damage: {character.health}")              # Expected: 70

print("\n=== Warrior ===")
print(f"Is alive: {warrior.is_alive()}")                       # Expected: True
print(f"Attack power: {warrior.attack_power()}")               # Expected: 130
warrior.take_damage(50)
print(f"Health after damage: {warrior.health}")                # Expected: 70
print(f"Attack power after damage: {warrior.attack_power()}")  # Expected: 80