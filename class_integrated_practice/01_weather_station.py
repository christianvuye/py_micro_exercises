"""
Build a weather monitoring system for tracking temperature data.

Concepts practiced:
- Instance methods with type hints and validation
- Google-style docstrings for professional documentation
- Defensive programming and error handling

Business Requirements:
- Track temperature readings from sensors
- Support Celsius/Fahrenheit conversion
- Provide weather condition analysis
- Handle invalid sensor data gracefully

# Test your class:
station = WeatherStation("Downtown")
station.add_reading(25.0)
station.add_reading(30.0) 
station.add_reading(22.5)

print(station.get_average_temp())        # Expected: 25.8
print(station.get_average_temp('F'))     # Expected: 78.5
print(station.get_condition())           # Expected: "Warm"
print(str(station))                      # Expected: "WeatherStation(Downtown, 3 readings)"
"""

from typing import List, Optional, Union

class WeatherStation:
    VALID_UNITS: List[str] = ['C', 'F']
    
    def __init__(self, name: str) -> None:
        """Initialize a weather station with a given name.
        
        Args:
            name (str): The name of the weather station.
            
        Raises:
            ValueError: If name is not a string.
        """
        if isinstance(name, str):
            self.name: str = name
        else: 
            raise ValueError(f"{name} is not a string")
        self.readings: List[Union[int, float]] = []

    @staticmethod
    def _validate_temperature(temperature: Union[int, float]) -> Union[int, float]:
        """Validate that the temperature value is a numeric type.
        
        Args:
            temperature (Union[int, float]): The temperature value to validate.
            
        Returns:
            Union[int, float]: The validated temperature value.
            
        Raises:
            ValueError: If temperature is not an integer or float value.
        """
        if isinstance(temperature, (float, int)):
            return temperature
        else:
            raise ValueError(f"{temperature} is not a number")

    @staticmethod
    def _to_fahrenheit(temperature: Union[int, float]) -> Union[int, float]:
        """Convert temperature from Celsius to Fahrenheit.
        
        Args:
            temperature (Union[int, float]): Temperature in Celsius.
            
        Returns:
            float: Temperature converted to Fahrenheit.
            
        Raises:
            ValueError: If temperature is not a valid numeric value.
        """
        WeatherStation._validate_temperature(temperature)
        return (temperature * (9/5)) + 32
    
    def add_reading(self, reading: Union[int, float]) -> None:
        """Add a temperature reading to the collection after validation.
        
        Args:
            reading (Union[int, float]): Temperature reading in Celsius.
            
        Raises:
            ValueError: If reading is not a valid numeric value.
        """
        WeatherStation._validate_temperature(reading)
        self.readings.append(reading)
    
    def get_average_temp(self, unit: str ="C") -> float:
        """Calculate the average temperature from all readings.
        
        Args:
            unit (str, optional): Temperature unit for output. Either 'C' for Celsius 
                or 'F' for Fahrenheit. Defaults to 'C'.
                
        Returns:
            float: Average temperature in the specified unit.
        """
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Unit must be one of {self.VALID_UNITS}, got '{unit}'")
        
        if len(self.readings) == 0:
            raise ValueError(f"{self.readings} is empty. No readings have been added yet.")
        
        average_celcius: Union[int, float] = sum(self.readings) / len(self.readings) 
        if unit == "F":
            return round(self._to_fahrenheit(average_celcius), 1)
        return round(average_celcius, 1)
    
    def get_minimum(self) -> Union[int, float]:
        """Get the minimum temperature reading from all recorded readings.
        
        Returns:
            Union[int, float]: The minimum temperature reading.
        """
        if len(self.readings) == 0:
            raise ValueError(f"{self.readings} is empty. No readings have been added yet.")
        else:
            return round(min(self.readings), 1) 

    def get_maximum(self) -> Union[int, float]:
        """Get the maximum temperature reading from all recorded readings.
        
        Returns:
            Union[int, float]: The maximum temperature reading.
        """
        if len(self.readings) == 0:
            raise ValueError(f"{self.readings} is empty. No readings have been added yet.")
        else:
            return round(max(self.readings), 1) 
    
    def get_condition(self) -> str:
        """Get the weather condition based on the average temperature.
        
        Returns:
            str: Weather condition string. Can be 'Freezing', 'Cold', 'Mild', 'Warm', or 'Hot'.
        """
        if self.get_average_temp() < 0:
            return "Freezing"
        elif 0 <= self.get_average_temp() <= 15:
            return "Cold"
        elif 16 <= self.get_average_temp() <= 25:
            return "Mild"
        elif 26 <= self.get_average_temp() <= 35:
            return "Warm"
        else:
            return "Hot"
    
    def get_summary(self) -> str:
        return f"{self.name}: {len(self.readings)} readings, avg {self.get_average_temp()}, condition: {self.get_condition()}"
    
    def __str__(self) -> str:
        return f"WeatherStation({self.name}, {len(self.readings)} readings)"
    
# Test your class:
station = WeatherStation("Downtown")
station.add_reading(25.0)
station.add_reading(30.0) 
station.add_reading(22.5)

print(station.get_average_temp())        # Expected: 25.8
print(station.get_average_temp('F'))     # Expected: 78.5
print(station.get_condition())           # Expected: "Warm"
print(str(station))                      # Expected: "WeatherStation(Downtown, 3 readings)"

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We need something that tracks temperatures and tells us if it's hot or cold. 
Users might want Fahrenheit or Celsius. Make it robust - our sensors sometimes send weird data."

Developer Clarifications Asked:
- Should temperature limits be hard-coded for Earth, or stay flexible for other use cases?
- What level of validation is appropriate beyond basic type checking?
- How should edge cases like empty datasets be handled?
- Should constants be used for maintainable configuration?

Stakeholder Responses:
- Prioritize code reusability over Earth-specific constraints
- Focus on type validation, trust sensor data ranges
- Graceful error handling essential for production use
- Yes, use constants for any repeated configuration values

Final Technical Decisions:
- No hard-coded temperature ranges for maximum flexibility
- Class-level VALID_UNITS constant for maintainable unit validation
- Comprehensive empty-dataset error handling
- Static methods for utility functions (validation, conversion)
- Support both int/float inputs with proper type hints

Assumptions Documented:
- Celsius as storage unit, Fahrenheit as display option
- Earth-based weather condition categories for user experience
- 1 decimal place precision for temperature display
- Station name validation for data integrity
"""