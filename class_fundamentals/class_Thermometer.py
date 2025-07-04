"""
Create a Thermometer class with input validation.

Requirements:
- Initialize with temperature and unit ("C" or "F")
- In __init__, validate that unit is either "C" or "F" (case-insensitive)
- If invalid unit, set to "C" as default
- Validate temperature is between -273.15°C and 1000°C (convert F to C for validation)
- If invalid temperature, set to 0
- Create method convert_to_fahrenheit() and convert_to_celsius()
- Create method get_reading() that returns formatted string

Test your class:
temp1 = Thermometer(25, "C")
temp2 = Thermometer(77, "f")  # lowercase should work
temp3 = Thermometer(-500, "C")  # should default to 0
print(temp1.get_reading())
print(temp2.convert_to_celsius())
"""

class Thermometer:
    def __init__(self, temperature, unit):
        self.unit = self._validate_unit(unit)
        self.temperature = self._validate_temp(temperature)
    
    def _validate_unit(self, unit):
        if unit.upper() in ["C", "F"]:
            return unit.upper()
        else:
            return "C"
    
    def _validate_temp(self, temperature):
        if self.unit == "F":
            temp_c = (temperature - 32) / 1.8
            if -273.15 <= temp_c <= 1000:
                return temperature
            else:
                return 32 # 0 in fahrenheit
        if self.unit == "C":
            if -273.15 <= temperature <= 1000:
                return temperature
            else:
                return 0
        else: 
            # This should never happen if _validate_unit works correctly
            raise ValueError(f"Unexpected unit: {self.unit}")
    
    def convert_to_celsius(self):
        if self.unit == "C": 
            return self.temperature
        else:
            return (self.temperature - 32) / 1.8
    
    def convert_to_fahrenheit(self):
        if self.unit == "F":
            return self.temperature
        else:
            return (self.temperature * 1.8) + 32
    
    def get_reading(self):
        return (self.temperature - 32) / 1.8

temp1 = Thermometer(25, "C")
print(temp1.get_reading())
print(temp1.convert_to_fahrenheit())

temp2 = Thermometer(77, "f")  # lowercase should work
print(temp2.get_reading())
print(temp2.convert_to_celsius())

temp3 = Thermometer(-500, "C")  # should default to 0
print(temp3.get_reading())
print(temp3.convert_to_fahrenheit())