"""
Create a class called `Circle` that takes a `radius` parameter. 
Add methods `area` and `circumference` that calculate and return the respective values.
Use 3.14159 for pi.

Your task: Define the Circle class with area and circumference methods
Test it with:
circle = Circle(5)
print(circle.area())         # Should print 78.53975
print(circle.circumference()) # Should print 31.4159
"""

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi*(self.radius**2)

    def circumference(self):
        return 2 * pi * self.radius

circle = Circle(5)
print(circle.area())         # Should print 78.53975
print(circle.circumference()) # Should print 31.4159