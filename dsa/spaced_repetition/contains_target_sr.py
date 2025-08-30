"""
Contains Target - Two Sum Existence Check

Write a function `contains_target` that takes in a list of numbers and a target sum as arguments.
The function should return a boolean indicating whether or not there exist two distinct elements
in the list that sum to the target value.
"""


def contains_target(nums: list[int | float], target: int | float) -> bool:
    """
    Checks if any two distinct numbers in the list sum up to the target value.

    Args:
        nums (list[int | float]): List of integers or floats to check.
        target (int | float): The target sum to find.

    Returns:
        bool: True if there exists a pair of numbers in nums whose sum is equal to target, False otherwise.
    """
    previous_numbers = set()
    for num in nums:
        complement = target - num
        if complement in previous_numbers:
            return True
        else:
            previous_numbers.add(num)
    return False


def test_contains_target_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Target sum exists
    result = contains_target([3, 4, 6, 8], 10)
    expected = True  # 4 + 6 = 10
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Target sum does not exist
    result = contains_target([4, 7, 1, -3], 15)
    expected = False  # No pair sums to 15
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: Single element list
    result = contains_target([5], 10)
    expected = False  # Need two distinct elements
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_contains_target_sample()

"""
=== EXERCISE #20 SUMMARY - CONTAINS TARGET (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT IMPLEMENTATION
- Optimal complement lookup approach using set
- Perfect "check before add" logic for distinct element requirement
- Early return optimization for efficient performance
- Clean, readable implementation with proper type hints
- Demonstrates mastery of fundamental two-sum pattern

Interview Readiness: 🟢 PROFESSIONAL QUALITY SOLUTION
- Caught test case error: 4 + 1 = 5 (shows attention to detail)
- Professional clarifying questions about data types and distinct elements
- Optimal O(n) time complexity with hash set approach
- Clean code structure with comprehensive documentation

Spaced Repetition Performance: 📈 STRONG COMPLEXITY ANALYSIS
- Accurate time complexity: O(n) worst case, better with early termination
- Correct space complexity: O(n) worst case for unique elements
- Shows understanding of best/worst case scenarios
- Solid improvement in complexity reasoning precision

Next Review Schedule:
- Sept 1: 1st review (tomorrow)
- Sept 3: 2nd review (+2 days)
- Sept 6: 3rd review (+3 days)
- Sept 9: 4th review (+3 days) [Final prep before interview]

Time Complexity: O(n) worst case, O(1) best case
Space Complexity: O(n) worst case for unique elements  
Pattern Type: Two Sum existence check with complement lookup
Core Skills: Hash set usage, complement calculation, early termination

Key Strengths Demonstrated:
- Optimal algorithmic approach selection (complement lookup vs brute force)
- Professional attention to detail (caught test case error)
- Accurate complexity analysis with best/worst case understanding
- Clean implementation with proper type hints and documentation
- Strong pattern recognition for two-sum problems

🎉 TIER 2 COMPLETE: Pattern Recognition (Exercises 11-20) FINISHED

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Ready to advance to Tier 3: Advanced Patterns (Exercises 21-30)
"""
