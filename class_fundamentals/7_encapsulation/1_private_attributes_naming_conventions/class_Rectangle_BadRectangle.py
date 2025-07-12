"""
Practice creating private attributes to protect class data integrity.

Requirements:
- Create a `Rectangle` class with:
  - __init__ takes: `width`, `height`
  - Private attributes: `__width`, `__height` (store the parameters)
  - Public method: `get_area()` returns width * height
  - Public method: `get_dimensions()` returns a formatted string with both dimensions
  - Public method: `is_square()` returns True if width equals height

- Create a `BadRectangle` class with:
  - Same functionality but use PUBLIC attributes: `width`, `height`
  - Same methods: `get_area()`, `get_dimensions()`, `is_square()`

Test Scenario:
# Test good design with private attributes
good_rect = Rectangle(5, 3)
print(good_rect.get_area())           # Expected: 15
print(good_rect.get_dimensions())     # Expected: "Width: 5, Height: 3"
print(good_rect.is_square())          # Expected: False

# Test what happens with public attributes
bad_rect = BadRectangle(4, 4)
print(bad_rect.get_area())            # Expected: 16
print(bad_rect.is_square())           # Expected: True

# Now break the bad rectangle
bad_rect.width = -10                  # Oops! Invalid state
print(bad_rect.get_area())            # Expected: -40 (nonsensical!)

# Try to break the good rectangle
# good_rect.__width = -10             # Expected: Won't affect internal state due to name mangling
"""

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__height * self.__width
    
    def get_dimensions(self):
        return f"Height: {self.__height}, Width: {self.__width}"

    def is_square(self):
        return self.__height == self.__width

class BadRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_dimensions(self):
        return f"Height: {self.height}, Width: {self.width}"

    def is_square(self):
        return self.height == self.width
    
# Test good design with private attributes
good_rect = Rectangle(5, 3)
print(good_rect.get_area())           # Expected: 15
print(good_rect.get_dimensions())     # Expected: "Width: 5, Height: 3"
print(good_rect.is_square())          # Expected: False

# Test what happens with public attributes
bad_rect = BadRectangle(4, 4)
print(bad_rect.get_area())            # Expected: 16
print(bad_rect.is_square())           # Expected: True

# Now break the bad rectangle
bad_rect.width = -10                  # Oops! Invalid state
print(bad_rect.get_area())            # Expected: -40 (nonsensical!) (negative area does not exist, but this could be fixed with validation)

"""
# Try to break the good rectangle
good_rect.__width = -10             # Expected: Won't affect internal state due to name mangling 
                                    # Why doesn't this raise an AttributeError?

The key difference is between reading vs writing private attributes:
    Reading (accessing) a private attribute from outside → AttributeError
    Writing (setting) a private attribute from outside → Creates a NEW attribute!
"""

# After running your code, try this:
print("Before assignment:")
print([attr for attr in dir(good_rect) if 'width' in attr])

good_rect.__width = -10  # This creates a NEW attribute!

print("After assignment:")
print([attr for attr in dir(good_rect) if 'width' in attr])
print(f"Internal width (still protected): {good_rect._Rectangle__width}") # type: ignore
print(f"New external width: {good_rect.__width}")
print(f"get_area() still works correctly: {good_rect.get_area()}")

try:
    print(good_rect.__width)  # This works (reads the new attribute we just created)
    print(good_rect.__height)  # This will raise AttributeError (never created)
except AttributeError as e:
    print(f"Error: {e}")