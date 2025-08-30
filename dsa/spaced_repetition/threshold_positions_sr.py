"""
Threshold Positions - Multi-category Index Collection

Write a function `threshold_positions` that takes in a list of numbers and a threshold value as arguments.
The function should return a dictionary with two keys: 'below' and 'above_or_equal'.
The 'below' key should map to a list of indices where the number is below the threshold.
The 'above_or_equal' key should map to a list of indices where the number is greater than or equal to the threshold.
"""


def threshold_positions(nums: list[int], threshold: int) -> dict:
    """
    Returns the positions (indices) of elements in the input list that are below or above/equal to a given threshold.

    Args:
        nums (list[int]): A list of integers to be evaluated.
        threshold (int): The threshold value to compare each element against.

    Returns:
        dict: A dictionary with two keys:
            - "below": a list of indices where the corresponding element in nums is less than the threshold.
            - "above_or_equal": a list of indices where the corresponding element in nums is greater than or equal to the threshold.

    Example:
        >>> threshold_positions([1, 5, 3, 7], 4)
        {'below': [0, 2], 'above_or_equal': [1, 3]}
    """
    result = {"below": [], "above_or_equal": []}
    for index, num in enumerate(nums):
        if num < threshold:
            result["below"].append(index)
        elif num >= threshold:
            result["above_or_equal"].append(index)
    return result


# Sample test cases (HackerRank format)
def test_threshold_positions():
    # Sample Case 1: Mixed values around threshold
    result = threshold_positions([3, 1, 7, 2, 8], 5)
    expected = {"below": [0, 1, 3], "above_or_equal": [2, 4]}
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: All values below threshold
    result = threshold_positions([1, 2, 3], 10)
    expected = {"below": [0, 1, 2], "above_or_equal": []}
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: Values equal to threshold
    result = threshold_positions([5, 3, 5, 7], 5)
    expected = {"below": [1], "above_or_equal": [0, 2, 3]}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests after implementation
test_threshold_positions()

"""
=== EXERCISE #25 SUMMARY - THRESHOLD POSITIONS (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT EXECUTION
- Clean index collection with enumerate() + conditional categorization
- Proper dictionary initialization with both required keys
- Correct boundary handling (< vs >=) without edge case confusion

Interview Readiness: 🟢 STRONG TECHNICAL COMMUNICATION  
- Professional requirements clarification about data types and edge cases
- Sound complexity analysis with correct reasoning about index storage
- Good defensive programming instincts (redundant empty check discussion)

Spaced Repetition Performance: 📈 SOLID FIRST ATTEMPT
- Immediate recognition of enumerate pattern from previous exercises
- Clean implementation without syntax struggles
- Comprehensive docstring with type hints and examples
- Quick correction of edge case handling

Next Review Schedule:
- Sept 2: 1st review (+2 days)  
- Sept 5: 2nd review (+3 days)
- Sept 9: 3rd review (+4 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n) - single pass with constant operations per element
Space Complexity: O(n) - each index stored once across two result lists  
Pattern Type: Index collection with binary categorization
Core Skills: enumerate(), conditional logic, dictionary operations

Key Strengths Demonstrated:
- Strong understanding of enumerate pattern application
- Correct complexity analysis reasoning (O(n + i) → O(n) insight)
- Professional edge case questioning and type constraint clarification  
- Clean code organization with proper documentation

Areas for Continued Practice:
- Python syntax fluency (lambda, set operations) from previous exercises
- Continue building pattern library for Affirm interview preparation

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule
Note: Shows pattern internalization and strong technical reasoning
"""
