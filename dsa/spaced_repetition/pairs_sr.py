"""
Pairs - Generate All Unique Pairs

Write a function, pairs, that takes in a list as an argument.
The function should return a new list containing all unique pairs of elements from the input list.
The pairs should be represented as lists with exactly two elements.
You can return the pairs in any order.
"""


def pairs(lst: list) -> list[list]:
    """
    Generates all unique pairs from a given list.

    Args:
        lst (list): The input list from which pairs are to be generated.

    Returns:
        list[list]: A list of lists, where each inner list contains a unique pair of elements from the input list.
                    Returns an empty list if the input list has fewer than two elements.

    Examples:
        >>> pairs([1, 2, 3])
        [[1, 2], [1, 3], [2, 3]]
    """
    if len(lst) == 0 or len(lst) == 1:
        return []
    if len(lst) == 2:
        return [lst]
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            result.append([lst[i], lst[j]])
    return result


# Sample test cases (HackerRank format)
def test_pairs():
    # Sample Case 1: Basic list
    result = pairs(["a", "b", "c"])
    expected = [["a", "b"], ["a", "c"], ["b", "c"]]
    # Order doesn't matter, so we'll check length and membership
    assert len(result) == len(expected), (
        f"Expected {len(expected)} pairs, got {len(result)}"
    )
    for pair in expected:
        assert pair in result or [pair[1], pair[0]] in result, f"Missing pair {pair}"

    # Sample Case 2: Two elements
    result = pairs([1, 2])
    expected = [[1, 2]]
    assert len(result) == 1, f"Expected 1 pair, got {len(result)}"
    assert result[0] == [1, 2] or result[0] == [2, 1], (
        f"Expected [1, 2] or [2, 1], got {result[0]}"
    )

    # Sample Case 3: Single element
    result = pairs(["x"])
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests after implementation
test_pairs()

"""
=== EXERCISE #26 SUMMARY - PAIRS (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT EXECUTION
- Classic nested loop pattern for combinatorial generation (i < j)
- Smart edge case optimization for length 2 using list wrapping
- Correct systematic pair generation without duplicates

Interview Readiness: 🟢 STRONG TECHNICAL PRECISION
- Comprehensive type hints and professional documentation
- Thorough edge case questioning about duplicates and data types
- Accurate mathematical understanding (n*(n-1)/2 formula)
- Clean implementation with proper bounds (i < j pattern)

Spaced Repetition Performance: 📈 SOLID FIRST ATTEMPT
- Quick recognition of combinatorial generation requirements
- Efficient edge case handling for empty, single, and double element cases
- No syntax struggles with nested loops or list operations

Next Review Schedule:
- Sept 2: 1st review (+2 days)
- Sept 5: 2nd review (+3 days)  
- Sept 9: 3rd review (+4 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n²) - exactly n*(n-1)/2 pair generation operations
Space Complexity: O(n²) - storing n*(n-1)/2 pairs in result list
Pattern Type: Combinatorial generation with nested iteration
Core Skills: Nested loops, index management, edge case optimization

Key Strengths Demonstrated:
- Understanding of mathematical relationship between input size and output size
- Efficient edge case optimization (length 2 shortcut)
- Professional requirements clarification about data types and duplicates
- Clean nested loop implementation with proper index bounds

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule
Note: Shows strong grasp of combinatorial algorithms and edge case handling
"""
