"""
Create a class called `Calculator` with methods `add`, `subtract`, `multiply`, and `divide`. 
Each method should take two parameters and return the result.

Your task: Define the Calculator class with arithmetic methods
Test it with:
calc = Calculator()
print(calc.add(5, 3))      # Should print 8
print(calc.subtract(10, 4)) # Should print 6
print(calc.multiply(3, 7))  # Should print 21
print(calc.divide(15, 3))   # Should print 5.0
"""

class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
calc = Calculator()
print(calc.add(5, 3))      # Should print 8
print(calc.subtract(10, 4)) # Should print 6
print(calc.multiply(3, 7))  # Should print 21
print(calc.divide(15, 3))   # Should print 5.0