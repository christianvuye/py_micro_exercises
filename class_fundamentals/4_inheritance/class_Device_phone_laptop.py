"""
Practice automatic constructor inheritance with electronics.

Requirements:
- Create a `Device` class with:
  - Attributes: `brand`, `price` (set in __init__)
  - Method `get_info()` that returns "{brand} device costs ${price}"

- Create a `Phone` class that inherits from `Device`:
  - DO NOT define __init__ (inherit automatically)
  - Add method `call(number)` that returns "Calling {number} from {brand} phone"

- Create a `Laptop` class that inherits from `Device`:
  - DO NOT define __init__ (inherit automatically)
  - Add method `boot_up()` that returns "{brand} laptop is starting up..."

Test Scenario:
phone = Phone("Apple", 999)       # Uses Device.__init__ automatically!
laptop = Laptop("Dell", 1299)     # Uses Device.__init__ automatically!

print("=== Phone ===")
print(phone.get_info())           # Expected: "Apple device costs $999"
print(phone.call("555-1234"))     # Expected: "Calling 555-1234 from Apple phone"

print("\n=== Laptop ===")
print(laptop.get_info())          # Expected: "Dell device costs $1299" 
print(laptop.boot_up())           # Expected: "Dell laptop is starting up..."
"""

class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def get_info(self):
        return f"{self.brand} device costs ${self.price}"

class Phone(Device):
    def call(self, number):
        # self.number = number not sure if needed, but otherwise this Phone class has absolutely zero unique attributes
        return f"Calling {number} from {self.brand} phone"
    
class Laptop(Device):
    def boot_up(self):
        return f"{self.brand} laptop is starting up..."
    
# Test Scenario:
phone = Phone("Apple", 999)       # Uses Device.__init__ automatically!
laptop = Laptop("Dell", 1299)     # Uses Device.__init__ automatically!

print("=== Phone ===")
print(phone.get_info())           # Expected: "Apple device costs $999"
print(phone.call("555-1234"))     # Expected: "Calling 555-1234 from Apple phone"

print("\n=== Laptop ===")
print(laptop.get_info())          # Expected: "Dell device costs $1299" 
print(laptop.boot_up())           # Expected: "Dell laptop is starting up..."