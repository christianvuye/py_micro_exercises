"""
Intersection - Spaced Repetition

Write a function, intersection, that takes in two lists as arguments.
The function should return a new list containing elements that are common to both input lists.

The result should not contain duplicate elements and the order doesn't matter.

Sample Test Cases:
intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]) → [2, 6]
intersection(['a', 'b', 'c'], ['b', 'a', 'c']) → ['a', 'b', 'c']

After completing, analyze time and space complexity.
"""


def intersection(a: list, b: list) -> list:
    """
    Returns a list containing the intersection of two input lists.

    Args:
        a (list): The first list.
        b (list): The second list.

    Returns:
        list: A list containing elements that are present in both input lists, with duplicates removed.

    Example:
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
    """
    set_a = set(a)
    set_b = set(b)
    set_ab = set_a & set_b
    return list(set_ab)


def test_intersection_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Numbers with some overlap
    result = intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])
    expected = [2, 6]  # Note: order may vary, so we'll check set equality
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    # Sample Case 2: Strings with complete overlap
    result = intersection(["a", "b", "c"], ["b", "a", "c"])
    expected = ["a", "b", "c"]
    assert set(result) == set(expected), f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_intersection_sample()

"""
=== EXERCISE #15 SUMMARY - INTERSECTION (SPACED REPETITION) ===

Pattern Mastery: 🟢 CORRECT ALGORITHM WITH SYNTAX GAP
- Perfect understanding of set intersection approach for duplicate removal
- Clean conversion between lists and sets for optimal operations
- Proper result formatting (set → list) for expected return type
- Strong grasp of set-based optimization for membership operations

Interview Readiness: 🟡 CORE SYNTAX KNOWLEDGE GAP
- **Critical Gap**: Forgot basic set intersection syntax (& operator)
- **Had to ask**: "What's the operation/syntax to see common values in two sets?"
- Algorithm logic was perfect once syntax was recalled
- Clean implementation with proper type hints and documentation

Spaced Repetition Performance: 🔴 FUNDAMENTAL SYNTAX FORGOTTEN
- Conceptual understanding of intersection problem was immediate
- Implementation approach was optimal (sets for deduplication + O(1) lookup)
- **Major Blocker**: Basic set operations syntax not automatic
- **CRITICAL**: This is fundamental Python knowledge for technical interviews

Next Review Schedule:
- **DAILY PRACTICE REQUIRED**: Set operations (&, |, -, ^) until automatic
- Tomorrow (Sept 1): 1st review - focus on set operations syntax
- Sept 2: 2nd review (+1 day due to syntax gaps)
- Sept 4: 3rd review (+2 days) - set operations must be fluent
- Sept 7: 4th review (+3 days)
- Sept 9: Final review before interview

Time Complexity: O(n + m) - set creation + intersection + list conversion
Space Complexity: O(n + m) - two input sets plus intersection result
Pattern Type: Set intersection with type conversion for return format
Core Skills: Set operations, intersection logic, duplicate handling

Key Strengths Demonstrated:
- Optimal algorithmic approach using sets for O(1) membership testing
- Excellent complexity analysis with edge case consideration
- Clean code structure with proper documentation
- Understanding of space/time trade-offs in set vs list operations

Areas for Major Improvement:
- **CRITICAL**: Set operations syntax must be automatic (&, |, -, ^)
- **CRITICAL**: Basic Python set methods (.intersection(), .union(), .difference())
- **Important**: Core data structure operations cannot require hints in interviews

**REMINDER**: You needed set intersection syntax help - drill set operations daily: &, |, -, ^ until automatic!

Status: 🔄 REQUIRES DAILY SET OPERATIONS PRACTICE - Algorithm perfect, syntax fluency essential
Note: This is fundamental Python knowledge that must be instant recall for technical interviews
"""
