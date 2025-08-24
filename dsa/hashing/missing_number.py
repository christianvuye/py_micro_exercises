"""
Missing Number

Write a function `missing_number` that takes in a list of integers from 0 to n,
but with exactly one number missing from the sequence. The function should
return the missing number.

Example:
missing_number([3, 0, 1]) → 2
missing_number([0, 1]) → 2
missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) → 8
missing_number([1]) → 0

Test Cases (copy-paste below your function):

import time

def test_missing_number():
    # Test case 1: Missing middle number
    result1 = missing_number([3, 0, 1])
    print(f"Test 1 - Missing middle: {result1 == 2}")

    # Test case 2: Missing last number
    result2 = missing_number([0, 1])
    print(f"Test 2 - Missing last: {result2 == 2}")

    # Test case 3: Larger sequence
    result3 = missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(f"Test 3 - Larger sequence: {result3 == 8}")

    # Test case 4: Missing first number
    result4 = missing_number([1])
    print(f"Test 4 - Missing first: {result4 == 0}")

    # Test case 5: Missing from beginning
    result5 = missing_number([1, 2, 3, 4])
    print(f"Test 5 - Missing zero: {result5 == 0}")

    # Test case 6: Single element missing last
    result6 = missing_number([0])
    print(f"Test 6 - Single element: {result6 == 1}")

    # Performance comparison test
    # Create list of 0 to 9999 with 5000 missing
    large_list = list(range(10000))
    large_list.remove(5000)  # Remove middle element

    # Time your optimized solution
    start_time = time.time()
    for _ in range(1000):
        result = missing_number(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (9,999 elements, 1000 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found missing number: {missing_number(large_list)}")

    # Reference: naive approach checking each number
    def naive_missing_number(nums):
        nums_sorted = sorted(nums)  # O(n log n)
        for i in range(len(nums_sorted) + 1):
            if i >= len(nums_sorted) or nums_sorted[i] != i:
                return i
        return len(nums_sorted)

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_missing_number(large_list[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n log n) time (1,000 elements, 100 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/100*1000)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_missing_number()
"""

import time


def missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list containing n distinct numbers taken from the range 0 to n.

    Args:
        nums (list[int]): List of n distinct integers from the range 0 to n, with one number missing.

    Returns:
        int: The missing number from the range 0 to n.
    """
    n = len(nums)
    nums_complete = [num for num in range(n + 1)]
    (diff,) = set(nums_complete) - set(nums)
    return diff


def test_missing_number():
    # Test case 1: Missing middle number
    result1 = missing_number([3, 0, 1])
    print(f"Test 1 - Missing middle: {result1 == 2}")

    # Test case 2: Missing last number
    result2 = missing_number([0, 1])
    print(f"Test 2 - Missing last: {result2 == 2}")

    # Test case 3: Larger sequence
    result3 = missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(f"Test 3 - Larger sequence: {result3 == 8}")

    # Test case 4: Missing first number
    result4 = missing_number([1])
    print(f"Test 4 - Missing first: {result4 == 0}")

    # Test case 5: Missing from beginning
    result5 = missing_number([1, 2, 3, 4])
    print(f"Test 5 - Missing zero: {result5 == 0}")

    # Test case 6: Single element missing last
    result6 = missing_number([0])
    print(f"Test 6 - Single element: {result6 == 1}")

    # Performance comparison test
    # Create list of 0 to 9999 with 5000 missing
    large_list = list(range(10000))
    large_list.remove(5000)  # Remove middle element

    # Time your optimized solution
    start_time = time.time()
    for _ in range(1000):
        result = missing_number(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (9,999 elements, 1000 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Found missing number: {missing_number(large_list)}")

    # Reference: naive approach checking each number
    def naive_missing_number(nums):
        nums_sorted = sorted(nums)  # O(n log n)
        for i in range(len(nums_sorted) + 1):
            if i >= len(nums_sorted) or nums_sorted[i] != i:
                return i
        return len(nums_sorted)

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_missing_number(large_list[:1000])
    naive_time = time.time() - start_time

    print(
        f"Naive O(n log n) time (1,000 elements, 100 iterations): {naive_time:.4f} seconds"
    )
    print(
        f"Estimated speedup: ~{(naive_time / 100 * 1000) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_missing_number()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Problem Clarification:
- Correctly questioned test case logic: "How is the missing last number 2?"
- Identified key insight about n = len(nums) vs max(nums)
- Understood complete sequence should be [0, 1, 2, ..., n] where n = len(nums)

Final Implementation:
- Used set difference approach: `set(nums_complete) - set(nums)`
- All test cases passed correctly
- O(n) time complexity solution

Professional Feedback:
- Called out poor performance test design: "you are comparing it to O(n log n)! Of course O(n) is going to be slower!"
- Correctly identified unfair comparison (different data sizes and iteration counts)
- Showed good technical judgment in questioning flawed benchmarks

Core Pattern Mastered:
Set difference for finding missing elements in a known sequence
"""
