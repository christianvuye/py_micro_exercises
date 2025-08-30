"""
User Activity Detector - Duplicate User Detection

You have a list of user activity logs. Each log entry contains a user ID and a timestamp.
Find all users who appear more than once in the logs.

The logs can contain up to 100,000 entries.
Return a list of user IDs that appear more than once in the logs.
"""


def user_activity_detector(logs: list[tuple]) -> list[str]:
    """
    Identifies users with duplicate activity logs.

    Args:
        logs (list[tuple]): A list of tuples, where each tuple represents a user activity log.
                            The first element of each tuple is assumed to be the user identifier.

    Returns:
        list[str]: A list of user identifiers that appear more than once in the logs.
    """
    user_count = {}
    for log in logs:
        if log[0] not in user_count:
            user_count[log[0]] = 1
        else:
            user_count[log[0]] += 1
    return [k for k, v in user_count.items() if v > 1]


# Sample test cases (HackerRank format)
def test_user_activity_detector():
    # Sample Case 1: Multiple users with duplicates
    logs1 = [
        ("user123", "2024-01-01"),
        ("user456", "2024-01-01"),
        ("user123", "2024-01-02"),
        ("user789", "2024-01-01"),
    ]
    result1 = user_activity_detector(logs1)
    expected1 = ["user123"]
    assert set(result1) == set(expected1), f"Expected {expected1}, got {result1}"

    # Sample Case 2: No duplicates
    logs2 = [("user1", "2024-01-01"), ("user2", "2024-01-02")]
    result2 = user_activity_detector(logs2)
    expected2 = []
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    # Sample Case 3: Multiple users with duplicates
    logs3 = [
        ("user1", "2024-01-01"),
        ("user1", "2024-01-02"),
        ("user2", "2024-01-01"),
        ("user2", "2024-01-03"),
    ]
    result3 = user_activity_detector(logs3)
    expected3 = ["user1", "user2"]
    assert set(result3) == set(expected3), f"Expected {expected3}, got {result3}"

    print("Sample tests passed!")


# Run sample tests after implementation
test_user_activity_detector()

"""
=== EXERCISE #27 SUMMARY - USER ACTIVITY DETECTOR (SPACED REPETITION) ===

Pattern Mastery: 🟢 CLEAN EXECUTION
- Classic frequency counting with manual dictionary approach
- Correct filter pattern: count all, then select by threshold
- Proper tuple indexing to extract user_id from log[0]

Interview Readiness: 🟢 ADVANCED COMPLEXITY REASONING
- Sophisticated analysis of n vs u relationship (total logs vs unique users)
- Understanding of data reduction impact on space usage
- Professional requirements clarification about data structure format
- Recognition of O(n) as optimal bound for counting problems

Spaced Repetition Performance: 📈 STRONG FIRST ATTEMPT
- No syntax struggles with dictionary operations or list comprehension
- Clean implementation without unnecessary complexity
- Proper edge case handling for empty inputs

Next Review Schedule:
- Sept 2: 1st review (+2 days)
- Sept 5: 2nd review (+3 days)
- Sept 9: 3rd review (+4 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n) - must examine every log entry, optimal for counting
Space Complexity: O(u) typically, O(n) worst case where u = unique users
Pattern Type: Frequency counting with threshold filtering
Core Skills: Dictionary operations, tuple indexing, list comprehension filtering

Key Strengths Demonstrated:
- Advanced complexity analysis considering real-world data distributions
- Understanding of optimal bounds for counting problems
- Clean manual dictionary implementation showing fundamental grasp
- Professional documentation with clear parameter descriptions

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule  
Note: Shows sophisticated understanding of algorithmic analysis beyond basic Big O
"""
