"""
Missing Number - Spaced Repetition

Write a function, missing_number, that takes in a list of integers as an argument.
The list contains n distinct numbers taken from the range 0 to n (inclusive).
The function should return the missing number from this range.

There is exactly one missing number in the range.

Sample Test Cases:
missing_number([3, 0, 1]) → 2
missing_number([0, 1, 2, 4, 5]) → 3

After completing, analyze time and space complexity.
"""


def missing_number(nums: list[int]) -> int:
    """
    Finds the smallest missing non-negative integer from a list of integers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The smallest missing non-negative integer in the list.
    """
    nums_s = set(nums)
    for i in range(0, len(nums) + 1):
        if i not in nums_s:
            return i


def test_missing_number_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Missing from middle
    result = missing_number([3, 0, 1])
    expected = 2
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Missing from middle of larger range
    result = missing_number([0, 1, 2, 4, 5])
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_missing_number_sample()

"""
=== EXERCISE #14 SUMMARY - MISSING NUMBER (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG ALGORITHM WITH QUICK BUG FIX
- Correct set-based approach for O(1) membership testing optimization
- Proper understanding of range-based iteration for missing number detection
- **Initial Bug**: Used max(nums) instead of len(nums) for range calculation
- **Quick Fix**: Immediately corrected logic after explanation of edge case failure

Interview Readiness: 🟢 GOOD ALGORITHMIC THINKING
- Professional edge case clarification questions (positive vs non-negative integers)
- Understanding of problem constraints (distinct numbers, exactly one missing)
- Clean implementation with proper type hints and documentation
- Solid complexity analysis with optimization insights

Spaced Repetition Performance: 📈 STRONG IMPROVEMENT FROM PREVIOUS EXERCISES
- No Python syntax errors or comprehension issues
- Logic error was conceptual, not implementation-based
- Quick debugging and correction when bug was identified
- Demonstrated understanding of alternative approaches (sum formula, XOR)

Next Review Schedule:
- Tomorrow (Sept 1): 1st review - focus on range calculation logic
- Sept 3: 2nd review (+2 days) - should be routine by then
- Sept 6: 3rd review (+3 days)
- Sept 9: Final review before interview

Time Complexity: O(n) - iterate through range 0 to n, set lookup O(1) per check
Space Complexity: O(n) - set storage for all distinct input elements
Pattern Type: Missing element detection using set membership optimization
Core Skills: Set optimization, range iteration, edge case analysis

Key Strengths Demonstrated:
- Excellent set-based optimization understanding for membership testing
- Strong complexity analysis including space/time trade-offs
- Professional clarifying questions about input constraints
- Quick identification and correction of logical error
- Knowledge of alternative algorithmic approaches (sum, XOR methods)

Areas for Minor Improvement:
- **Initial Logic**: Range calculation should be based on expected size, not max value
- **Edge Case Thinking**: Consider when missing number is the maximum possible value
- **Algorithm Selection**: Could mention O(1) space alternatives for completeness

Status: 🟢 SOLID PROGRESS - Much cleaner execution than previous exercises
Note: Shows significant improvement in implementation accuracy and algorithmic reasoning
"""
