"""
Common Elements
s
Write a function `common_elements` that takes in two lists as arguments.
The function should return a new list containing elements that appear in both lists.
You may assume that each input list does not contain duplicate element.

Example:
common_elements([1, 2, 3], [2, 3, 4]) → [2, 3]
common_elements(['a', 'b', 'c'], ['b', 'c', 'd']) → ['b', 'c']
common_elements([1, 2], [3, 4]) → []
common_elements([], [1, 2]) → []

Test Cases (copy-paste below your function):

import time

def test_common_elements():
    # Test case 1: Some common elements
    result1 = set(common_elements([1, 2, 3], [2, 3, 4]))
    expected1 = {2, 3}
    print(f"Test 1 - Some common: {result1 == expected1}")

    # Test case 2: String elements
    result2 = set(common_elements(['a', 'b', 'c'], ['b', 'c', 'd']))
    expected2 = {'b', 'c'}
    print(f"Test 2 - String common: {result2 == expected2}")

    # Test case 3: No common elements
    result3 = common_elements([1, 2], [3, 4])
    print(f"Test 3 - No common: {result3 == []}")

    # Test case 4: Empty first list
    result4 = common_elements([], [1, 2])
    print(f"Test 4 - Empty first: {result4 == []}")

    # Test case 5: Empty second list
    result5 = common_elements([1, 2], [])
    print(f"Test 5 - Empty second: {result5 == []}")

    # Test case 6: All elements common
    result6 = set(common_elements([1, 2, 3], [3, 2, 1]))
    expected6 = {1, 2, 3}
    print(f"Test 6 - All common: {result6 == expected6}")

    # Performance comparison test
    large_list_a = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_b = list(range(5000, 15000))  # [5000, 5001, ..., 14999]
    # Common elements: [5000, 5001, ..., 9999] = 5000 elements

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = common_elements(large_list_a, large_list_b)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10k + 10k elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found {len(common_elements(large_list_a, large_list_b))} common elements")

    # Reference: naive O(n*m) approach
    def naive_common_elements(a, b):
        result = []
        for item in a:
            if item in b:  # O(m) lookup for each element
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_common_elements(large_list_a[:1000], large_list_b[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n*m) time (1k + 1k elements, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_common_elements()
"""

import time


def common_elements(list_a: list, list_b: list) -> list:
    """
    Finds and returns the common elements between two lists.

    Args:
        list_a (list): The first list to compare.
        list_b (list): The second list to compare.

    Returns:
        list: A list containing the elements that are present in both list_a and list_b.
        The result contains unique elements only.

    Example:
        >>> common_elements([1, 2, 3], [2, 3, 4])
        [2, 3]
    """
    return list(set(list_a) & set(list_b))


def test_common_elements():
    # Test case 1: Some common elements
    result1 = set(common_elements([1, 2, 3], [2, 3, 4]))
    expected1 = {2, 3}
    print(f"Test 1 - Some common: {result1 == expected1}")

    # Test case 2: String elements
    result2 = set(common_elements(["a", "b", "c"], ["b", "c", "d"]))
    expected2 = {"b", "c"}
    print(f"Test 2 - String common: {result2 == expected2}")

    # Test case 3: No common elements
    result3 = common_elements([1, 2], [3, 4])
    print(f"Test 3 - No common: {result3 == []}")

    # Test case 4: Empty first list
    result4 = common_elements([], [1, 2])
    print(f"Test 4 - Empty first: {result4 == []}")

    # Test case 5: Empty second list
    result5 = common_elements([1, 2], [])
    print(f"Test 5 - Empty second: {result5 == []}")

    # Test case 6: All elements common
    result6 = set(common_elements([1, 2, 3], [3, 2, 1]))
    expected6 = {1, 2, 3}
    print(f"Test 6 - All common: {result6 == expected6}")

    # Performance comparison test
    large_list_a = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_b = list(range(5000, 15000))  # [5000, 5001, ..., 14999]
    # Common elements: [5000, 5001, ..., 9999] = 5000 elements

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = common_elements(large_list_a, large_list_b)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10k + 10k elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found {len(common_elements(large_list_a, large_list_b))} common elements")

    # Reference: naive O(n*m) approach
    def naive_common_elements(a, b):
        result = []
        for item in a:
            if item in b:  # O(m) lookup for each element
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_common_elements(large_list_a[:1000], large_list_b[:1000])
    naive_time = time.time() - start_time

    print(
        f"Naive O(n*m) time (1k + 1k elements, 10 iterations): {naive_time:.4f} seconds"
    )
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_common_elements()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- Used optimal set intersection approach: `list(set(list_a) & set(list_b))`
- Clean, Pythonic solution leveraging built-in set operations
- All test cases passed with 14.0x performance improvement over naive approach

Complexity Analysis Performance:
- Time: Correctly identified O(n+m) for set creation, refined intersection from O(s1+s2) to O(min(s1,s2)) ✅
- Initially tried to simplify O(n+m) to O(n), corrected that both input sizes matter ✅
- Space: Correctly identified as O(n+m) matching time complexity ✅
- Good intuition: "space complexity is pretty much the same as time complexity in this case"

Solution Optimization Inquiry:
- Asked about alternative approaches: "should I try to solve this in another way?"
- Demonstrated curiosity about optimization levels and understanding trade-offs
- Recognized that chosen solution is optimal for the given requirements

Key Learning Moments:
- Mastered Python set intersection operations and their underlying optimizations
- Understood that Python optimizes set intersection by iterating through smaller set
- Recognized when built-in operations are the best choice vs manual implementation

Core Pattern Mastered:
Set intersection for finding common elements - optimal O(n+m) approach using Python's built-in set operations
"""
