"""
Interviewer Problem Statement:
"Here's the problem: You have a list of user activity logs. Each log entry contains a user ID and a timestamp.
I want you to find all users who appear more than once in the logs.

For example, if I give you:
[("user123", "2024-01-01"), ("user456", "2024-01-01"),
("user123", "2024-01-02"), ("user789", "2024-01-01")]

You should return ["user123"] because user123 appears twice.

The logs can contain up to 100,000 entries. Go ahead and code this up."

Interviewer Requirements:
- Process user activity logs to identify potential duplicate accounts or suspicious behavior
- Handle large datasets efficiently (up to 100,000 log entries)
- Return list of user IDs that appear more than once in the logs
- Optimize for both time and space efficiency
- Provide complexity analysis to guide production deployment decisions

Tests that the code should pass:
# Test case 1: Multiple users with duplicates
logs1 = [("user123", "2024-01-01"), ("user456", "2024-01-01"),
        "user123", "2024-01-02"), ("user789", "2024-01-01")]
result1 = find_frequent_users(logs1)  # Expected: ["user123"]

# Test case 2: No duplicates
logs2 = [("user1", "2024-01-01"), ("user2", "2024-01-02")]
result2 = find_frequent_users(logs2)  # Expected: []

# Test case 3: Multiple users with duplicates
logs3 = [("user1", "2024-01-01"), ("user1", "2024-01-02"),
        ("user2", "2024-01-01"), ("user2", "2024-01-03")]
result3 = find_frequent_users(logs3)  # Expected: ["user1", "user2"] (order doesn't matter)

# Test case 4: Single user multiple times
logs4 = [("user1", "2024-01-01"), ("user1", "2024-01-02"), ("user1", "2024-01-03")]
result4 = find_frequent_users(logs4)  # Expected: ["user1"]

# Test case 5: Empty logs
logs5 = []
result5 = find_frequent_users(logs5)  # Expected: []

After implementation: Explain the time and space complexity and how to optimize it
"""


# first approach
def find_duplicates(logs: list[tuple]) -> list[str]:
    """
    Identifies and returns a list of user IDs that appear more than once in the provided logs.

    Args:
        logs (list[tuple]): A list of tuples, where each tuple contains a user ID as its first element.

    Returns:
        list[str]: A list of user IDs that are duplicated in the logs, in the order they are found.
    """
    unique_ids: list[str] = []
    duplicate_ids: list[str] = []
    for log in logs:
        if log[0] not in unique_ids:
            unique_ids.append(log[0])
        elif log[0] not in duplicate_ids:
            duplicate_ids.append(log[0])
    return duplicate_ids


# Test case 1: Multiple users with duplicates
logs1 = [
    ("user123", "2024-01-01"),
    ("user456", "2024-01-01"),
    ("user123", "2024-01-02"),
    ("user789", "2024-01-01"),
]
result1 = find_duplicates(logs1)  # Expected: ["user123"]
print(result1)

# Test case 2: No duplicates
logs2 = [("user1", "2024-01-01"), ("user2", "2024-01-02")]
result2 = find_duplicates(logs2)  # Expected: []
print(result2)

# Test case 3: Multiple users with duplicates
logs3 = [
    ("user1", "2024-01-01"),
    ("user1", "2024-01-02"),
    ("user2", "2024-01-01"),
    ("user2", "2024-01-03"),
]
result3 = find_duplicates(logs3)  # Expected: ["user1", "user2"] (order doesn't matter)
print(result3)

# Test case 4: Single user multiple times
logs4 = [("user1", "2024-01-01"), ("user1", "2024-01-02"), ("user1", "2024-01-03")]
result4 = find_duplicates(logs4)  # Expected: ["user1"]
print(result4)

# Test case 5: Empty logs
logs5 = []
result5 = find_duplicates(logs5)  # Expected: []
print(result5)

# Initial time and space complexity estimates:
"""
Time Complexity:
- Overall: O(n), linear time complexity increasing with size of list
- Best case: O(n + n) -> O(2n), linear time complexity still, but with no duplicates, only the if statement gets executed and elif is never reached
- Worst case: O(n + n + n) -> O(3n), linear time complexity still, but with all logs having a duplicate, so elif statement gets executed too

Space Complexity:
- Overall: O(n), linear space complexity increasing with size of list and amount of duplicates
- Best case: O(1), constant time complexity if only one tuple and no duplicates, but tuple will be stored in the unique ID list + empty duplicate list
- Worst case: O(n), linear space complexity, with many duplicates and unique IDs, but neither unique or duplicate list can be > input list
"""


# second approach, using sets instead of list to make lookups cheaper
def find_dupes(logs: list[tuple]) -> list[str]:
    """
    Identifies user IDs that appear more than once in the provided logs.

    Args:
        logs (list[tuple]): A list of tuples, where each tuple contains a user ID as its first element.

    Returns:
        list[str]: A list of user IDs that are duplicated in the logs, unordered.
    """
    unique_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    for log in logs:
        if (
            log[0] not in unique_ids
        ):  # set lookups are O(1) -> constant time complexity, much more efficient than a list!
            unique_ids.add(log[0])
        elif log[0] not in duplicate_ids:
            duplicate_ids.add(log[0])
    return list(duplicate_ids)


# Test case 1: Multiple users with duplicates
logs1 = [
    ("user123", "2024-01-01"),
    ("user456", "2024-01-01"),
    ("user123", "2024-01-02"),
    ("user789", "2024-01-01"),
]
result1 = find_dupes(logs1)  # Expected: ["user123"]
print(result1)

# Test case 2: No duplicates
logs2 = [("user1", "2024-01-01"), ("user2", "2024-01-02")]
result2 = find_dupes(logs2)  # Expected: []
print(result2)

# Test case 3: Multiple users with duplicates
logs3 = [
    ("user1", "2024-01-01"),
    ("user1", "2024-01-02"),
    ("user2", "2024-01-01"),
    ("user2", "2024-01-03"),
]
result3 = find_dupes(logs3)  # Expected: ["user1", "user2"] (order doesn't matter)
print(result3)

# Test case 4: Single user multiple times
logs4 = [("user1", "2024-01-01"), ("user1", "2024-01-02"), ("user1", "2024-01-03")]
result4 = find_dupes(logs4)  # Expected: ["user1"]
print(result4)

# Test case 5: Empty logs
logs5 = []
result5 = find_dupes(logs5)  # Expected: []
print(result5)


def get_duplicate_ids(logs: list[tuple]) -> list[str]:
    """
    Returns a list of user IDs that appear more than once in the provided logs.

    Args:
        logs (list[tuple]): A list of tuples, where each tuple represents a log entry and the first element is the user ID.

    Returns:
        list[str]: A list of user IDs (as strings) that have duplicate entries in the logs.
    """
    id_count: dict = {}
    for log in logs:
        if log[0] not in id_count:  # O(1) - constant time complexity for dict lookups
            id_count[log[0]] = 1
        else:
            id_count[log[0]] += 1
    return [k for k, v in id_count.items() if v > 1]


# Test case 1: Multiple users with duplicates
logs1 = [
    ("user123", "2024-01-01"),
    ("user456", "2024-01-01"),
    ("user123", "2024-01-02"),
    ("user789", "2024-01-01"),
]
result1 = get_duplicate_ids(logs1)  # Expected: ["user123"]
print(result1)

# Test case 2: No duplicates
logs2 = [("user1", "2024-01-01"), ("user2", "2024-01-02")]
result2 = get_duplicate_ids(logs2)  # Expected: []
print(result2)

# Test case 3: Multiple users with duplicates
logs3 = [
    ("user1", "2024-01-01"),
    ("user1", "2024-01-02"),
    ("user2", "2024-01-01"),
    ("user2", "2024-01-03"),
]
result3 = get_duplicate_ids(
    logs3
)  # Expected: ["user1", "user2"] (order doesn't matter)
print(result3)

# Test case 4: Single user multiple times
logs4 = [("user1", "2024-01-01"), ("user1", "2024-01-02"), ("user1", "2024-01-03")]
result4 = get_duplicate_ids(logs4)  # Expected: ["user1"]
print(result4)

# Test case 5: Empty logs
logs5 = []
result5 = get_duplicate_ids(logs5)  # Expected: []
print(result5)

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Request: 
"Here's the problem: You have a list of user activity logs. Each log entry contains a user ID and a timestamp. I want you to find all users who appear more than once in the logs. The logs can contain up to 100,000 entries. Go ahead and code this up."

Developer Clarifications Asked:
- "For the function name def find_frequent_users() -> isn't find_duplicates or something similar a better name?"
- "The logs are a list of tuples, right?"

Interviewer Responses:  
- Confirmed developer can choose any descriptive function name that makes sense
- Confirmed input format: list of tuples [(user_id, timestamp), ...]
- Guided developer through complexity analysis with leading questions about list lookup performance
- Provided optimization hints about data structures and counting approaches

Final Technical Decisions:
- Chose dictionary-based counting approach for O(n) time complexity
- Identified that original list-based solution had O(n²) time due to linear lookups
- Recognized that set-based approach improved to O(n) but used two data structures
- Final insight: Separate counting logic from filtering logic for better system design
- Proposed returning dictionary instead of list to avoid unnecessary O(k) conversion bottleneck

Assumptions Documented:
- Dictionary lookups are O(1) average case for hash table operations
- Space complexity is O(n) in worst case where all users are unique
- For production with 100,000 entries, O(n) performance is acceptable
- System design benefit: Separating count generation from duplicate filtering enables more flexible use cases (different thresholds, analytics, etc.)
- Performance optimization: Avoiding list conversion when caller only needs counts
"""
