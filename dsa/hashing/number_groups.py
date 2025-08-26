"""
Number Groups

Write a function `number_groups` that takes a list of integers.
Group numbers that share a common mathematical property together.

Example:
number_groups([121, 131, 141, 222, 333, 123, 456])
→ Groups numbers by their mathematical pattern

Test Cases (copy-paste below your function):

import time

def test_number_groups():
    # Test case 1: Mixed numbers
    result1 = number_groups([121, 131, 141, 222, 333, 123, 456])
    print(f"Test 1 result: {result1}")

    # Test case 2: All same property
    result2 = number_groups([121, 131, 141, 151])
    print(f"Test 2 result: {result2}")

    # Test case 3: No common property
    result3 = number_groups([123, 456, 789])
    print(f"Test 3 result: {result3}")

    # Test case 4: Empty list
    result4 = number_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Performance test
    large_list = list(range(100, 1000)) + list(range(1000, 100, -1))

    start_time = time.time()
    for _ in range(100):
        result = number_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (1,800 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(number_groups(large_list))}")

# test_number_groups()
"""

import time
from collections import defaultdict


def number_groups(numbers: list[int]) -> dict[str, list[int]]:
    """
    Groups a list of integers into 'palindrome' and 'non-palindrome' categories.

    A palindrome number reads the same forwards and backwards (e.g., 121, 44).
    Non-palindrome numbers do not.

    Args:
        numbers (list[int]): List of integers to group.

    Returns:
        dict[str, list[int]]: Dictionary with keys 'palindrome' and 'non-palindrome',
        each mapping to a list of corresponding numbers.
    """
    grouped = defaultdict(list)
    for number in numbers:
        number_str = str(number)
        number_str_rev = "".join(reversed(number_str))
        number_reversed = int(number_str_rev)
        if number_reversed == number:
            grouped["palindrome"].append(number)
        else:
            grouped["non-palindrome"].append(number)
    return dict(grouped)


def test_number_groups():
    # Test case 1: Mixed numbers
    result1 = number_groups([121, 131, 141, 222, 333, 123, 456])
    print(f"Test 1 result: {result1}")

    # Test case 2: All same property
    result2 = number_groups([121, 131, 141, 151])
    print(f"Test 2 result: {result2}")

    # Test case 3: No common property
    result3 = number_groups([123, 456, 789])
    print(f"Test 3 result: {result3}")

    # Test case 4: Empty list
    result4 = number_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Performance test
    large_list = list(range(100, 1000)) + list(range(1000, 100, -1))

    start_time = time.time()
    for _ in range(100):
        result = number_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (1,800 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(number_groups(large_list))}")


test_number_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Number Groups (Palindrome Detection)
Pattern: Signature-based grouping (Exercise 11 variant)

Developer's Solution Evolution:
- Initially implemented incorrect assignment (= instead of .append())
- Self-caught error immediately after submission
- Applied Exercise 11 pattern correctly: signature → group by signature
- Used string reversal approach for palindrome detection

Technical Implementation:
- Palindrome detection: str() → reversed() → join() → int() → comparison
- Used defaultdict(list) for automatic list creation
- Proper type hints and documentation
- Clean conditional logic with appropriate signatures ("palindrome" vs "non-palindrome")

Complexity Analysis Mastery:
- Time: O(n × log m) - correctly identified per-number operations cost
- Space: O(n) - understood temporary vs persistent storage distinction
- Accurately analyzed string operation costs individually
- Minor clarification needed on temporary variable lifecycle

Algorithm Design Choices:
- Chose string-based palindrome detection over mathematical approach
- Acknowledged potential optimization concerns but prioritized pattern practice
- Demonstrated understanding of bottleneck analysis (main loop vs per-item operations)

Self-Correction Skills:
- Immediately identified logic error after code submission
- Fixed type hint and append logic without prompting
- Maintained focus on pattern mastery over premature optimization

Pattern Recognition:
Successfully applied Exercise 11's structure to completely different domain (strings→numbers, anagram detection→palindrome detection), demonstrating solid understanding of signature-based grouping pattern.

Next Focus: Continue pattern reinforcement - one more variant per pattern type before advancing.
"""
