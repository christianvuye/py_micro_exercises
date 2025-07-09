"""
Learn to extend parent constructors with validation and conditional initialization.

Requirements:
- Create a `Vehicle` class with:
  - Attributes: `make`, `model`, `year` (set in __init__)
  - Validate: year must be between 1900 and 2025, raise ValueError if not
  - Method `basic_info()` that returns "{year} {make} {model}"

- Create a `Car` class that inherits from `Vehicle`:
  - Additional attributes: `doors`, `fuel_type`
  - EXTEND parent constructor with validation
  - Validate: doors must be 2 or 4, fuel_type must be in ["gas", "electric", "hybrid"]
  - Conditionally set `is_eco_friendly` based on fuel_type
  - Add method `car_details()` that returns basic info + door/fuel info

- Create a `ElectricCar` class that inherits from `Car`:
  - Additional attributes: `battery_capacity`, `charging_time`
  - EXTEND Car constructor (not Vehicle directly!)
  - Force fuel_type to always be "electric" regardless of input
  - Validate: battery_capacity must be > 0
  - Add method `charging_info()` that returns battery and charging details

Test Scenario:
car = Car("Toyota", "Camry", 2020, 4, "gas")
electric = ElectricCar("Tesla", "Model 3", 2023, 4, "gas", 75, 8)  # Note: "gas" will be forced to "electric"

print("=== Car ===")
print(car.basic_info())           # Expected: "2020 Toyota Camry"
print(car.car_details())          # Expected: includes door/fuel info
print(f"Eco friendly: {car.is_eco_friendly}")  # Expected: False

print("\n=== Electric Car ===")
print(electric.basic_info())      # Expected: "2023 Tesla Model 3"
print(f"Fuel type: {electric.fuel_type}")      # Expected: "electric" (forced)
print(f"Eco friendly: {electric.is_eco_friendly}")  # Expected: True
print(electric.charging_info())   # Expected: battery/charging details
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = self._validate_year(year)
    
    @staticmethod
    def _validate_year(year):
        if not (1900 <= year <= 2025):
            raise ValueError(f"{year} is not between 1900 and 2025")
        else: 
            return year
    
    def basic_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        Vehicle.__init__(self, make, model, year)
        self.doors = self._validate_doors(doors)
        self.fuel_type = self._validate_fuel_type(fuel_type)
    
    @staticmethod
    def _validate_doors(doors):
        if doors not in [2 ,4]:
            raise ValueError(f"{doors} is not 2 or 4")
        else:
            return doors
    
    @staticmethod
    def _validate_fuel_type(fuel_type):
        if fuel_type not in ["gas", "electric", "hybrid"]:
            raise ValueError(f"{fuel_type} is either gas, electric or hybrid")
        else:
            return fuel_type
    
    @property
    def is_eco_friendly(self):
        return self.fuel_type in ["electric", "hybrid"]
    
    def car_details(self):
        return f"{self.make} {self.model} {self.year} {self.doors} {self.fuel_type}"    

        
class ElectricCar(Car):
    def __init__(self, make, model, year, doors, fuel_type, battery_capacity, charging_time):
        Car.__init__(self, make, model, year, doors, fuel_type="electric")
        self.battery_capacity = self._validate_battery_capacity(battery_capacity)
        self.charging_time = charging_time
    
    @staticmethod
    def _validate_battery_capacity(battery_capacity):
        if not battery_capacity > 0:
            raise ValueError(f"{battery_capacity} has to be above 0")
        else:
            return battery_capacity
    
    def charging_info(self):
        return f"{self.battery_capacity} {self.charging_time}"

# Test Scenario:
car = Car("Toyota", "Camry", 2020, 4, "gas")
electric = ElectricCar("Tesla", "Model 3", 2023, 4, "gas", 75, 8)  # Note: "gas" will be forced to "electric"

print("=== Car ===")
print(car.basic_info())           # Expected: "2020 Toyota Camry"
print(car.car_details())          # Expected: includes door/fuel info
print(f"Eco friendly: {car.is_eco_friendly}")  # Expected: False

print("\n=== Electric Car ===")
print(electric.basic_info())      # Expected: "2023 Tesla Model 3"
print(f"Fuel type: {electric.fuel_type}")      # Expected: "electric" (forced)
print(f"Eco friendly: {electric.is_eco_friendly}")  # Expected: True
print(electric.charging_info())   # Expected: battery/charging details