# type: ignore
"""
Server Response Time Conversion
Convert response times from milliseconds to seconds (divide by 1000, round to 3 decimals):
"""

response_times_ms = [1500, 250, 3200, 800, 450]

response_times_s = map(lambda x: round(x/1000, 3), response_times_ms)

print(list(response_times_s))