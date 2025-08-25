"""
Value Positions

Write a function `value_positions` that takes a list of integers and a list of target values.
Return a dictionary where keys are the target values that appear in the list,
and values are lists of all indices where that target value appears.

Example:
value_positions([1, 5, 3, 5, 1, 8, 1], [1, 5]) → {1: [0, 4, 6], 5: [1, 3]}
value_positions([2, 4, 6, 8], [2, 9]) → {2: [0]}
value_positions([1, 2, 3], [4, 5]) → {}

Test Cases (copy-paste below your function):

import time

def test_value_positions():
    # Test case 1: Multiple targets found
    result1 = value_positions([1, 5, 3, 5, 1, 8, 1], [1, 5])
    expected1 = {1: [0, 4, 6], 5: [1, 3]}
    print(f"Test 1 - Multiple targets: {result1 == expected1}")

    # Test case 2: Some targets found
    result2 = value_positions([2, 4, 6, 8], [2, 9])
    expected2 = {2: [0]}
    print(f"Test 2 - Some targets: {result2 == expected2}")

    # Test case 3: No targets found
    result3 = value_positions([1, 2, 3], [4, 5])
    expected3 = {}
    print(f"Test 3 - No targets: {result3 == expected3}")

    # Test case 4: Empty inputs
    result4 = value_positions([], [1, 2])
    result5 = value_positions([1, 2, 3], [])
    print(f"Test 4 - Empty list: {result4 == {}}")
    print(f"Test 5 - Empty targets: {result5 == {}}")

    # Test case 6: Single occurrences
    result6 = value_positions([1, 2, 3, 4], [1, 2, 3, 4])
    expected6 = {1: [0], 2: [1], 3: [2], 4: [3]}
    print(f"Test 6 - Single occurrences: {result6 == expected6}")

    # Performance test
    large_list = list(range(50000)) * 2  # 100k elements
    targets = list(range(0, 50000, 1000))  # 50 target values

    start_time = time.time()
    for _ in range(50):
        result = value_positions(large_list, targets)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (100,000 integers, 50 targets, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Targets found: {len(value_positions(large_list, targets))}")

# test_value_positions()
"""

import time
from collections import defaultdict


def value_positions(nums: list[int], targets: list[int]) -> dict[int, list[int]]:
    """
    Finds the positions of specified target values within a list of numbers.

    Args:
        nums (list[int]): The list of integers to search through.
        targets (list[int]): The list of target integers whose positions are to be found.

    Returns:
        dict[int, list[int]]: A dictionary mapping each target integer found in `nums` to a list of its indices in `nums`.
    """
    targets_dict = defaultdict(list)
    targets_set = set(targets)
    for index, num in enumerate(nums):
        if num in targets_set:
            targets_dict[num].append(index)
    return targets_dict


def test_value_positions():
    # Test case 1: Multiple targets found
    result1 = value_positions([1, 5, 3, 5, 1, 8, 1], [1, 5])
    expected1 = {1: [0, 4, 6], 5: [1, 3]}
    print(f"Test 1 - Multiple targets: {result1 == expected1}")

    # Test case 2: Some targets found
    result2 = value_positions([2, 4, 6, 8], [2, 9])
    expected2 = {2: [0]}
    print(f"Test 2 - Some targets: {result2 == expected2}")

    # Test case 3: No targets found
    result3 = value_positions([1, 2, 3], [4, 5])
    expected3 = {}
    print(f"Test 3 - No targets: {result3 == expected3}")

    # Test case 4: Empty inputs
    result4 = value_positions([], [1, 2])
    result5 = value_positions([1, 2, 3], [])
    print(f"Test 4 - Empty list: {result4 == {}}")
    print(f"Test 5 - Empty targets: {result5 == {}}")

    # Test case 6: Single occurrences
    result6 = value_positions([1, 2, 3, 4], [1, 2, 3, 4])
    expected6 = {1: [0], 2: [1], 3: [2], 4: [3]}
    print(f"Test 6 - Single occurrences: {result6 == expected6}")

    # Performance test
    large_list = list(range(50000)) * 2  # 100k elements
    targets = list(range(0, 50000, 1000))  # 50 target values

    start_time = time.time()
    for _ in range(50):
        result = value_positions(large_list, targets)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (100,000 integers, 50 targets, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Targets found: {len(value_positions(large_list, targets))}")


test_value_positions()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Value Positions
Pattern: Index collection with filtering (Exercise 12 variant)

Developer's Solution Approach:
- Applied Exercise 12 pattern: enumerate → collect indices → filter by condition
- Added set optimization: converted targets list to set for O(1) lookups
- Used defaultdict(list) for automatic list creation
- Correctly handled empty input cases

Performance Optimization:
- Identified O(n × m) bottleneck in naive list lookup approach
- Implemented O(1) set lookup optimization independently
- Final complexity: O(m + n) vs naive O(n × m)
- Demonstrated understanding of when preprocessing improves performance

Complexity Analysis Accuracy:
- Time: O(m + n) - correctly broke down all components
- Space: O(m + n) - understood key storage vs value storage breakdown
- Recognized optimization impact: O(n × m) → O(m + n)
- Minor clarification needed on dictionary space components but overall sound

Pattern Recognition Mastery:
- Successfully adapted Exercise 12's core logic to new requirements
- Added filtering condition (check if value in targets) correctly
- Maintained same data structure approach (defaultdict + enumerate)
- Applied appropriate optimization without prompting

Technical Skills Demonstrated:
- Set usage for membership testing optimization
- Proper handling of edge cases (empty inputs)
- Clean code structure with appropriate type hints
- Understanding of amortized complexity in hash operations

Next Focus: Ready for Exercise 11 variant to complete pattern reinforcement cycle.
"""
