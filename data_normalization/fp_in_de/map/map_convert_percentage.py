# type: ignore
"""
Performance Metrics Calculation
Calculate conversion rates as percentages (conversions/visits * 100, rounded to 1 decimal)
"""

campaign_data = [
    {"visits": 1000, "conversions": 25},
    {"visits": 1500, "conversions": 45},
    {"visits": 800, "conversions": 12},
    {"visits": 2000, "conversions": 80}
]

conversion_rates = map(lambda x: round(x["conversions"]/x["visits"] * 100, 1), campaign_data)

print(list(conversion_rates))