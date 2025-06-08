# type: ignore
"""
Date Format Standardization:
Convert dates from MM/DD/YYYY to YYYY-MM-DD format
"""

dates_us_format = ["01/15/2024", "03/22/2024", "12/01/2023", "07/04/2024"] 

dates_standardized = map(lambda x:x[6:10]+"-"+x[:2]+"-"+x[3:5], dates_us_format)

print(list(dates_standardized))