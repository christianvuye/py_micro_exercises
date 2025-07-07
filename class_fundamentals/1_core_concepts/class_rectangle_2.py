"""
Create a class called `Rectangle` with instance variables `width` and `height`. 
Add a method `resize` that takes a scale factor and multiplies both dimensions by it.

Your task: Define Rectangle class with resize functionality
Test it with:
rect = Rectangle(10, 5)
print(rect.width, rect.height)  # Should print 10 5
rect.resize(2)
print(rect.width, rect.height)  # Should print 20 10
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def resize(self, scale_factor):
        self.width *= scale_factor
        self.height *= scale_factor

rect = Rectangle(10, 5)
print(rect.width, rect.height)  # Should print 10 5
rect.resize(2)
print(rect.width, rect.height)  # Should print 20 10