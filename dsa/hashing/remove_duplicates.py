"""
Remove Duplicates

Write a function `remove_duplicates` that takes in a list as an argument.
The function should return a new list with duplicate elements removed,
preserving the order of first occurrence.

Example:
remove_duplicates([1, 2, 2, 3, 1, 4]) → [1, 2, 3, 4]
remove_duplicates(['a', 'b', 'a', 'c']) → ['a', 'b', 'c']
remove_duplicates([]) → []
remove_duplicates([5, 5, 5]) → [5]

Test Cases (copy-paste below your function):

import time

def test_remove_duplicates():
    # Test case 1: Basic functionality
    result1 = remove_duplicates([1, 2, 2, 3, 1, 4])
    expected1 = [1, 2, 3, 4]
    print(f"Test 1 - Basic: {result1 == expected1}")

    # Test case 2: String elements
    result2 = remove_duplicates(['a', 'b', 'a', 'c'])
    expected2 = ['a', 'b', 'c']
    print(f"Test 2 - Strings: {result2 == expected2}")

    # Test case 3: Empty list
    result3 = remove_duplicates([])
    expected3 = []
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: All same elements
    result4 = remove_duplicates([5, 5, 5])
    expected4 = [5]
    print(f"Test 4 - All same: {result4 == expected4}")

    # Test case 5: No duplicates
    result5 = remove_duplicates([1, 2, 3, 4])
    expected5 = [1, 2, 3, 4]
    print(f"Test 5 - No duplicates: {result5 == expected5}")

    # Test case 6: Order preservation
    result6 = remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5])
    expected6 = [3, 1, 4, 5, 9, 2, 6]
    print(f"Test 6 - Order preserved: {result6 == expected6}")

    # Performance comparison test
    large_list = list(range(5000)) * 2  # [0,1,2...4999,0,1,2...4999] = 10,000 elements

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = remove_duplicates(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,000 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Result length: {len(remove_duplicates(large_list))}")

    # Reference: naive O(n²) approach
    def naive_remove_duplicates(items):
        result = []
        for item in items:
            # Check if item already in result (O(n) operation)
            if item not in result:
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_remove_duplicates(large_list)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (10,000 elements, 100 iterations): {naive_time:.4f} seconds")
    print(f"Speedup: ~{naive_time/optimized_time:.1f}x faster")

# Run tests after implementing your function
# test_remove_duplicates()
"""

import time


def remove_duplicates(items: list) -> list:
    """
    Removes duplicate elements from a list while preserving the original order.

    Args:
        items (list): The list from which to remove duplicates.

    Returns:
        list: A new list containing only the first occurrence of each element from the input list, in the same order.
    """
    return list(dict.fromkeys(items))


def test_remove_duplicates():
    # Test case 1: Basic functionality
    result1 = remove_duplicates([1, 2, 2, 3, 1, 4])
    expected1 = [1, 2, 3, 4]
    print(f"Test 1 - Basic: {result1 == expected1}")

    # Test case 2: String elements
    result2 = remove_duplicates(["a", "b", "a", "c"])
    expected2 = ["a", "b", "c"]
    print(f"Test 2 - Strings: {result2 == expected2}")

    # Test case 3: Empty list
    result3 = remove_duplicates([])
    expected3 = []
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: All same elements
    result4 = remove_duplicates([5, 5, 5])
    expected4 = [5]
    print(f"Test 4 - All same: {result4 == expected4}")

    # Test case 5: No duplicates
    result5 = remove_duplicates([1, 2, 3, 4])
    expected5 = [1, 2, 3, 4]
    print(f"Test 5 - No duplicates: {result5 == expected5}")

    # Test case 6: Order preservation
    result6 = remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5])
    expected6 = [3, 1, 4, 5, 9, 2, 6]
    print(f"Test 6 - Order preserved: {result6 == expected6}")

    # Performance comparison test
    large_list = list(range(5000)) * 2  # [0,1,2...4999,0,1,2...4999] = 10,000 elements

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = remove_duplicates(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,000 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Result length: {len(remove_duplicates(large_list))}")

    # Reference: naive O(n²) approach
    def naive_remove_duplicates(items):
        result = []
        for item in items:
            # Check if item already in result (O(n) operation)
            if item not in result:
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_remove_duplicates(large_list)
    naive_time = time.time() - start_time

    print(
        f"Naive O(n²) time (10,000 elements, 100 iterations): {naive_time:.4f} seconds"
    )
    print(f"Speedup: ~{naive_time / optimized_time:.1f}x faster")


# Run tests after implementing your function
test_remove_duplicates()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Final Implementation:
- Used `dict.fromkeys(items)` - extremely elegant and sophisticated solution
- Leveraged dict properties: unique keys + insertion order preservation  
- Shows deep Python knowledge beyond typical set-based approaches

Complexity Analysis Performance:
- Time: O(n) ✅ (recognized two O(n) operations → O(n) overall)
- Space: O(k) where k=unique elements ✅
- Excellent insight: "if lots of dupes final list smaller, but dict has large amount of keys" ✅

Core Pattern Mastered:
Advanced deduplication using dict properties - demonstrates mastery beyond basic hashing patterns
"""
