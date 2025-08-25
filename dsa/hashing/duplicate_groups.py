"""
Duplicate Groups

Write a function `duplicate_groups` that takes a list of integers.
Return a dictionary where keys are the numbers that appear more than once,
and values are lists of all indices where that number appears.

Example:
duplicate_groups([1, 2, 3, 2, 1, 4, 1]) → {1: [0, 4, 6], 2: [1, 3]}
duplicate_groups([5, 5, 5]) → {5: [0, 1, 2]}
duplicate_groups([1, 2, 3]) → {}

Test Cases (copy-paste below your function):

import time

def test_duplicate_groups():
    # Test case 1: Mixed duplicates
    result1 = duplicate_groups([1, 2, 3, 2, 1, 4, 1])
    expected1 = {1: [0, 4, 6], 2: [1, 3]}
    print(f"Test 1 - Mixed duplicates: {result1 == expected1}")

    # Test case 2: All same number
    result2 = duplicate_groups([5, 5, 5])
    expected2 = {5: [0, 1, 2]}
    print(f"Test 2 - All same: {result2 == expected2}")

    # Test case 3: No duplicates
    result3 = duplicate_groups([1, 2, 3])
    expected3 = {}
    print(f"Test 3 - No duplicates: {result3 == expected3}")

    # Test case 4: Empty list
    result4 = duplicate_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Test case 5: Two pairs
    result5 = duplicate_groups([1, 2, 1, 2])
    expected5 = {1: [0, 2], 2: [1, 3]}
    print(f"Test 5 - Two pairs: {result5 == expected5}")

    # Performance test
    large_list = list(range(10000)) * 3  # 30k elements, each appears 3 times

    start_time = time.time()
    for _ in range(100):
        result = duplicate_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (30,000 integers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(duplicate_groups(large_list))}")

    # Naive O(n²) approach for comparison
    def naive_duplicate_groups(nums):
        result = {}
        for i, num in enumerate(nums):
            indices = []
            for j, other_num in enumerate(nums):
                if num == other_num:
                    indices.append(j)
            if len(indices) > 1:
                result[num] = indices
        return result

    start_time = time.time()
    for _ in range(10):  # Fewer iterations due to slowness
        naive_result = naive_duplicate_groups(large_list[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 integers, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time * 30 * 10) / optimized_time:.1f}x faster")

# test_duplicate_groups()
"""

import time
from collections import defaultdict


def duplicate_groups(nums: list[int]) -> dict[int, list[int]]:
    """
    Finds all duplicate elements in the input list and groups their indices.

    Args:
        nums (list[int]): A list of integers to search for duplicates.

    Returns:
        dict[int, list[int]]: A dictionary where each key is a duplicated integer from the input list,
            and the value is a list of indices where that integer occurs. Only integers that appear
            more than once are included.
    """
    nums_frequency = defaultdict(list)
    for index, num in enumerate(nums):
        nums_frequency[num].append(index)
    return {num: indices for num, indices in nums_frequency.items() if len(indices) > 1}


def test_duplicate_groups():
    # Test case 1: Mixed duplicates
    result1 = duplicate_groups([1, 2, 3, 2, 1, 4, 1])
    expected1 = {1: [0, 4, 6], 2: [1, 3]}
    print(f"Test 1 - Mixed duplicates: {result1 == expected1}")

    # Test case 2: All same number
    result2 = duplicate_groups([5, 5, 5])
    expected2 = {5: [0, 1, 2]}
    print(f"Test 2 - All same: {result2 == expected2}")

    # Test case 3: No duplicates
    result3 = duplicate_groups([1, 2, 3])
    expected3 = {}
    print(f"Test 3 - No duplicates: {result3 == expected3}")

    # Test case 4: Empty list
    result4 = duplicate_groups([])
    expected4 = {}
    print(f"Test 4 - Empty: {result4 == expected4}")

    # Test case 5: Two pairs
    result5 = duplicate_groups([1, 2, 1, 2])
    expected5 = {1: [0, 2], 2: [1, 3]}
    print(f"Test 5 - Two pairs: {result5 == expected5}")

    # Performance test
    large_list = list(range(10000)) * 3  # 30k elements, each appears 3 times

    start_time = time.time()
    for _ in range(100):
        result = duplicate_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (30,000 integers, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(duplicate_groups(large_list))}")

    # Naive O(n²) approach for comparison
    def naive_duplicate_groups(nums):
        result = {}
        for i, num in enumerate(nums):
            indices = []
            for j, other_num in enumerate(nums):
                if num == other_num:
                    indices.append(j)
            if len(indices) > 1:
                result[num] = indices
        return result

    start_time = time.time()
    for _ in range(10):  # Fewer iterations due to slowness
        naive_result = naive_duplicate_groups(large_list[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 integers, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time * 30 * 10) / optimized_time:.1f}x faster")


test_duplicate_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Duplicate Groups  
Pattern: Single-pass index collection with hash-based grouping

Developer's Solution Approach:
- Used defaultdict(list) for automatic list initialization
- Single pass with enumerate to collect (index, value) pairs
- Dictionary comprehension to filter out single occurrences
- Clean separation: collect all, then filter duplicates

Complexity Analysis Process:
Initial confusion about dictionary operation costs, but corrected well:
- Time: O(n) - linear pass + linear filter, not O(n×i)
- Space: O(n) with ~2n actual usage (original + indices)
- Correctly identified that dictionary operations are O(1) amortized
- Understood practical vs theoretical space complexity differences

Technical Understanding:
- Recognized the "can't know until complete" nature of duplicate detection
- Chose collect-then-filter over two-pass approach for efficiency
- Fixed type hint error independently (dict[int, int] → dict[int, list[int]])
- Demonstrated strong grasp of enumerate vs manual index tracking

Key Learning Moments:
- Dictionary operations are O(1) regardless of stored values
- Space complexity counts quantity of data, not the values themselves
- Constant factors matter for practical memory planning (2n vs n)
- Single-pass algorithms can still require post-processing

Algorithm Design Insight:
"No way to know duplicates until complete list" - correctly identified the fundamental constraint that drives the collect-then-filter approach.

Next Focus: Continue building hash-based pattern recognition with more complex grouping scenarios.
"""
