"""
Practice inheritance with both class attributes and instance attributes.

Requirements:
- Create a `Food` class with:
  - Class attribute: `nutrition_database = {"protein": 20, "carbs": 30, "fat": 10}`
  - Instance attributes: `name`, `calories` (set in __init__)
  - Method `describe()` that returns "{name} has {calories} calories"
  - Method `get_nutrition(nutrient)` that returns nutrition_database[nutrient]

- Create a `Fruit` class that inherits from `Food`:
  - Class attribute: `category = "healthy"`
  - DO NOT define __init__ (inherit automatically)
  - Add method `health_benefit()` that returns "{name} is {category} and provides vitamins"

- Create a `Dessert` class that inherits from `Food`:
  - Class attribute: `category = "treat"`
  - DO NOT define __init__ (inherit automatically)
  - Add method `indulgence_level()` that returns "high" if calories > 300, else "moderate"

Test Scenario:
fruit = Fruit("Apple", 95)
dessert = Dessert("Chocolate Cake", 450)

print("=== Fruit ===")
print(fruit.describe())                    # Expected: "Apple has 95 calories"
print(fruit.health_benefit())              # Expected: "Apple is healthy and provides vitamins"
print(f"Protein content: {fruit.get_nutrition('protein')}")  # Expected: 20

print("\n=== Dessert ===")
print(dessert.describe())                  # Expected: "Chocolate Cake has 450 calories"
print(f"Indulgence: {dessert.indulgence_level()}")  # Expected: "high"
print(f"Category: {dessert.category}")     # Expected: "treat"
"""

class Food:
    nutrition_database = {"protein": 20, "carbs": 30, "fat": 10}

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories # calories should be calculated from protein, carbs and fat and not seperately provided
    
    def describe(self):
        return f"{self.name} has {self.calories} calories"
    
    def get_nutrition(self, nutrient):
        return Food.nutrition_database[nutrient]
    
class Fruit(Food):
    category = "healthy"

    def health_benefit(self):
        return f"{self.name} is {self.category} and provides vitamins"
    
class Dessert(Food):
    category = "treat"

    def indulgence_level(self):
        return "high" if self.calories > 300 else "moderate"

# Test Scenario:
fruit = Fruit("Apple", 95)
dessert = Dessert("Chocolate Cake", 450)

print("=== Fruit ===")
print(fruit.describe())                    # Expected: "Apple has 95 calories"
print(fruit.health_benefit())              # Expected: "Apple is healthy and provides vitamins"
print(f"Protein content: {fruit.get_nutrition('protein')}")  # Expected: 20

print("\n=== Dessert ===")
print(dessert.describe())                  # Expected: "Chocolate Cake has 450 calories"
print(f"Indulgence: {dessert.indulgence_level()}")  # Expected: "high"
print(f"Category: {dessert.category}")     # Expected: "treat"
