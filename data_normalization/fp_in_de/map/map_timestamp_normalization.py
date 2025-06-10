# type: ignore
"""
Timestamp Normalization
Convert various timestamp formats to ISO format (YYYY-MM-DD HH:MM:SS) using datetime parsing:
"""

from datetime import datetime

timestamps = [
    "2024-01-15T10:30:45Z",      # ISO with timezone
    "2024/01/15 10:30:45",       # US format with slashes
    "15-01-2024 10:30:45",       # European format
    "01/15/24 10:30:45"          # Short year format
]

# Expected output: ["2024-01-15 10:30:45", "2024-01-15 10:30:45", "2024-01-15 10:30:45", "2024-01-15 10:30:45"]

def parse_timestamp(timestamp_str):
    date_format_iso_with_timezone = "%Y-%m-%dT%H:%M:%SZ"
    date_format_us_with_slashes = "%Y/%m/%d %H:%M:%S"
    date_format_european = "%d-%m-%Y %H:%M:%S"
    date_format_short_year = "%m/%d/%y %H:%M:%S"
    date_format_final = "%Y-%m-%d %H:%M:%S"
    try:
        print(f"Current timestamp_str trying to be parsed {timestamp_str}")
        timestamp_dt = datetime.strptime(timestamp_str, date_format_iso_with_timezone)
        print(f"Current timestamp_str completed parsing on the first try/except {timestamp_str} \n")
        return datetime.strftime(timestamp_dt, date_format_final)
    except Exception as e:
        print(f"First try/except raised error {e}")
    
    try:
        print(f"Current timestamp_str trying to be parsed {timestamp_str}") 
        timestamp_dt = datetime.strptime(timestamp_str, date_format_us_with_slashes)
        print(f"Current timestamp_str completed parsing on the second try/except {timestamp_str} \n")
        return datetime.strftime(timestamp_dt, date_format_final)
    except Exception as e:
        print(f"Second try/except raised error {e}")
    
    try:
        print(f"Current timestamp_str trying to be parsed {timestamp_str}")
        timestamp_dt = datetime.strptime(timestamp_str, date_format_european)
        print(f"Current timestamp_str completed parsing on the third try/except {timestamp_str} \n")
        return datetime.strftime(timestamp_dt, date_format_final)
    except Exception as e:
        print(f"Third try/except raised error {e}")
    
    try:
        print(f"Current timestamp_str trying to be parsed {timestamp_str}")
        timestamp_dt = datetime.strptime(timestamp_str, date_format_short_year)
        print(f"Current timestamp_str completed parsing on the fourth try/except {timestamp_str} \n")
        return datetime.strftime(timestamp_dt, date_format_final)
    except Exception as e:
        print(f"Fourth try/except raised error {e}")
    
timestamps_normalized = map(parse_timestamp, timestamps)

print(list(timestamps_normalized))

"""
Solution using array and loop:

# Remove debug prints, add error handling for unparseable dates
def parse_timestamp(timestamp_str):
    formats = [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y/%m/%d %H:%M:%S", 
        "%d-%m-%Y %H:%M:%S",
        "%m/%d/%y %H:%M:%S"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(timestamp_str, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    
    return None  # or raise exception for unparseable dates
"""