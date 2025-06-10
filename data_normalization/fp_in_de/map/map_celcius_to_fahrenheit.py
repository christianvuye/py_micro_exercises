# type: ignore
"""
Temperature Data Conversion
Convert Celsius to Fahrenheit for weather data (F = C * 9/5 + 32, round to 1 decimal):
"""

temperatures_celsius = [20, 25, 30, 15, 35]
# Expected output: [68.0, 77.0, 86.0, 59.0, 95.0]

temperatures_fahrenheit = map(lambda x:round(x*(9/5)+32, 1), temperatures_celsius)

print(list(temperatures_fahrenheit))