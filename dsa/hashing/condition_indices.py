"""
Condition Indices

Write a function `condition_indices` that takes a list of integers.
Return a dictionary with different mathematical conditions as keys,
and lists of indices where numbers meet those conditions as values.

Example:
condition_indices([4, 9, 12, 16, 25, 30, 36])
→ Groups indices by mathematical properties of the numbers

condition_indices([2, 3, 5, 7, 8, 9, 11])
→ Groups indices by mathematical properties of the numbers

Test Cases (copy-paste below your function):

import time

def test_condition_indices():
    # Test case 1: Mixed numbers
    result1 = condition_indices([4, 9, 12, 16, 25, 30, 36])
    print(f"Test 1 result: {result1}")

    # Test case 2: Small numbers
    result2 = condition_indices([2, 3, 5, 7, 8, 9, 11, 13])
    print(f"Test 2 result: {result2}")

    # Test case 3: No conditions met
    result3 = condition_indices([1, 1, 1, 1])
    print(f"Test 3 result: {result3}")

    # Test case 4: All conditions met
    result4 = condition_indices([4, 16, 36, 64])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = condition_indices([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = list(range(1, 5000))  # 4999 numbers

    start_time = time.time()
    for _ in range(50):
        result = condition_indices(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (4,999 numbers, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    total_indices = sum(len(v) for v in condition_indices(large_list).values())
    print(f"Total indices collected: {total_indices}")

# test_condition_indices()
"""

import time
from collections import defaultdict
from math import isqrt


def is_prime(number: int) -> bool:
    """
    Determine if a given integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    This function checks for primality by:
    - Returning False for numbers less than 2.
    - Returning True for 2 and 3, which are prime.
    - Returning False for even numbers greater than 2.
    - Iterating through odd divisors from 3 up to the integer square root of the number.
        If any divisor evenly divides the number, it is not prime.

    Args:
            number (int): The integer to check for primality.

    Returns:
            bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    for i in range(3, isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


def condition_indices(numbers: list) -> dict[str, list[int]]:
    """
    Returns a dictionary mapping condition names to lists of indices in the input list `numbers`
    where those conditions are met.

    The function checks each number in the input list for two conditions:
    1. If the number is a perfect square, its index is added to the "perfect_squares" list.
    2. If the number is a prime number, its index is added to the "prime_numbers" list.

    Args:
        numbers (list): A list of integers to be checked for conditions.

    Returns:
        dict[str, list[int]]: A dictionary with keys "perfect_squares" and "prime_numbers",
        each mapping to a list of indices in `numbers` where the respective condition is true.

    Note:
        This function assumes the existence of `isqrt` and `is_prime` helper functions.
    """
    grouped = defaultdict(list)
    for index, number in enumerate(numbers):
        root = isqrt(number)
        if root * root == number:
            grouped["perfect_squares"].append(index)
        if is_prime(number):
            grouped["prime_numbers"].append(index)
    return dict(grouped)


def test_condition_indices():
    # Test case 1: Mixed numbers
    result1 = condition_indices([4, 9, 12, 16, 25, 30, 36])
    print(f"Test 1 result: {result1}")

    # Test case 2: Small numbers
    result2 = condition_indices([2, 3, 5, 7, 8, 9, 11, 13])
    print(f"Test 2 result: {result2}")

    # Test case 3: No conditions met
    result3 = condition_indices([1, 1, 1, 1])
    print(f"Test 3 result: {result3}")

    # Test case 4: All conditions met
    result4 = condition_indices([4, 16, 36, 64])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = condition_indices([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = list(range(1, 5000))  # 4999 numbers

    start_time = time.time()
    for _ in range(50):
        result = condition_indices(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (4,999 numbers, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    total_indices = sum(len(v) for v in condition_indices(large_list).values())
    print(f"Total indices collected: {total_indices}")


test_condition_indices()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Condition Indices
Pattern: Multi-condition index collection (Exercise 12 variant)

Developer's Solution Approach:
- Applied Exercise 12 pattern: enumerate → check conditions → collect indices  
- Implemented custom prime checker using trial division
- Used isqrt() for perfect square detection with root * root verification
- Proper handling of multiple conditions per number (can be both prime and perfect square)

Technical Implementation:
- Well-documented prime checking algorithm with early returns
- Efficient perfect square check avoiding floating-point issues
- Clean enumerate + conditional structure
- Appropriate use of defaultdict(list) for automatic list creation

Complexity Analysis Challenges:
- Correctly identified main algorithmic components
- Overcomplicated with unnecessary implementation detail research
- Missed that prime checking is O(sqrt(m)), not O(n)
- Final complexity: O(n × sqrt(m)) - prime checking dominates
- Space analysis accurate: O(n)

Algorithm Design Skills:
- Chose appropriate algorithms for both mathematical conditions
- Avoided floating-point precision issues with integer-only operations
- Implemented efficient trial division with proper bounds
- Good separation of concerns with helper function

Pattern Mastery Achievement:
Successfully completed all three pattern reinforcement cycles:
- Exercise 11 variants: signature-based grouping (anagrams → palindromes → digit sums)
- Exercise 12 variants: index collection (duplicates → value positions → threshold positions → condition indices)  
- Exercise 13 variants: structural analysis (word patterns → digit patterns → character type patterns)

Ready for Tier 3: Real-world problem-solving with advanced pattern combinations.
"""
