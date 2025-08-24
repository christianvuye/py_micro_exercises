"""
Find Complement

Write a function `find_complement` that takes in a list of numbers and a target sum.
The function should return the first number in the list that has a complement
(another number in the list) such that the two numbers add up to the target sum.
If no such number exists, return None.

Example:
find_complement([1, 2, 3, 4], 5) → 1  (because 1 + 4 = 5)
find_complement([2, 7, 11, 15], 9) → 2  (because 2 + 7 = 9)
find_complement([1, 2, 3], 10) → None  (no pair sums to 10)
find_complement([], 5) → None

Test Cases (copy-paste below your function):

import time

def test_find_complement():
    # Test case 1: Has complement
    result1 = find_complement([1, 2, 3, 4], 5)
    print(f"Test 1 - Has complement: {result1 == 1}")

    # Test case 2: Different complement
    result2 = find_complement([2, 7, 11, 15], 9)
    print(f"Test 2 - Different complement: {result2 == 2}")

    # Test case 3: No complement
    result3 = find_complement([1, 2, 3], 10)
    print(f"Test 3 - No complement: {result3 is None}")

    # Test case 4: Empty list
    result4 = find_complement([], 5)
    print(f"Test 4 - Empty list: {result4 is None}")

    # Test case 5: Same number twice
    result5 = find_complement([3, 3], 6)
    print(f"Test 5 - Same number twice: {result5 == 3}")

    # Test case 6: Multiple valid pairs
    result6 = find_complement([1, 4, 2, 3], 5)  # Both 1+4 and 2+3 = 5
    print(f"Test 6 - Multiple pairs (should return first): {result6 == 1}")

    # Performance comparison test
    large_list = list(range(10000)) + [5000]  # [0,1,2,...,9999,5000]
    target = 15000  # 5000 + 10000, but complement is at end

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = find_complement(large_list, target)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,001 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_find_complement(numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return numbers[i]
        return None

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_find_complement(large_list[:1000], target)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 elements, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_find_complement()
"""

import time
from collections import Counter


def find_complement(numbers: list, target: int) -> int | None:
    """
    Finds and returns a number from the input list such that there exists another number in the list whose sum with it equals the target value.

    If such a pair exists, returns the first of the numbers from the pair. If no such pair exists, returns None.

    Args:
        numbers (list): A list of integers to search for the complement.
        target (int): The target sum to find.

    Returns:
        int | None: A number from the list that forms the target sum with its complement, or None if no such pair exists.
    """
    count_numbers = Counter(numbers)

    for number in numbers:
        complement = target - number
        if complement in count_numbers:
            if complement == number:
                if count_numbers[number] > 1:
                    return number
            else:
                return number
    return None


def test_find_complement():
    # Test case 1: Has complement
    result1 = find_complement([1, 2, 3, 4], 5)
    print(f"Test 1 - Has complement: {result1 == 1}")

    # Test case 2: Different complement
    result2 = find_complement([2, 7, 11, 15], 9)
    print(f"Test 2 - Different complement: {result2 == 2}")

    # Test case 3: No complement
    result3 = find_complement([1, 2, 3], 10)
    print(f"Test 3 - No complement: {result3 is None}")

    # Test case 4: Empty list
    result4 = find_complement([], 5)
    print(f"Test 4 - Empty list: {result4 is None}")

    # Test case 5: Same number twice
    result5 = find_complement([3, 3], 6)
    print(f"Test 5 - Same number twice: {result5 == 3}")

    # Test case 6: Multiple valid pairs
    result6 = find_complement([1, 4, 2, 3], 5)  # Both 1+4 and 2+3 = 5
    print(f"Test 6 - Multiple pairs (should return first): {result6 == 1}")

    # Performance comparison test
    large_list = list(range(10000)) + [5000]  # [0,1,2,...,9999,5000]
    target = 15000  # 5000 + 10000, but complement is at end

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = find_complement(large_list, target)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,001 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_find_complement(numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return numbers[i]
        return None

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_find_complement(large_list[:1000], target)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 elements, 10 iterations): {naive_time:.4f} seconds")
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_find_complement()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Problem Recognition:
- Correctly identified that standard "iterate and build tracking set" approach doesn't guarantee first number
- Recognized need to separate "finding complements" from "checking in order"
- Asked clarifying questions about approach before implementing

Edge Case Analysis:
- Identified self-complement problem: "is it possible to solve using set lookup? Probably not because sets have only unique values"
- Proposed Counter/dict solution for tracking frequency: "check if dict[number] > 1"
- Demonstrated strong analytical thinking about data structure limitations

Final Implementation:
- Used Counter for O(1) complement lookup with frequency tracking
- Clean logic: if complement == number, check count > 1; else just check existence
- All test cases passed with 45.1x performance improvement

Complexity Analysis Performance:
- Initially said Counter creation is O(k) unique elements, corrected to O(n) total elements ✅
- Correctly identified space as O(k) for unique elements
- Overall analysis: O(n) time, O(k) to O(n) space ✅
- Good insight: "Counter is the appropriate solution, no need to reinvent manually"

Core Pattern Mastered:
Complement lookup with frequency consideration - handles both general pairs and self-complement cases
"""
