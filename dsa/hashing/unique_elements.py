"""
Unique Elements

Write a function `unique_elements` that takes in two lists as arguments.
The function should return a new list containing elements that are in either
list but not both lists (elements that are unique to each list).
You may assume that each input list does not contain duplicate elements.

Example:
unique_elements([1, 2, 3], [2, 3, 4]) → [1, 4]
unique_elements(['a', 'b', 'c'], ['b', 'c', 'd']) → ['a', 'd']
unique_elements([1, 2], [3, 4]) → [1, 2, 3, 4]
unique_elements([], [1, 2]) → [1, 2]

Test Cases (copy-paste below your function):

import time

def test_unique_elements():
    # Test case 1: Some unique elements
    result1 = set(unique_elements([1, 2, 3], [2, 3, 4]))
    expected1 = {1, 4}
    print(f"Test 1 - Some unique: {result1 == expected1}")

    # Test case 2: String elements
    result2 = set(unique_elements(['a', 'b', 'c'], ['b', 'c', 'd']))
    expected2 = {'a', 'd'}
    print(f"Test 2 - String unique: {result2 == expected2}")

    # Test case 3: No common elements (all unique)
    result3 = set(unique_elements([1, 2], [3, 4]))
    expected3 = {1, 2, 3, 4}
    print(f"Test 3 - All unique: {result3 == expected3}")

    # Test case 4: Empty first list
    result4 = set(unique_elements([], [1, 2]))
    expected4 = {1, 2}
    print(f"Test 4 - Empty first: {result4 == expected4}")

    # Test case 5: Empty second list
    result5 = set(unique_elements([1, 2], []))
    expected5 = {1, 2}
    print(f"Test 5 - Empty second: {result5 == expected5}")

    # Test case 6: All elements common (none unique)
    result6 = unique_elements([1, 2, 3], [3, 2, 1])
    print(f"Test 6 - No unique: {result6 == []}")

    # Performance comparison test
    large_list_a = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_b = list(range(5000, 15000))  # [5000, 5001, ..., 14999]
    # Unique elements: [0,1,2,...,4999] + [10000,10001,...,14999] = 10000 elements

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = unique_elements(large_list_a, large_list_b)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10k + 10k elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found {len(unique_elements(large_list_a, large_list_b))} unique elements")

    # Reference: naive O(n*m) approach
    def naive_unique_elements(a, b):
        result = []
        for item in a:
            if item not in b:  # O(m) lookup
                result.append(item)
        for item in b:
            if item not in a:  # O(n) lookup
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_unique_elements(large_list_a[:1000], large_list_b[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n*m) time (1k + 1k elements, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_unique_elements()
"""

import time


def unique_elements(list_a, list_b):
    """
    Returns a list of elements that are unique to either list_a or list_b.

    This function computes the symmetric difference between two lists,
    returning elements that are present in one list but not both.

    Args:
        list_a (list): The first list of elements.
        list_b (list): The second list of elements.

    Returns:
        list: A list containing elements unique to either list_a or list_b.

    Example:
        >>> unique_elements([1, 2, 3], [2, 3, 4])
        [1, 4]
    """
    return list(set(list_a) ^ set(list_b))


def test_unique_elements():
    # Test case 1: Some unique elements
    result1 = set(unique_elements([1, 2, 3], [2, 3, 4]))
    expected1 = {1, 4}
    print(f"Test 1 - Some unique: {result1 == expected1}")

    # Test case 2: String elements
    result2 = set(unique_elements(["a", "b", "c"], ["b", "c", "d"]))
    expected2 = {"a", "d"}
    print(f"Test 2 - String unique: {result2 == expected2}")

    # Test case 3: No common elements (all unique)
    result3 = set(unique_elements([1, 2], [3, 4]))
    expected3 = {1, 2, 3, 4}
    print(f"Test 3 - All unique: {result3 == expected3}")

    # Test case 4: Empty first list
    result4 = set(unique_elements([], [1, 2]))
    expected4 = {1, 2}
    print(f"Test 4 - Empty first: {result4 == expected4}")

    # Test case 5: Empty second list
    result5 = set(unique_elements([1, 2], []))
    expected5 = {1, 2}
    print(f"Test 5 - Empty second: {result5 == expected5}")

    # Test case 6: All elements common (none unique)
    result6 = unique_elements([1, 2, 3], [3, 2, 1])
    print(f"Test 6 - No unique: {result6 == []}")

    # Performance comparison test
    large_list_a = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_b = list(range(5000, 15000))  # [5000, 5001, ..., 14999]
    # Unique elements: [0,1,2,...,4999] + [10000,10001,...,14999] = 10000 elements

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = unique_elements(large_list_a, large_list_b)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10k + 10k elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found {len(unique_elements(large_list_a, large_list_b))} unique elements")

    # Reference: naive O(n*m) approach
    def naive_unique_elements(a, b):
        result = []
        for item in a:
            if item not in b:  # O(m) lookup
                result.append(item)
        for item in b:
            if item not in a:  # O(n) lookup
                result.append(item)
        return result

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_unique_elements(large_list_a[:1000], large_list_b[:1000])
    naive_time = time.time() - start_time

    print(
        f"Naive O(n*m) time (1k + 1k elements, 10 iterations): {naive_time:.4f} seconds"
    )
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_unique_elements()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- Used optimal symmetric difference approach: `list(set(list_a) ^ set(list_b))`
- Demonstrated knowledge of mathematical set operations (symmetric difference)
- Excellent docstring mentioning "symmetric difference" concept correctly
- All test cases passed with 27.1x performance improvement

Complexity Analysis Performance:
- Time: Correctly identified O(n+m) for all operations ✅
- Key insight: Unlike intersection, symmetric difference cannot be optimized because you must examine all elements in both sets
- Space: Correctly identified as O(n+m) ✅
- Perfect understanding: "you have to go through all the elements in each set, I would imagine?"

Professional Communication:
- Called out inconsistency in feedback: "So I was right not on most points, but all points?" 
- Shows attention to detail and confidence in correct analysis
- Demonstrates strong self-advocacy skills

Key Learning Moments:
- Mastered distinction between intersection optimization vs symmetric difference requirements
- Understood why certain set operations can be optimized while others cannot
- Applied mathematical concepts correctly to programming problem

Core Pattern Mastered:
Set symmetric difference for finding elements unique to either set - optimal O(n+m) approach using Python's XOR operator
"""
