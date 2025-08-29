"""
Max Value - Spaced Repetition

Write a function, max_value, that takes in list of numbers as an argument.
The function should return the largest number in the list.

Solve this without using any built-in list methods.
You can assume that the list is non-empty.

Example:
max_value([4, 7, 2, 8, 10, 9]) → 10
max_value([10, 5, 40, 40.3]) → 40.3

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def max_value(nums: list[int]) -> int:
    """
    Finds and returns the maximum value in a list of integers.

    Args:
        nums (list[int]): A list of integers to search.

    Returns:
        int: The maximum integer value found in the list. If the list is empty, returns negative infinity.

    Example:
        >>> max_value([1, 5, 3, 9, 2])
        9
    """
    current_max = float("-inf")
    for num in nums:
        if num > current_max:
            current_max = num
    return current_max


def test_max_value():
    """
    Tests the max_value function with multiple test cases.

    Each test case provides a list of numbers and checks if the max_value function
    returns the expected maximum value. The results are printed to indicate whether
    the actual output matches the expected value.

    Test cases:
        1. nums = [4, 7, 2, 8, 10, 9], expected_value = 10
        2. nums = [10, 5, 40, 40.3], expected_value = 40.3
    """
    # Test case 1
    nums = [4, 7, 2, 8, 10, 9]
    expected_value = 10
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")

    # Test case 2
    nums = [10, 5, 40, 40.3]
    expected_value = 40.3
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")

    # Test case 3
    nums = [7, 7, 7, 7, 7, 7]
    expected_value = 7
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")

    # Test case 4
    nums = [4]
    expected_value = 4
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")

    # Test case 5
    nums = [-4, 7, -2, -8, 10, 9]
    expected_value = 10
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")

    # Test case 6
    nums = [-24.5, 8.15, -80.15, -8.23517, 10, 9]
    expected_value = 10
    result = max_value(nums)
    if result == expected_value:
        print(f"Expected value: {expected_value} == actual value: {result}")
    else:
        print(f"Expected value: {expected_value} != actual value: {result}")


# Run your tests
test_max_value()

"""
=== EXERCISE #1 SUMMARY - MAX VALUE (SPACED REPETITION) ===

Pattern Mastery: 🟡 IN PROGRESS
- Linear scan optimization pattern demonstrated well
- Clean single-pass implementation  
- Perfect complexity analysis

Interview Readiness: 🟡 DEVELOPING
- Good foundation established, needs repetition for speed
- Comprehensive edge case thinking
- Clean, readable code

Spaced Repetition Performance: 📈 IMPROVED FROM ORIGINAL
- Added missing edge cases from original attempt
- Fixed code quality issues (variable shadowing)
- More thorough testing approach

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days) 
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(n) - single pass through list
Space Complexity: O(1) - constant extra space
Pattern Type: Linear scan with accumulator
Core Skill: Single-pass optimization without built-in functions

Key Improvements Made:
- Fixed variable shadowing (max_value → current_max)
- Added comprehensive edge cases (single element, all same, negatives, floats)
- Enhanced test case documentation

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
"""
