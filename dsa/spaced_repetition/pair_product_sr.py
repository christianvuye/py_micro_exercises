"""
Pair Product - Two Product Returning Indices

Write a function `pair_product` that takes in a list of numbers and a target product as arguments.
The function should return a list containing the indices of a pair of elements whose product equals the target.
The indices returned should be in sorted order. If no such pair exists, return None.
You may assume that there will be at most one pair whose product equals the target.
"""


def pair_product(nums: list[int | float], target: int | float) -> list[int]:
    """
    Finds the indices of two numbers in the input list whose product equals the target value.

    Args:
        nums (list[int | float]): A list of integers or floats to search through. Must not contain zero.
        target (int | float): The target product value. Must not be zero.

    Returns:
        list[int]: A list containing the indices of the two numbers whose product equals the target.
                   Returns None if no such pair exists or if the input list has fewer than two elements.

    Raises:
        Exception: If target is zero.
        ZeroDivisionError: If zero is present in nums.

    Example:
        >>> pair_product([2, 4, 1, 6], 8)
        [0, 1]
        >>> pair_product([0, 2, 4], 8)
        ZeroDivisionError: 0 cannot be in the nums list!
        >>> pair_product([2, 4, 1, 6], 0)
        Exception: Target cannot be 0!
    """
    if target == 0:
        raise Exception(f"Target cannot be {target}!")
    if 0 in set(nums):
        raise ZeroDivisionError("0 cannot be in the nums list!")
    if len(nums) == 0 or len(nums) == 1:
        return None
    previous_nums = {}
    for index, num in enumerate(nums):
        complement = target / num
        if complement in previous_nums:
            return [previous_nums[complement], index]
        else:
            previous_nums[num] = index
    return None


def test_pair_product_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Product exists
    result = pair_product([3, 2, 5, 4, 1], 8)
    expected = [1, 3]  # nums[1] * nums[3] = 2 * 4 = 8
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Different pair
    result = pair_product([4, 7, 9, 2, 5, 1], 28)
    expected = [0, 1]  # 4 * 7 = 28
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: No pair exists
    result = pair_product([4, 7, 9, 2, 5, 1], 100)
    expected = None
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_pair_product_sample()

"""
=== EXERCISE #22 SUMMARY - PAIR PRODUCT (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG IMPLEMENTATION
- Optimal hash map approach adapted from pair_sum pattern
- Clean complement calculation using division: complement = target / num
- Smart constraint handling: explicit exceptions for target=0 and nums containing 0
- Direct parallel to Exercise #21 with multiplication instead of addition
- Professional error handling with clear exception messages

Interview Readiness: 🟢 SOLID PERFORMANCE  
- Comprehensive edge case identification and handling
- Professional documentation with clear constraint specifications
- Clean code structure following established patterns
- Proper exception handling with informative error messages
- Strong pattern transfer from previous two-sum exercises

Spaced Repetition Performance: 📈 CONSISTENT COMPLEXITY ANALYSIS
- Accurate time complexity: O(n) worst case when no complement exists
- Correct space complexity: O(n) for hash map storage
- Shows understanding of division vs subtraction in complement calculation
- Clean implementation without unnecessary complexity

Next Review Schedule:
- Sept 1: 1st review (tomorrow)
- Sept 3: 2nd review (+2 days)
- Sept 6: 3rd review (+3 days)
- Sept 9: 4th review (+3 days) [Final prep before interview]

Time Complexity: O(n) worst case when no pair exists
Space Complexity: O(n) for hash map storage
Pattern Type: Two Product returning indices with division-based complement lookup
Core Skills: Hash map usage, complement calculation via division, constraint handling

Key Strengths Demonstrated:
- Pattern adaptation: sum → product with appropriate operations
- Professional constraint definition and enforcement
- Clean error handling with explicit exception types
- Consistent complexity analysis approach
- Strong pattern library building across similar problems

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent pattern transfer and professional constraint handling
"""
