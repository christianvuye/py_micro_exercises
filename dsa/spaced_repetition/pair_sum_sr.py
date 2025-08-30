"""
Pair Sum - Two Sum Returning Indices

Write a function `pair_sum` that takes in a list of numbers and a target sum as arguments.
The function should return a list containing the indices of a pair of elements that sum to the target.
The indices returned should be in sorted order. If no such pair exists, return None.
You may assume that there will be at most one pair that sums to the target.
"""


def pair_sum(nums: list[int | float], target: int | float) -> None | list[int]:
    """
    Finds two indices in the input list whose corresponding values sum up to the target value.

    Args:
        nums (list[int | float]): List of integers or floats to search through.
        target (int | float): The target sum to find.

    Returns:
        None: If no such pair exists or the list is too short.
        list[int | float]: A list containing the indices of the two numbers whose sum equals the target.

    Example:
        >>> pair_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    if len(nums) == 0 or len(nums) == 1:
        return None
    previous_nums = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in previous_nums:
            return [previous_nums[complement], index]
        else:
            previous_nums[num] = index
    return None


def test_pair_sum_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Pair exists
    result = pair_sum([3, 2, 5, 4, 1], 8)
    expected = [0, 2]  # nums[0] + nums[2] = 3 + 5 = 8
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Pair exists at different positions
    result = pair_sum([4, 7, 9, 2, 5, 1], 5)
    expected = [0, 5]  # nums[0] + nums[5] = 4 + 1 = 5
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: No pair exists
    result = pair_sum([4, 7, 9, 2, 5, 1], 17)
    expected = None
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_pair_sum_sample()

"""
=== EXERCISE #21 SUMMARY - PAIR SUM (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT IMPLEMENTATION
- Optimal hash map approach for two sum with indices
- Perfect complement lookup pattern: check before store
- Proper edge case handling for empty/single element lists
- Clean enumerate() usage for index tracking
- Strong progression from contains_target pattern (Exercise #20)

Interview Readiness: 🟢 PROFESSIONAL QUALITY SOLUTION
- Comprehensive clarifying questions about data types and constraints
- Optimal O(n) time complexity with hash map approach
- Clean early returns for impossible cases
- Professional documentation with comprehensive type hints
- Caught and corrected sample test case errors

Spaced Repetition Performance: 📈 EXCELLENT COMPLEXITY ANALYSIS
- Accurate time complexity: O(n) with best/worst case understanding
- Correct space complexity: O(n) worst case analysis
- Shows mastery of hash map operation complexities
- Strong improvement in complexity reasoning precision
- Clean implementation without unnecessary complexity

Next Review Schedule:
- Sept 1: 1st review (tomorrow)
- Sept 3: 2nd review (+2 days)
- Sept 6: 3rd review (+3 days)
- Sept 9: 4th review (+3 days) [Final prep before interview]

Time Complexity: O(n) worst case, O(1) best case
Space Complexity: O(n) worst case for unique elements
Pattern Type: Two Sum returning indices with hash map lookup
Core Skills: Hash map usage, complement calculation, index management

Key Strengths Demonstrated:
- Optimal algorithmic approach (hash map vs brute force O(n²))
- Professional edge case handling and validation
- Accurate complexity analysis with best/worst case scenarios
- Clean code structure with proper type hints and documentation
- Strong pattern evolution from existence check to index return

Minor Improvement Note:
- Return type hint: `None | list[int]` (indices always integers, not floats)

🎉 TIER 3: ADVANCED PATTERNS - STRONG START

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Ready to tackle more complex pattern variations with confidence
"""
