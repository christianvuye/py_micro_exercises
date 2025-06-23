"""
Your task: Define the Rectangle class with area method
Test it with:
rect = Rectangle(5, 3)
print(rect.area())  # Should print 15
"""

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width