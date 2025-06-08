# type: ignore
"""
Log Timestamp Extraction: Extract just the date from log entries:
"""
from re import sub

log_entries = ["2024-01-15 10:30:45 ERROR Database connection failed", 
               "2024-01-15 10:31:02 INFO User login successful",
               "2024-01-15 10:31:15 WARN High memory usage detected"]

date_only = map(lambda x:sub(r'.*(\d{4}-\d{2}-\d{2}).*', r'\1', x), log_entries)

print(list(date_only))