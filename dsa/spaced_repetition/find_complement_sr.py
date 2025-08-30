"""
Find Complement - First Number with Complement

Write a function `find_complement` that takes in a list of numbers and a target sum as arguments.
The function should return the first number in the list that has a complement (another number in the list)
such that the two numbers sum to the target value. If no such number exists, return None.
"""

from collections import Counter


def find_complement(nums: list[int | float], target: int | float) -> int | float:
    """
    Finds and returns a number from the input list whose complement (target - number) also exists in the list.

    Args:
        nums (list[int | float]): List of integers or floats to search.
        target (int | float): The target value to find complements for.

    Returns:
        int | float | None: The first number in the list whose complement exists in the list, or None if no such pair is found.

    Example:
        >>> find_complement([1, 2, 3, 4], 5)
        1  # Because 5 - 1 = 4, and 4 is in the list.
    """
    if len(nums) == 0 or len(nums) == 1:
        return None
    num_freq = Counter(nums)
    for num in nums:
        complement = target - num
        if complement in num_freq:
            if complement == num:
                if num_freq[num] > 1:
                    return num
            else:
                return num
    return None


def test_find_complement_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Complement exists
    result = find_complement([3, 4, 6, 8], 10)
    expected = 4  # 4 + 6 = 10, 4 appears before 6
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Multiple complements, return first
    result = find_complement([1, 2, 3, 4, 5], 7)
    expected = 2  # 2 + 5 = 7, and 3 + 4 = 7, but 2 appears first
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 3: No complement exists
    result = find_complement([1, 2, 3], 10)
    expected = None
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 4: Self complement case:
    result = find_complement([5, 3], 10)
    expected = None
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 5: Self complement case:
    result = find_complement([3, 3, 6], 9)
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_find_complement_sample()

"""
=== EXERCISE #23 SUMMARY - FIND COMPLEMENT (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT PROBLEM SOLVING
- Strong Counter-based approach for frequency tracking
- Perfect self-complement edge case handling (frequency > 1 check)
- Clean iteration through original list order for "first occurrence" requirement
- Professional debugging approach when hidden tests failed
- Shows mastery of frequency-based complement problems

Interview Readiness: 🟢 STRONG DEBUGGING SKILLS
- Comprehensive clarifying questions about constraints and edge cases
- Professional response to test failures: requested specific failure details
- Iterative improvement: set approach → Counter approach with edge case fix
- Clean code structure with proper early returns
- Excellent pattern recognition for self-complement cases

Spaced Repetition Performance: 📈 SOLID COMPLEXITY ANALYSIS
- Accurate time complexity: O(n) with Counter creation + main loop
- Correct space complexity: O(n) for unique element storage
- Minor typo correction: len() operations are O(1), not O(n) ✅
- Shows understanding of Counter operations and dictionary lookups
- Good analysis of worst-case scenarios

Next Review Schedule:
- Sept 1: 1st review (tomorrow)
- Sept 3: 2nd review (+2 days)
- Sept 6: 3rd review (+3 days)
- Sept 9: 4th review (+3 days) [Final prep before interview]

Time Complexity: O(n) for Counter creation and main loop
Space Complexity: O(n) for frequency storage of unique elements
Pattern Type: First element with complement using frequency counting
Core Skills: Counter usage, frequency-based logic, edge case handling

Key Strengths Demonstrated:
- Professional debugging approach when tests failed
- Correct identification and handling of self-complement edge case
- Clean iterative improvement from initial approach to final solution
- Accurate complexity analysis with minor corrections
- Strong pattern recognition for frequency-based complement problems

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent problem-solving progression and debugging skills
"""
