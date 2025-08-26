"""
Sum Digit Groups

Write a function `sum_digit_groups` that takes a list of integers.
Group numbers based on a calculated property of their digits.

Example:
sum_digit_groups([123, 456, 789, 321, 147, 258])
→ Groups numbers by their calculated digit property

sum_digit_groups([11, 22, 33, 12, 21, 13])
→ Groups numbers by their calculated digit property

Test Cases (copy-paste below your function):

import time

def test_sum_digit_groups():
    # Test case 1: Various numbers
    result1 = sum_digit_groups([123, 456, 789, 321, 147, 258])
    print(f"Test 1 result: {result1}")

    # Test case 2: Two-digit numbers
    result2 = sum_digit_groups([11, 22, 33, 12, 21, 13, 31])
    print(f"Test 2 result: {result2}")

    # Test case 3: Single digits
    result3 = sum_digit_groups([1, 2, 3, 4, 5])
    print(f"Test 3 result: {result3}")

    # Test case 4: Same calculated property
    result4 = sum_digit_groups([123, 321, 231, 132])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = sum_digit_groups([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = list(range(100, 10000, 7))  # ~1400 numbers

    start_time = time.time()
    for _ in range(100):
        result = sum_digit_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (1,400 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(sum_digit_groups(large_list))}")

# test_sum_digit_groups()
"""

import time
from collections import defaultdict


def sum_digit_groups(numbers: list[int]) -> dict[int, list[int]]:
    """
    Groups integers by the sum of their digits.

    Args:
        numbers (list[int]): A list of integers to be grouped.

    Returns:
        dict[int, list[int]]: A dictionary where each key is a digit sum,
            and the corresponding value is a list of integers from the input
            whose digits sum to that key.
    """
    grouped = defaultdict(list)
    for number in numbers:
        sum = 0
        number_str = str(number)
        for digit in number_str:
            sum += int(digit)
        grouped[sum].append(number)
    return dict(grouped)


def test_sum_digit_groups():
    # Test case 1: Various numbers
    result1 = sum_digit_groups([123, 456, 789, 321, 147, 258])
    print(f"Test 1 result: {result1}")

    # Test case 2: Two-digit numbers
    result2 = sum_digit_groups([11, 22, 33, 12, 21, 13, 31])
    print(f"Test 2 result: {result2}")

    # Test case 3: Single digits
    result3 = sum_digit_groups([1, 2, 3, 4, 5])
    print(f"Test 3 result: {result3}")

    # Test case 4: Same calculated property
    result4 = sum_digit_groups([123, 321, 231, 132])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = sum_digit_groups([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = list(range(100, 10000, 7))  # ~1400 numbers

    start_time = time.time()
    for _ in range(100):
        result = sum_digit_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (1,400 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(sum_digit_groups(large_list))}")


test_sum_digit_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Sum Digit Groups
Pattern: Calculated signature-based grouping (Exercise 11 variant)

Developer's Solution Approach:
- Applied Exercise 11 pattern: calculate signature (digit sum) → group by signature
- Used string conversion + digit iteration for sum calculation
- Proper use of defaultdict(list) and dict() return conversion
- Clean loop structure with accumulator variable

Technical Implementation:
- Correct digit sum calculation through string iteration
- Appropriate type conversion (str→int for digits, sum as grouping key)
- Proper handling of edge cases (empty list)
- Sound algorithm structure following established pattern

Complexity Analysis:
- Time: O(n × m) - correct conclusion despite muddled string conversion explanation
- Space: O(n) - correctly identified dominant storage factor
- Minor confusion about digit count vs single digit processing
- Overall understanding of nested loop complexity sound

Pattern Recognition:
- Seamlessly applied Exercise 11 structure to new calculation domain
- Extended from character-based signatures to numeric property signatures
- Maintained consistent grouping approach with minimal guidance
- Demonstrated solid understanding of signature-based grouping concept

Algorithm Design:
- Chose straightforward string-based approach for digit extraction
- Used accumulator pattern for sum calculation
- Proper variable naming and structure
- No unnecessary complexity or optimization premature for learning context

Ready for final Tier 2 pattern reinforcement exercise.
"""
