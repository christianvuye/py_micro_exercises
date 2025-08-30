"""
Exclusive Items - Symmetric Difference

Write a function `exclusive_items` that takes in two lists as arguments.
The function should return a new list containing elements that are in either list but not both lists.
You may assume that each input list does not contain duplicate elements.
"""


def exclusive_items(list_a: list, list_b: list) -> list:
    """
    Returns a list of items that are present in either list_a or list_b, but not in both.

    Args:
        list_a (list): The first list of items.
        list_b (list): The second list of items.

    Returns:
        list: A list containing items that are exclusive to either list_a or list_b.

    Example:
        >>> exclusive_items([1, 2, 3], [2, 3, 4])
        [1, 4]
    """
    return list(set(list_a) ^ set(list_b))


def test_exclusive_items_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Numbers with some overlap
    result = exclusive_items([1, 2, 3], [2, 3, 4])
    expected = [1, 4]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 2: No overlap between lists
    result = exclusive_items(["a", "b"], ["x", "y"])
    expected = ["a", "b", "x", "y"]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 3: Complete overlap
    result = exclusive_items([1, 2], [1, 2])
    expected = []
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_exclusive_items_sample()

"""
=== EXERCISE #17 SUMMARY - EXCLUSIVE ITEMS (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT PROGRESSION
- Perfect symmetric difference implementation using ^ operator
- Strong mathematical understanding: "either but not both"
- Clean one-liner leveraging Python set operations
- Demonstrates mastery of different set operation types

Interview Readiness: 🟢 ACCELERATING PERFORMANCE
- Ahead of schedule: ~10 minutes vs 15 minute target
- Immediate recognition of symmetric difference pattern
- Professional clarifying question about empty lists
- Precise complexity analysis without hesitation

Spaced Repetition Performance: 📈 BUILDING CONFIDENCE
- No syntax struggles with set operators
- Smooth pattern recognition from problem description
- Strong retention of set operation concepts
- Accurate complexity reasoning with edge case awareness

Next Review Schedule:
- Sept 2: 1st review (+1 day)
- Sept 4: 2nd review (+2 days)
- Sept 7: 3rd review (+3 days)
- Sept 11: 4th review (+4 days) [post-interview reinforcement]

Time Complexity: O(n + m) - correct analysis  
Space Complexity: O(n + m) - correct analysis
Pattern Type: Set symmetric difference for exclusive elements
Core Skills: Set operations, mathematical reasoning, pattern recognition

Key Strengths Demonstrated:
- Immediate pattern recognition (symmetric difference)
- Professional edge case clarification (empty lists)
- Accurate complexity analysis including result size bounds
- Clean implementation with proper documentation
- Strong progression in set operation fluency

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent velocity and confidence with set operations
"""
