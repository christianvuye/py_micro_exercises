# type: ignore
"""
API Response Processing: Extract user IDs from API response objects.
"""

api_responses = [
    {"status": "success", "user": {"id": 12345, "name": "John"}},
    {"status": "success", "user": {"id": 67890, "name": "Jane"}},
    {"status": "success", "user": {"id": 54321, "name": "Bob"}}
]

user_ids = map(lambda x:x["user"]["id"], api_responses)

print(list(user_ids))