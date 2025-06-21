"""
Active User Filtering
Filter users who have logged in within the last 30 days for targeted marketing campaigns:
"""

from datetime import datetime, timedelta

# Current date for reference
current_date = datetime(2024, 6, 21)

user_activity = [
    {"user_id": "U001", "name": "Alice", "last_login": datetime(2024, 6, 20)},
    {"user_id": "U002", "name": "Bob", "last_login": datetime(2024, 5, 15)},
    {"user_id": "U003", "name": "Charlie", "last_login": datetime(2024, 6, 18)},
    {"user_id": "U004", "name": "Diana", "last_login": datetime(2024, 4, 10)},
    {"user_id": "U005", "name": "Eve", "last_login": datetime(2024, 6, 1)},
    {"user_id": "U006", "name": "Frank", "last_login": datetime(2024, 3, 22)},
    {"user_id": "U007", "name": "Grace", "last_login": datetime(2024, 6, 19)},
    {"user_id": "U008", "name": "Henry", "last_login": datetime(2024, 5, 25)}
]

# Expected output: Users who logged in on or after 2024-05-22 (30 days ago)
# Should return: Alice, Charlie, Eve, Grace, Henry

active_users = filter(lambda x: True if x["last_login"] > current_date - timedelta(days=30) else False, user_activity)

print(*(user["name"] for user in list(active_users)), sep=", ")

# Slightly more concise:
lambda x: x["last_login"] > current_date - timedelta(days=30)