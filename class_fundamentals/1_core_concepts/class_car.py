"""
Create a class called `Car` that takes `make`, `model`, and `year` in its `__init__` method. 
Add a method called `get_info` that returns a formatted string with all the car information.

Your task: Define the Car class with get_info method
Test it with:
car = Car("Toyota", "Camry", 2020)
print(car.get_info())  # Should print "2020 Toyota Camry"
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

car = Car("Toyota", "Camry", 2020)
print(car.get_info())  # Should print "2020 Toyota Camry"