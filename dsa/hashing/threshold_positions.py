"""
Threshold Positions

Write a function `threshold_positions` that takes a list of integers and two threshold values (min_val, max_val).
Return a dictionary with three keys: "below", "within", and "above".
Each key maps to a list of indices where numbers fall into that category.

Example:
threshold_positions([5, 12, 3, 18, 7, 25, 4], 6, 15)
→ {"below": [0, 2, 6], "within": [1, 4], "above": [3, 5]}

threshold_positions([1, 2, 3], 5, 10)
→ {"below": [0, 1, 2]}

threshold_positions([20, 25, 30], 5, 15)
→ {"above": [0, 1, 2]}

Test Cases (copy-paste below your function):

import time

def test_threshold_positions():
    # Test case 1: Mixed categories
    result1 = threshold_positions([5, 12, 3, 18, 7, 25, 4], 6, 15)
    expected1 = {"below": [0, 2, 6], "within": [1, 4], "above": [3, 5]}
    print(f"Test 1 - Mixed categories: {result1 == expected1}")

    # Test case 2: All below threshold
    result2 = threshold_positions([1, 2, 3], 5, 10)
    expected2 = {"below": [0, 1, 2]}
    print(f"Test 2 - All below: {result2 == expected2}")

    # Test case 3: All above threshold
    result3 = threshold_positions([20, 25, 30], 5, 15)
    expected3 = {"above": [0, 1, 2]}
    print(f"Test 3 - All above: {result3 == expected3}")

    # Test case 4: All within range
    result4 = threshold_positions([7, 8, 9, 10], 6, 15)
    expected4 = {"within": [0, 1, 2, 3]}
    print(f"Test 4 - All within: {result4 == expected4}")

    # Test case 5: Empty list
    result5 = threshold_positions([], 5, 10)
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Test case 6: Boundary values
    result6 = threshold_positions([5, 6, 15, 16], 6, 15)
    expected6 = {"below": [0], "within": [1, 2], "above": [3]}
    print(f"Test 6 - Boundaries: {result6 == expected6}")

    # Performance test
    large_list = list(range(0, 100000, 3))  # 33k numbers

    start_time = time.time()
    for _ in range(100):
        result = threshold_positions(large_list, 30000, 60000)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (33,000 integers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    total_positions = sum(len(v) for v in threshold_positions(large_list, 30000, 60000).values())
    print(f"Total positions collected: {total_positions}")

# test_threshold_positions()
"""

import time
from collections import defaultdict


def threshold_positions(
    nums: list[int], min_val: int, max_val: int
) -> dict[str, list[int]]:
    """
    Returns the positions (indices) of elements in the input list `nums` that fall below, within, or above the specified thresholds.

    Args:
        nums (list[int]): List of integers to evaluate.
        min_val (int): Minimum threshold value.
        max_val (int): Maximum threshold value.

    Returns:
        dict[str, list[int]]: A dictionary with keys "below", "within", and "above", each mapping to a list of indices in `nums`:
            - "below": Indices of elements less than `min_val`.
            - "within": Indices of elements between `min_val` and `max_val` (inclusive).
            - "above": Indices of elements greater than `max_val`.
    """
    grouped = defaultdict(list)
    for index, num in enumerate(nums):
        if num > max_val:
            grouped["above"].append(index)
        elif num < min_val:
            grouped["below"].append(index)
        elif min_val <= num <= max_val:
            grouped["within"].append(index)
    return dict(grouped)


def test_threshold_positions():
    # Test case 1: Mixed categories
    result1 = threshold_positions([5, 12, 3, 18, 7, 25, 4], 6, 15)
    expected1 = {"below": [0, 2, 6], "within": [1, 4], "above": [3, 5]}
    print(f"Test 1 - Mixed categories: {result1 == expected1}")

    # Test case 2: All below threshold
    result2 = threshold_positions([1, 2, 3], 5, 10)
    expected2 = {"below": [0, 1, 2]}
    print(f"Test 2 - All below: {result2 == expected2}")

    # Test case 3: All above threshold
    result3 = threshold_positions([20, 25, 30], 5, 15)
    expected3 = {"above": [0, 1, 2]}
    print(f"Test 3 - All above: {result3 == expected3}")

    # Test case 4: All within range
    result4 = threshold_positions([7, 8, 9, 10], 6, 15)
    expected4 = {"within": [0, 1, 2, 3]}
    print(f"Test 4 - All within: {result4 == expected4}")

    # Test case 5: Empty list
    result5 = threshold_positions([], 5, 10)
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Test case 6: Boundary values
    result6 = threshold_positions([5, 6, 15, 16], 6, 15)
    expected6 = {"below": [0], "within": [1, 2], "above": [3]}
    print(f"Test 6 - Boundaries: {result6 == expected6}")

    # Performance test
    large_list = list(range(0, 100000, 3))  # 33k numbers

    start_time = time.time()
    for _ in range(100):
        result = threshold_positions(large_list, 30000, 60000)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (33,000 integers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    total_positions = sum(
        len(v) for v in threshold_positions(large_list, 30000, 60000).values()
    )
    print(f"Total positions collected: {total_positions}")


test_threshold_positions()


"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Threshold Positions  
Pattern: Index collection with multi-category filtering (Exercise 12 variant)

Developer's Solution Approach:
- Applied Exercise 12 pattern: enumerate → collect indices → categorize by condition
- Used three-way conditional logic for threshold comparison
- Proper boundary handling with inclusive range for "within" category
- Used defaultdict(list) for automatic list creation

Technical Implementation:
- Clean conditional structure: > max_val, < min_val, within range
- Correct boundary logic: min_val <= num <= max_val for "within"
- Proper enumerate usage for index collection
- Appropriate return type conversion to dict()

Complexity Analysis Accuracy:
- Time: O(n) - correctly identified single-pass with constant operations
- Space: O(n) - understood index storage distribution across categories
- Recognized constant factors (3 comparisons, 3 keys) don't affect Big O
- Sound reasoning about index storage: each stored exactly once

Pattern Mastery Evidence:
- Seamlessly applied Exercise 12's core structure to new domain
- Extended single-condition filtering to multi-condition categorization
- Maintained same data collection approach (defaultdict + enumerate)
- No guidance needed for pattern application

Algorithm Design Skills:
- Handled boundary conditions correctly without prompting
- Used appropriate conditional order for clarity
- Demonstrated understanding of inclusive vs exclusive ranges
- Clean documentation explaining each category

Next Focus: Complete pattern reinforcement cycle with final Exercise 13 variant.
"""
