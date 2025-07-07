"""
Practice the inheritance pattern with vehicles.

Requirements:
- Create a `Vehicle` class with:
  - Attributes: `make`, `year` (set in __init__)
  - Method `get_info()` that returns "{year} {make}"
  - Method `is_vintage()` that returns True if year < 2000, False otherwise

- Create a `Car` class that inherits from `Vehicle`:
  - Additional attribute: `doors` (set in __init__)
  - Inherit all Vehicle methods WITHOUT modifying them
  - Add method `describe_car()` that returns "{year} {make} with {doors} doors"

Test Scenario:
vehicle = Vehicle("Ford", 1995)
car = Car("Toyota", 2021, 4)

print("=== Vehicle ===")
print(vehicle.get_info())
print(f"Is vintage: {vehicle.is_vintage()}")

print("\n=== Car ===")
print(car.get_info())  # Should work automatically!
print(f"Is vintage: {car.is_vintage()}")  # Should work automatically!
print(car.describe_car())  # New method
"""

class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make}"

    def is_vintage(self):
        return self.year < 2000
    
class Car(Vehicle):
    def __init__(self, make, year, doors):
        Vehicle.__init__(self, make, year)
        self.doors = doors
    
    def describe_car(self):
        return f"{self.year} {self.make} with {self.doors} doors"
    
vehicle = Vehicle("Ford", 1995)
car = Car("Toyota", 2021, 4)

print("=== Vehicle ===")
print(vehicle.get_info())
print(f"Is vintage: {vehicle.is_vintage()}")

print("\n=== Car ===")
print(car.get_info())  # Should work automatically!
print(f"Is vintage: {car.is_vintage()}")  # Should work automatically!
print(car.describe_car())  # New method