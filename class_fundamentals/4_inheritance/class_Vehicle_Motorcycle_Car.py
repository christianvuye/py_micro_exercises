"""
Explore how class variables behave during inheritance.

Requirements:
- Create a base class `Vehicle` with a class variable `wheels = 4`.
- The `Vehicle` class should have a method `get_wheel_count()` that returns the value of the `wheels` class variable.
- Create a `Motorcycle` class that inherits from `Vehicle`.
- In the `Motorcycle` class definition, override the class variable to `wheels = 2`.
- Create a `Car` class that also inherits from `Vehicle` but does NOT override the `wheels` variable.

Test Scenario:
# Create instances of each class
car = Car()
motorcycle = Motorcycle()

print(f"A car has {car.get_wheel_count()} wheels.")
print(f"A motorcycle has {motorcycle.get_wheel_count()} wheels.")

# Now, let's change the base class variable
print("\n--- Changing base class wheels to 3 ---")
Vehicle.wheels = 3

print(f"A car now has {car.get_wheel_count()} wheels.")
print(f"A motorcycle now has {motorcycle.get_wheel_count()} wheels.")
"""


class Vehicle:
    wheels = 4

    def get_wheel_count(self):
        return self.wheels


class Motorcycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    pass


# Create instances of each class
car = Car()
motorcycle = Motorcycle()

print(f"A car has {car.get_wheel_count()} wheels.")
print(f"A motorcycle has {motorcycle.get_wheel_count()} wheels.")

# Now, let's change the base class variable
print("\n--- Changing base class wheels to 3 ---")
Vehicle.wheels = 3

print(f"A car now has {car.get_wheel_count()} wheels.")
print(f"A motorcycle now has {motorcycle.get_wheel_count()} wheels.")
