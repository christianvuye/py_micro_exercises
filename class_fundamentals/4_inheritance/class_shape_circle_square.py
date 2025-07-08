"""
Learn when child classes can automatically inherit parent constructors.

Requirements:
- Create a `Shape` class with:
  - Attributes: `color`, `size` (set in __init__)
  - Method `describe()` that returns "A {color} shape of size {size}"

- Create a `Circle` class that inherits from `Shape`:
  - DO NOT define __init__ (let it inherit automatically)
  - Add method `area()` that returns size * size * 3.14

- Create a `Square` class that inherits from `Shape`:
  - DO NOT define __init__ (let it inherit automatically)
  - Add method `perimeter()` that returns size * 4

Test Scenario:
circle = Circle("red", 5)        # Uses Shape.__init__ automatically!
square = Square("blue", 4)       # Uses Shape.__init__ automatically!

print("=== Circle ===")
print(circle.describe())         # Expected: "A red shape of size 5"
print(f"Area: {circle.area()}")  # Expected: 78.5

print("\n=== Square ===")
print(square.describe())         # Expected: "A blue shape of size 4"
print(f"Perimeter: {square.perimeter()}")  # Expected: 16
"""

class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    def describe(self):
        return f"A {self.color} shape of size {self.size}"
    
class Circle(Shape):
    def area(self):
        return self.size * self.size * 3.14

class Square(Shape):
    def perimeter(self):
        return self.size * 4 
    
# Tests
circle = Circle("red", 5)        # Uses Shape.__init__ automatically!
square = Square("blue", 4)       # Uses Shape.__init__ automatically!

print("=== Circle ===")
print(circle.describe())         # Expected: "A red shape of size 5"
print(f"Area: {circle.area()}")  # Expected: 78.5

print("\n=== Square ===")
print(square.describe())         # Expected: "A blue shape of size 4"
print(f"Perimeter: {square.perimeter()}")  # Expected: 16