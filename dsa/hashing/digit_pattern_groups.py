"""
Digit Pattern Groups

Write a function `digit_pattern_groups` that takes a list of integers.
Group numbers that have the same digit arrangement pattern.

Numbers have the same pattern if their digits follow the same
ascending/descending/equal relationships.

Example:
digit_pattern_groups([123, 456, 321, 654, 111, 222])
→ {"asc": [123, 456], "desc": [321, 654], "same": [111, 222]}

digit_pattern_groups([135, 246, 531, 642])
→ {"asc": [135, 246], "desc": [531, 642]}

Test Cases (copy-paste below your function):

import time

def test_digit_pattern_groups():
    # Test case 1: Mixed patterns
    result1 = digit_pattern_groups([123, 456, 321, 654, 111, 222])
    # Normalize for comparison
    normalized1 = {k: sorted(v) for k, v in result1.items()}
    expected1 = {"asc": [123, 456], "desc": [321, 654], "same": [111, 222]}
    expected1_normalized = {k: sorted(v) for k, v in expected1.items()}
    print(f"Test 1 - Mixed patterns: {normalized1 == expected1_normalized}")

    # Test case 2: Only ascending
    result2 = digit_pattern_groups([135, 246, 789])
    normalized2 = {k: sorted(v) for k, v in result2.items()}
    expected2 = {"asc": [135, 246, 789]}
    expected2_normalized = {k: sorted(v) for k, v in expected2.items()}
    print(f"Test 2 - Only ascending: {normalized2 == expected2_normalized}")

    # Test case 3: Single digits
    result3 = digit_pattern_groups([1, 2, 3])
    print(f"Test 3 - Single digits: {len(result3) == 1}")  # All same pattern

    # Test case 4: Empty list
    result4 = digit_pattern_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Performance test with simple timing
    large_list = list(range(100, 1000)) + list(range(999, 99, -1))  # 1800 numbers

    start_time = time.time()
    for _ in range(100):
        result = digit_pattern_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (1,800 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

# test_digit_pattern_groups()
"""

import time
from collections import defaultdict


def digit_pattern_groups(numbers: list[int]) -> dict[str, list[int]]:
    """
    Groups a list of integers based on the pattern of their first and last digits.

    Each number is classified into one of three groups:
    - "asc": if the last digit is greater than the first digit
    - "desc": if the first digit is greater than the last digit
    - "same": if the first and last digits are equal

    Args:
        numbers (list[int]): A list of integers to be grouped.

    Returns:
        dict[str, list[int]]: A dictionary with keys "asc", "desc", and "same",
            each mapping to a list of integers belonging to that group.
    """
    grouped = defaultdict(list)
    for number in numbers:
        number_str = str(number)
        first_number = int(number_str[0])
        last_number = int(number_str[-1])
        if first_number > last_number:
            grouped["desc"].append(number)
        elif last_number > first_number:
            grouped["asc"].append(number)
        elif last_number == first_number:
            grouped["same"].append(number)
    return grouped


def test_digit_pattern_groups():
    # Test case 1: Mixed patterns
    result1 = digit_pattern_groups([123, 456, 321, 654, 111, 222])
    # Normalize for comparison
    normalized1 = {k: sorted(v) for k, v in result1.items()}
    expected1 = {"asc": [123, 456], "desc": [321, 654], "same": [111, 222]}
    expected1_normalized = {k: sorted(v) for k, v in expected1.items()}
    print(f"Test 1 - Mixed patterns: {normalized1 == expected1_normalized}")

    # Test case 2: Only ascending
    result2 = digit_pattern_groups([135, 246, 789])
    normalized2 = {k: sorted(v) for k, v in result2.items()}
    expected2 = {"asc": [135, 246, 789]}
    expected2_normalized = {k: sorted(v) for k, v in expected2.items()}
    print(f"Test 2 - Only ascending: {normalized2 == expected2_normalized}")

    # Test case 3: Single digits
    result3 = digit_pattern_groups([1, 2, 3])
    print(f"Test 3 - Single digits: {len(result3) == 1}")  # All same pattern

    # Test case 4: Empty list
    result4 = digit_pattern_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Performance test with simple timing
    large_list = list(range(100, 1000)) + list(range(999, 99, -1))  # 1800 numbers

    start_time = time.time()
    for _ in range(100):
        result = digit_pattern_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (1,800 numbers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")


test_digit_pattern_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Digit Pattern Groups  
Pattern: Signature-based grouping (reinforcement of Exercise 13 pattern)

Developer's Learning Strategy:
- Requested pattern reinforcement rather than complexity advancement
- Recognized need to master core concepts before progressing
- Applied Exercise 13's pattern (analyze → create signature → group by signature)
- Used constraint-based optimization (first/last digit shortcut)

Solution Implementation:
- Correctly identified first < last, first > last, first == last approach
- Used string conversion with indexing for digit extraction
- Applied defaultdict(list) for automatic group initialization
- Clean conditional logic with proper signature assignment

Complexity Analysis Progression:
Initially confused log complexity in different contexts:
- Mixed up array length n vs number value n in string conversion
- Learned relationship between digit count and logarithm: digits ≈ log₁₀(value)
- Final understanding: O(n × log m) where n=array size, m=max number value
- Space: O(n) - correctly identified linear storage of input data

Technical Learning Moments:
- Integer-to-string conversion: division by 10, collect remainders
- String-to-integer conversion: multiply by 10, add digit value
- Both algorithms process each digit once, explaining log/linear complexity
- Temporary variable lifecycle: created/destroyed per iteration, not accumulated

Algorithm Understanding:
- Applied pattern recognition from previous exercise successfully
- Used problem constraints to optimize approach (clean patterns only)
- Distinguished between temporary storage vs persistent storage in complexity
- Understood why O(n) space is optimal for this problem type

Communication & Process:
- Caught instructor error in log explanation and requested clarification
- Asked for detailed algorithm explanations to build foundational understanding
- Requested both integer→string and string→integer algorithm details
- Demonstrated self-awareness about learning needs and pacing

Pattern Mastery Evidence:
Successfully transferred Exercise 13 approach to new domain with minimal guidance, indicating solid pattern recognition skills.

Next Focus: Continue pattern reinforcement with Exercise 12 variant before advancing complexity.
"""
