"""
Value Positions - Index Collection with Filtering

Write a function `value_positions` that takes in a list of numbers and a target value as arguments.
The function should return a list of all indices where the target value appears in the input list.
If the target value does not appear in the list, return an empty list.
"""


def value_positions(nums: list[int | float], target: int | float) -> list[int]:
    """
    Finds all indices of a target value in a list of numbers.

    Args:
        nums (list[int | float]): The list of numbers to search.
        target (int | float): The value to find in the list.

    Returns:
        list[int]: A list of indices where the target value occurs in nums.
    """
    if len(nums) == 0:
        return []
    result = []
    for index, num in enumerate(nums):
        if num == target:
            result.append(index)
    return result


def test_value_positions_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Multiple occurrences
    result = value_positions([3, 1, 4, 1, 5], 1)
    expected = [1, 3]  # 1 appears at indices 1 and 3
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Single occurrence
    result = value_positions([2, 7, 8, 3, 1], 8)
    expected = [2]  # 8 appears at index 2
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: Target not found
    result = value_positions([1, 2, 3, 4], 5)
    expected = []  # 5 does not appear in the list
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_value_positions_sample()

"""
=== EXERCISE #24 SUMMARY - VALUE POSITIONS (SPACED REPETITION) ===

Pattern Mastery: 🟢 CLEAN IMPLEMENTATION
- Optimal linear search approach with index collection
- Clean enumeration pattern for simultaneous value/index access
- Proper empty list edge case handling
- Simple, readable solution without unnecessary complexity
- Shows mastery of basic index collection patterns

Interview Readiness: 🟢 EFFICIENT PERFORMANCE
- Fast completion: ~8 minutes vs 10 minute target
- Comprehensive clarifying questions about data types and constraints
- Professional documentation with clear type hints
- Clean code structure with logical flow
- All edge cases handled correctly

Spaced Repetition Performance: 📈 EXCELLENT COMPLEXITY ANALYSIS
- Accurate time complexity: O(n) - must scan entire list always
- Correct space complexity: O(n) worst case when all elements match
- Strong understanding of amortized append operations
- Good analysis of best/worst case scenarios for space usage
- Clear reasoning about unavoidable linear scan requirement

Next Review Schedule:
- Sept 1: 1st review (tomorrow)
- Sept 3: 2nd review (+2 days)
- Sept 6: 3rd review (+3 days)
- Sept 9: 4th review (+3 days) [Final prep before interview]

Time Complexity: O(n) - must examine every element
Space Complexity: O(n) worst case when all elements match target
Pattern Type: Linear search with index collection and filtering
Core Skills: Enumeration, list accumulation, linear search

Key Strengths Demonstrated:
- Clean, straightforward implementation approach
- Accurate complexity analysis with best/worst case understanding
- Professional edge case identification and handling
- Fast problem-solving with minimal complexity
- Strong understanding of result list growth patterns

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent velocity and clean implementation skills
"""
