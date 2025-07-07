"""
Create a Recipe class that manages cooking information.

Requirements:
- Initialize with dish_name, prep_time_minutes, and serving_size
- Store all as instance variables
- Create a method scale_recipe(multiplier) that returns a new serving size
- Create a method get_cooking_time() that returns prep_time + 15 minutes (assumed cooking time)
- Create a method is_quick_meal() that returns True if total time <= 30 minutes

Test your class:
recipe = Recipe("Pasta", 10, 4)
print(recipe.scale_recipe(2))        # Should print 8
print(recipe.get_cooking_time())     # Should print 25
print(recipe.is_quick_meal())        # Should print True
"""

class Recipe:
    def __init__(self, dish_name, prep_time_minutes, serving_size):
        self.dish_name = dish_name
        self.prep_time_minutes = prep_time_minutes
        self.cooking_time = self.prep_time_minutes + 15
        self.serving_size = serving_size
    
    def scale_recipe(self, multiplier):
        return self.serving_size * multiplier

    def get_cooking_time(self):
        return self.cooking_time
    
    def is_quick_meal(self):
        return self.get_cooking_time() <= 30

recipe = Recipe("Pasta", 10, 4)
print(recipe.scale_recipe(2))        # Should print 8
print(recipe.get_cooking_time())     # Should print 25
print(recipe.is_quick_meal())        # Should print True