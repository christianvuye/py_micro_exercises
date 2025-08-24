"""
Duplicate Detection

Write a function `has_duplicates` that takes in a list as an argument.
The function should return a boolean indicating whether or not the list
contains any duplicate elements.

Example:
has_duplicates([1, 2, 3, 4]) → False
has_duplicates([1, 2, 2, 3]) → True
has_duplicates([]) → False
has_duplicates(['a', 'b', 'c', 'a']) → True

Test Cases (copy-paste below your function):

import time

def test_has_duplicates():
    # Test case 1: No duplicates
    result1 = has_duplicates([1, 2, 3, 4])
    print(f"Test 1 - No duplicates: {result1 == False}")

    # Test case 2: Has duplicates
    result2 = has_duplicates([1, 2, 2, 3])
    print(f"Test 2 - Has duplicates: {result2 == True}")

    # Test case 3: Empty list
    result3 = has_duplicates([])
    print(f"Test 3 - Empty list: {result3 == False}")

    # Test case 4: Single element
    result4 = has_duplicates([42])
    print(f"Test 4 - Single element: {result4 == False}")

    # Test case 5: All duplicates
    result5 = has_duplicates([5, 5, 5, 5])
    print(f"Test 5 - All duplicates: {result5 == True}")

    # Test case 6: String elements
    result6 = has_duplicates(['a', 'b', 'c', 'a'])
    print(f"Test 6 - String duplicates: {result6 == True}")

    # Performance comparison test
    large_list_no_dups = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_with_dups = list(range(9999)) + [5000]  # Duplicate at end

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result_no_dups = has_duplicates(large_list_no_dups)
        result_with_dups = has_duplicates(large_list_with_dups)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,000 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_has_duplicates(items):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j]:
                    return True
        return False

    start_time = time.time()
    for _ in range(10):  # Much fewer iterations due to slowness
        naive_result_no_dups = naive_has_duplicates(large_list_no_dups[:1000])
        naive_result_with_dups = naive_has_duplicates(large_list_with_dups[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 elements, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")
"""

import time


def has_duplicates(lst: list) -> bool:
    """
    Checks if the input list contains any duplicate elements.

    Args:
        lst (list): The list to check for duplicates.

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
    unique_elements = set()
    for element in lst:
        if element in unique_elements:
            return True
        else:
            unique_elements.add(element)
    return False


def test_has_duplicates():
    # Test case 1: No duplicates
    result1 = has_duplicates([1, 2, 3, 4])
    print(f"Test 1 - No duplicates: {result1 == False}")

    # Test case 2: Has duplicates
    result2 = has_duplicates([1, 2, 2, 3])
    print(f"Test 2 - Has duplicates: {result2 == True}")

    # Test case 3: Empty list
    result3 = has_duplicates([])
    print(f"Test 3 - Empty list: {result3 == False}")

    # Test case 4: Single element
    result4 = has_duplicates([42])
    print(f"Test 4 - Single element: {result4 == False}")

    # Test case 5: All duplicates
    result5 = has_duplicates([5, 5, 5, 5])
    print(f"Test 5 - All duplicates: {result5 == True}")

    # Test case 6: String elements
    result6 = has_duplicates(["a", "b", "c", "a"])
    print(f"Test 6 - String duplicates: {result6 == True}")

    # Performance comparison test
    large_list_no_dups = list(range(10000))  # [0, 1, 2, ..., 9999]
    large_list_with_dups = list(range(9999)) + [5000]  # Duplicate at end

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result_no_dups = has_duplicates(large_list_no_dups)
        result_with_dups = has_duplicates(large_list_with_dups)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,000 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_has_duplicates(items):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j]:
                    return True
        return False

    start_time = time.time()
    for _ in range(10):  # Much fewer iterations due to slowness
        naive_result_no_dups = naive_has_duplicates(large_list_no_dups[:1000])
        naive_result_with_dups = naive_has_duplicates(large_list_with_dups[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 elements, 10 iterations): {naive_time:.4f} seconds")
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_has_duplicates()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- Used set-based approach with early termination optimization
- Pattern: build tracking set while iterating, return immediately when condition met
- Achieved 42.9x performance improvement over naive O(n²) nested loops

Bug Detection & Resolution:
- Initially missing `return False` statement - function returned `None` for no duplicates
- Quickly identified and fixed when pointed to incorrect test outputs
- Demonstrates good debugging skills and attention to test results

Complexity Analysis Performance:
- Worst case: O(n) time/space ✅ (correctly identified)
- Best case: Initially said O(k) where k=set size, refined to O(1) with coaching
- Excellent understanding: "k=2 so O(2) so O(1) when we remove constants" ✅
- Shows solid grasp of Big O notation and constant elimination rules

Key Learning Moments:
- Mastered early termination optimization concept
- Understood that best case can be dramatically better than worst case
- Demonstrated that set membership checking (O(1)) beats list searching (O(n))
- Recognized how small constants collapse to O(1) in complexity analysis

Core Pattern Mastered:
Set-based existence checking with early return - foundation for many "have I seen this before?" problems
"""
