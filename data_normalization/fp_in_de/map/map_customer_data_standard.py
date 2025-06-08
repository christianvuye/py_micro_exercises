# type: ignore
"""
You have customer phone numbers in different formats. Standardize them to remove all non-digits.
"""
from re import sub

phone_numbers = ["(555) 123-4567", "555.123.4567", "555-123-4567", "+1-555-123-4567"]

remove_non_digits = map(lambda phone_nr:sub(r'\D', "", phone_nr), phone_numbers)

print(list(remove_non_digits))