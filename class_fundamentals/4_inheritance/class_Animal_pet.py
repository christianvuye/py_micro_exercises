"""
Practice the same inheritance pattern with animals.

Requirements:
- Create an `Animal` class with:
  - Attributes: `species`, `age` (set in __init__)
  - Method `describe()` that returns "I am a {respecies}, {age} years old"
  - Method `is_adult()` that returns True if age >= 2, False otherwise

- Create a `Pet` class that inherits from `Animal`:
  - Additional attribute: `owner_name` (set in __init__)
  - Inherit all Animal methods WITHOUT modifying them
  - Add method `show_owner()` that returns "{species} belongs to {owner_name}"

Test Scenario:
animal = Animal("Wolf", 5)
pet = Pet("Dog", 3, "Sarah")

print("=== Animal ===")
print(animal.describe())
print(f"Is adult: {animal.is_adult()}")

print("\n=== Pet ===")
print(pet.describe())  # Should work automatically!
print(f"Is adult: {pet.is_adult()}")  # Should work automatically!
print(pet.show_owner())  # New method
"""

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def describe(self):
        return f"I am a {self.species}, {self.age} years old"
    
    def is_adult(self):
        return self.age >= 2

class Pet(Animal):
    def __init__(self, species, age, owner_name):
        Animal.__init__(self, species, age)
        self.owner_name = owner_name
    
    def show_owner(self):
        return f"{self.species} belongs to {self.owner_name}"


animal = Animal("Wolf", 5)
pet = Pet("Dog", 3, "Sarah")

print("=== Animal ===")
print(animal.describe())
print(f"Is adult: {animal.is_adult()}")

print("\n=== Pet ===")
print(pet.describe())  # Should work automatically!
print(f"Is adult: {pet.is_adult()}")  # Should work automatically!
print(pet.show_owner())  # New method