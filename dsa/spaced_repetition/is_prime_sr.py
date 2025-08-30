"""
Is Prime - Spaced Repetition

Write a function, is_prime, that takes in a number as an argument. The function
should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7.
For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.

Example:
is_prime(2) → True
is_prime(3) → True
is_prime(4) → False
is_prime(5) → True
is_prime(6) → False
is_prime(7) → True

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""

from math import sqrt


def is_prime(n: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if n in (0, 1):
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    """
    Tests the is_prime function with a series of predefined inputs and expected outputs.

    This function runs multiple assertions to verify that is_prime correctly identifies
    prime and non-prime numbers for a range of test cases, including edge cases such as 0 and 1.
    If all tests pass, it prints "ALL TESTS PASSED". If any test fails, an assertion error is raised
    with details about the failed test.
    """

    # Test1
    to_evaluate = 2
    expected = True
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test2
    to_evaluate = 3
    expected = True
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test3
    to_evaluate = 4
    expected = False
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test4
    to_evaluate = 5
    expected = True
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test5
    to_evaluate = 6
    expected = False
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test6
    to_evaluate = 7
    expected = True
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test7
    to_evaluate = 1
    expected = False
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test8
    to_evaluate = 0
    expected = False
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    # Test9
    to_evaluate = 2400
    expected = False
    result = is_prime(to_evaluate)
    assert expected == result, f"TEST FAILED, expected: {expected} got {result}"

    print("ALL TESTS PASSED")


test_is_prime()

"""
=== EXERCISE #7 SUMMARY - IS PRIME (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG MATHEMATICAL REASONING
- Correctly identified and implemented square root optimization independently
- Sound algorithmic logic with proper edge case handling (0, 1, 2)
- Clean iterative approach with early termination on factor discovery
- Demonstrates understanding of mathematical efficiency principles

Interview Readiness: 🟢 OPTIMIZATION-FOCUSED APPROACH
- Recognized key performance improvement opportunity (O(n) → O(√n))
- Should have asked about library imports upfront (good learning point)
- Comprehensive test coverage including edge cases and larger test values
- Clear complexity analysis with minor correction needed on space complexity

Spaced Repetition Performance: 📈 STRONG PROBLEM-SOLVING
- Different pattern type from previous hash table exercises shows versatility
- Proactive optimization thinking rather than just solving for correctness
- Good historical knowledge of Python language evolution (range behavior)
- Quick to understand and correct space complexity misconception

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)  
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(√n) - optimized from naive O(n) approach
Space Complexity: O(1) - constant space regardless of input size
Pattern Type: Mathematical optimization with iterative factor checking
Core Skills: Loop optimization, mathematical reasoning, edge case handling

Key Strengths Demonstrated:
- Proactive optimization identification and implementation
- Solid mathematical intuition for prime number properties
- Understanding of algorithmic efficiency trade-offs
- Good test case design covering edge cases and performance scenarios
- Learning agility when correcting space complexity misconception

Areas for Refinement:
- Always clarify library usage permissions before implementing
- Remember Python 3 range() behavior for space complexity analysis
- Continue building diverse algorithmic pattern recognition

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows strong transition from data structure patterns to mathematical algorithms
"""
