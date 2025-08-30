"""
Common Elements - List Intersection

Write a function `common_elements` that takes in two lists as arguments.
The function should return a new list containing elements that appear in both lists.
You may assume that each input list does not contain duplicate elements.
"""


def common_elements(list_a: list, list_b: list) -> list:
    """
    Returns a list of elements that are common to both input lists.

    Args:
        list_a (list): The first list to compare.
        list_b (list): The second list to compare.

    Returns:
        list: A list containing the elements found in both list_a and list_b. The result contains unique elements only.

    Example:
        >>> common_elements([1, 2, 3], [2, 3, 4])
        [2, 3]
    """
    return list(set(list_a) & set(list_b))


def test_common_elements_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Numbers with some overlap
    result = common_elements([1, 2, 3], [2, 3, 4])
    expected = [2, 3]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 2: Strings with no overlap
    result = common_elements(["a", "b"], ["x", "y"])
    expected = []
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 3: Empty first list
    result = common_elements([], [1, 2])
    expected = []
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_common_elements_sample()

"""
=== EXERCISE #16 SUMMARY - COMMON ELEMENTS (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG IMPLEMENTATION
- Optimal set intersection approach using & operator
- Clean one-liner solution leveraging Python built-ins
- Demonstrates mastery of set operations from Exercise #15
- Strong understanding of mathematical set theory concepts

Interview Readiness: 🟢 SOLID PERFORMANCE  
- Under time target: ~12 minutes vs 15 minute goal
- Comprehensive complexity analysis with edge case considerations
- Professional documentation with type hints and docstring
- Shows engineering optimization instincts (early return discussion)

Spaced Repetition Performance: 📈 BUILDING FLUENCY
- No syntax struggles with set intersection operator
- Smooth progression from Exercise #15 intersection pattern
- Demonstrates retention and application of set operations
- Good analytical reasoning about space complexity edge cases

Next Review Schedule:
- Sept 2: 1st review (+1 day)
- Sept 4: 2nd review (+2 days)  
- Sept 7: 3rd review (+3 days)
- Sept 11: 4th review (+4 days) [post-interview reinforcement]

Time Complexity: O(n + m) - correct analysis
Space Complexity: O(n + m) general case, O(1) when both lists empty
Pattern Type: Set intersection for finding common elements
Core Skills: Set operations, mathematical reasoning, edge case optimization

Key Strengths Demonstrated:
- Optimal algorithmic approach selection
- Nuanced complexity analysis including edge cases  
- Engineering optimization considerations (early return patterns)
- Clean, production-ready code with proper documentation
- Strong retention of set operation syntax from previous exercises

Areas for Continued Growth:
- Space complexity precision in conditional scenarios
- Distinguishing between theoretical edge cases vs practical optimizations

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent progression in set operations and analytical thinking
"""
