"""
Session Duration Analyzer

You're building analytics for a web application. You have user session
data and need to identify users who have unusually long sessions that
might indicate bot activity or data quality issues.

Given a list of session records, find all users who have at least one
session longer than a specified threshold AND have multiple sessions
in the dataset.

Each session record is a tuple: (user_id, duration_minutes)

Requirements:
- Return a list of user_ids that meet both criteria
- Order the results by user_id for consistent output
- Handle edge cases (empty data, no matches, etc.)

Example:
sessions = [
    ("user123", 45), ("user456", 120), ("user123", 200),
    ("user789", 30), ("user456", 25), ("user999", 150)
]
threshold = 100

Expected result: ["user123", "user456"]
- user123: has sessions 45,200 (multiple sessions, max=200 > 100) ✓
- user456: has sessions 120,25 (multiple sessions, max=120 > 100) ✓
- user789: has session 30 (only one session) ✗
- user999: has session 150 (only one session) ✗

Test cases to consider:
- Empty sessions list
- No users meet criteria
- Users with only one session
- Users with multiple sessions but none over threshold
- Very large session counts per user
"""

import random


def find_suspicious_users(sessions: list[tuple], threshold: int) -> list[str]:
    # Docstring here
    users = {}
    for session in sessions:
        if session[0] not in users:
            users[session[0]] = {"session count": 1, "has_long_session": False}
        else:
            users[session[0]]["session count"] += 1
        if session[1] > threshold:
            # alternatively, you could check here if the boolean check here is already True
            users[session[0]]["has_long_session"] = True
    return [
        k for k, v in users.items() if v["session count"] > 1 and v["has_long_session"]
    ]


# Tests that the code should pass:

# Test case 1: Basic case - some users meet both criteria
sessions1 = [
    ("user123", 45),
    ("user456", 120),
    ("user123", 200),
    ("user789", 30),
    ("user456", 25),
    ("user999", 150),
]
result1 = find_suspicious_users(sessions1, 100)
print("Test 1 - Basic case:", result1)  # Expected: ["user123", "user456"]

# Test case 2: No users meet criteria (no long sessions)
sessions2 = [("user1", 30), ("user1", 40), ("user2", 50), ("user2", 60)]
result2 = find_suspicious_users(sessions2, 100)
print("Test 2 - No long sessions:", result2)  # Expected: []

# Test case 3: No users meet criteria (no multiple sessions)
sessions3 = [("user1", 200), ("user2", 150), ("user3", 300)]
result3 = find_suspicious_users(sessions3, 100)
print("Test 3 - No multiple sessions:", result3)  # Expected: []

# Test case 4: All users meet both criteria
sessions4 = [("user1", 200), ("user1", 50), ("user2", 150), ("user2", 80)]
result4 = find_suspicious_users(sessions4, 100)
print("Test 4 - All users qualify:", result4)  # Expected: ["user1", "user2"]

# Test case 5: Empty sessions
sessions5 = []
result5 = find_suspicious_users(sessions5, 100)
print("Test 5 - Empty input:", result5)  # Expected: []

# Test case 6: Single session per user, one long
sessions6 = [("user1", 200)]
result6 = find_suspicious_users(sessions6, 100)
print("Test 6 - Single long session:", result6)  # Expected: []

# Test case 7: Multiple sessions but none long enough
sessions7 = [("user1", 80), ("user1", 90), ("user2", 70), ("user2", 85)]
result7 = find_suspicious_users(sessions7, 100)
print("Test 7 - Multiple short sessions:", result7)  # Expected: []

# Test case 8: Edge case - threshold is 0
sessions8 = [("user1", 10), ("user1", 20), ("user2", 5)]
result8 = find_suspicious_users(sessions8, 0)
print("Test 8 - Zero threshold:", result8)  # Expected: ["user1"]

# Test case 9: Many sessions for one user, few for others
sessions9 = [
    ("user1", 50),
    ("user1", 150),
    ("user1", 30),
    ("user1", 200),
    ("user2", 120),
    ("user3", 80),
    ("user3", 110),
]
result9 = find_suspicious_users(sessions9, 100)
print("Test 9 - Uneven session counts:", result9)  # Expected: ["user1", "user3"]

# Test case 10: Threshold exactly at session duration
sessions10 = [("user1", 100), ("user1", 50), ("user2", 99), ("user2", 101)]
result10 = find_suspicious_users(sessions10, 100)
print("Test 10 - Exact threshold match:", result10)  # Expected: ["user2"]

# Edge/Stress test cases:

# Large dataset - 10,000 sessions across 1,000 users
random.seed(42)  # For reproducible results
sessions_large = []
for i in range(1000):
    user_id = f"user{i}"
    # Each user gets 10 sessions with random durations
    for j in range(10):
        duration = random.randint(20, 300)
        sessions_large.append((user_id, duration))
result_large = find_suspicious_users(sessions_large, 250)
print(
    f"Test 11 - Large dataset: Found {len(result_large)} suspicious users out of 1000"
)

# Extreme edge case - all same user
sessions_extreme = [
    ("user1", i) for i in range(1, 1001)
]  # 1000 sessions, 1-1000 minutes
result_extreme = find_suspicious_users(sessions_extreme, 500)
print("Test 12 - Single user, 1000 sessions:", result_extreme)  # Expected: ["user1"]

# Edge case - very high threshold
sessions_high_threshold = [
    ("user1", 100),
    ("user1", 200),
    ("user2", 1000),
    ("user2", 50),
]
result_high = find_suspicious_users(sessions_high_threshold, 999)
print("Test 13 - Very high threshold:", result_high)  # Expected: ["user2"]

# Mixed user ID types (strings, numbers as strings)
sessions_mixed = [("123", 150), ("123", 50), ("abc", 200), ("abc", 30)]
result_mixed = find_suspicious_users(sessions_mixed, 100)
print("Test 14 - Mixed user ID types:", result_mixed)  # Expected: ["123", "abc"]

# Boundary case - exactly 2 sessions each
sessions_boundary = [("user1", 150), ("user1", 50), ("user2", 80), ("user2", 120)]
result_boundary = find_suspicious_users(sessions_boundary, 100)
print(
    "Test 15 - Exactly 2 sessions each:", result_boundary
)  # Expected: ["user1", "user2"]

"""
Time Complexity, worst-case: 
    - O(n), linear time complexity dependent on len of input list
Space Complexity, worst-case: 
    - O(n), linear time complexity dependent on len of input list
    - Two new data structures are created: a dict and a list
    - Both are 'constrained' in size by the original input list
    - Dict will only have unique keysn but will store two extra data points per user
    - Returned list will be smaller as it only returns strings from 
      the original list if a certain condition is met
"""

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Request: 
"Build analytics for web application to identify users with unusually long sessions 
who might indicate bot activity. Find users with multiple sessions AND at least one 
session over threshold duration."

Developer Clarifications Asked:
- "What specific information do I need to track for each user to efficiently check both criteria?"
- "Do I need to count HOW MANY sessions exceed threshold, or just whether there's at least one?"
- "Should results be ordered for consistent output?"

Interviewer Responses:
- Confirmed need to track: session count (for >1 check) and boolean flag (for threshold check)
- Only need boolean - just whether ANY session exceeds threshold, not count
- Yes, results should be ordered by user_id for consistency

Final Technical Decisions:
- Dictionary of dictionaries: {user_id: {"session_count": int, "has_long_session": bool}}
- Single pass O(n) algorithm processes all sessions once
- Alternative considered: tuple values (count, boolean) - equally valid
- Linear O(n) time and space complexity
- Micro-optimization rejected: checking if boolean already True costs more than assignment

Key Learning Moments:
- Space complexity heuristics developed: focus on growth rate, not number of data structures
- Peak memory usage determines space complexity (not just final structures)  
- Pattern recognition: identified as variation of counting/grouping problem from previous exercises

Assumptions Documented:
- Each session tuple contains (user_id, duration_minutes) as specified
- Threshold comparison uses > (strictly greater than)
- Algorithm scales linearly - suitable for production web analytics
"""
