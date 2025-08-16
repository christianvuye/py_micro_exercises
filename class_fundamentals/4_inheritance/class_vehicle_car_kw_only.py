"""
Master flexible constructors with keyword-only arguments and complex defaults.

Requirements:
- Create a `Vehicle` class with:
  - Required: `make`, `model`
  - Optional: `year` (default: 2024), `color` (default: "white"), `mileage` (default: 0)
  - Validate: year between 1900-2025, mileage >= 0
  - Method `get_summary()` returning formatted vehicle info

- Create a `Car` class that inherits from `Vehicle`:
  - EXTEND parent constructor
  - Add optional: `doors` (default: 4), `fuel_type` (default: "gasoline")
  - Force year to be >= 2000 (override parent's range)
  - Validate: doors must be 2 or 4, fuel_type must be "gasoline", "hybrid", or "electric"
  - OVERRIDE get_summary() to include car-specific details

# Test various initialization patterns
basic_vehicle = Vehicle("Toyota", "Camry")
custom_vehicle = Vehicle("Ford", "F-150", year=2022, color="blue", mileage=15000)
basic_car = Car("Honda", "Civic")
custom_car = Car("Tesla", "Model 3", year=2023, color="red", doors=4, fuel_type="electric")

print(basic_vehicle.get_summary())    # Expected: Toyota Camry with defaults
print(custom_vehicle.get_summary())   # Expected: Ford F-150 with custom values
print(basic_car.get_summary())        # Expected: Honda Civic with car defaults
print(custom_car.get_summary())       # Expected: Tesla Model 3 with all custom values
"""


class Vehicle:
    def __init__(self, make, model, year=2024, color="white", mileage=0):
        self.make = make
        self.model = model
        self.year = self._validate_year(
            year
        )  # using self here bcse the static method is a part of the class
        # self.year = Vehicle._validate_year(year) # not sure which one is preferred?
        # using the class makes it more explicit that its a part of the class and that it is not being called on an instance?
        self.color = color
        self.mileage = self._validate_mileage(mileage)

    @staticmethod  # static method so its not tied to a vehicle instance
    def _validate_year(year):
        # could use range here instead of hard coding but not worth the hassle atm
        if not (1900 <= year <= 2025):
            raise ValueError(f"{year} should be between 1900 and 2025")
        else:
            return year

    @staticmethod
    def _validate_mileage(mileage):
        if (
            not mileage >= 0
        ):  # no reason for storing zero in a variable, mileage won't change and can't logically be under 0
            raise ValueError("Mileage cannot be negative.")
        else:
            return mileage

    def get_summary(self):
        return f"Vehicle, make: {self.make}, model: {self.model}, year: {self.year}, color: {self.color}, mileage: {self.mileage}"


class Car(Vehicle):
    def __init__(
        self,
        make,
        model,
        year=2024,
        color="white",
        mileage=0,
        doors=4,
        fuel_type="gasoline",
    ):
        year = Car._validate_year(
            year
        )  # better to explicitely call Car prefix to make clear it is static method of Car not Vehicle class
        Vehicle.__init__(self, make, model, year, color, mileage)
        self.doors = self._validate_doors(doors)
        self.fuel_type = self._validate_fuel_type(fuel_type)

    @staticmethod
    def _validate_year(year):
        year_cutoff = 2000  # avoid hardcoding magic numbers
        if not year >= year_cutoff:
            raise ValueError(f"Year shoud be {year_cutoff} or later")
        else:
            return year

    @staticmethod
    def _validate_doors(doors):
        allowed_doors = [2, 4]
        if doors not in allowed_doors:
            raise ValueError(f"Car must have {allowed_doors} doors.")
        else:
            return doors

    @staticmethod
    def _validate_fuel_type(fuel_type):
        allowed_fuel_types = ["gasoline", "hybrid", "electric"]
        if fuel_type not in allowed_fuel_types:
            raise ValueError(f"Fuel type must be {allowed_fuel_types}")
        else:
            return fuel_type

    def get_summary(self):
        return (
            f"Vehicle, make: {self.make}, model: {self.model}, "
            f"year: {self.year}, color: {self.color}, "
            f"mileage: {self.mileage}, doors: {self.doors}, "
            f"fuel_type: {self.fuel_type}"
        )


# Test various initialization patterns
basic_vehicle = Vehicle("Toyota", "Camry")
custom_vehicle = Vehicle("Ford", "F-150", year=2022, color="blue", mileage=15000)
basic_car = Car("Honda", "Civic")
custom_car = Car(
    "Tesla", "Model 3", year=2023, color="red", doors=4, fuel_type="electric"
)

print(basic_vehicle.get_summary())  # Expected: Toyota Camry with defaults
print(custom_vehicle.get_summary())  # Expected: Ford F-150 with custom values
print(basic_car.get_summary())  # Expected: Honda Civic with car defaults
print(custom_car.get_summary())  # Expected: Tesla Model 3 with all custom values
