"""
Unique Elements - Elements in Either But Not Both

Write a function `unique_elements` that takes in two lists as arguments.
The function should return a new list containing elements that appear in either list but not both lists.
You may assume that each input list does not contain duplicate elements.
"""


def unique_elements(list_a: list, list_b: list) -> list:
    """
    Returns a list of elements that are unique to either list_a or list_b.

    This function computes the symmetric difference between two lists,
    meaning it returns all elements that are present in one list but not both.

    Args:
        list_a (list): The first list of elements.
        list_b (list): The second list of elements.

    Returns:
        list: A list containing elements that are unique to either list_a or list_b.

    Example:
        >>> unique_elements([1, 2, 3], [2, 3, 4])
        [1, 4]
    """
    return list(set(list_a) ^ set(list_b))


def test_unique_elements_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Numbers with some overlap
    result = unique_elements([1, 2, 3], [2, 3, 4])
    expected = [1, 4]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 2: No overlap between lists
    result = unique_elements(["a", "b"], ["x", "y"])
    expected = ["a", "b", "x", "y"]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 3: Empty first list
    result = unique_elements([], [1, 2])
    expected = [1, 2]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_unique_elements_sample()

"""
=== EXERCISE #18 SUMMARY - UNIQUE ELEMENTS (SPACED REPETITION) ===

Pattern Mastery: 🟢 PATTERN MASTERY CONFIRMED
- Immediate recognition: identical to Exercise #17 symmetric difference
- Consistent implementation approach across similar problems
- Clean code with comprehensive documentation
- Demonstrates internalized understanding of set operations

Interview Readiness: 🟢 ACCELERATED PERFORMANCE  
- Rapid completion: ~5 minutes (pattern recognition)
- No hesitation on approach selection
- Professional documentation standards maintained
- Shows pattern transfer between similar problems

Spaced Repetition Performance: 📈 PATTERN INTERNALIZATION
- Instant recognition of symmetric difference requirement
- No syntax struggles with ^ operator
- Consistent solution quality across repeated patterns
- Building confidence through successful pattern application

Next Review Schedule:
- Sept 2: 1st review (+1 day)
- Sept 4: 2nd review (+2 days)
- Sept 7: 3rd review (+3 days)
- Sept 11: 4th review (+4 days) [post-interview reinforcement]

Time Complexity: O(n + m) - consistent with Exercise #17
Space Complexity: O(n + m) - consistent with Exercise #17
Pattern Type: Set symmetric difference (duplicate pattern)
Core Skills: Pattern recognition, consistent implementation

Key Strengths Demonstrated:
- Immediate pattern recognition from problem description
- Consistent high-quality implementation across similar problems
- Professional documentation maintained even for familiar patterns
- Building pattern library through successful repetition

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Duplicate pattern confirms symmetric difference mastery
"""
