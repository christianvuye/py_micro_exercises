"""
Create a class called `Temperature` that stores a temperature in Celsius. 
Add methods `to_fahrenheit` and `to_kelvin` that return the converted temperatures.

Your task: Define the Temperature class with conversion methods
Test it with:
temp = Temperature(25)
print(temp.to_fahrenheit())  # Should print 77.0
print(temp.to_kelvin())      # Should print 298.15
"""

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15

temp = Temperature(25)
print(temp.to_fahrenheit())  # Should print 77.0
print(temp.to_kelvin())      # Should print 298.15