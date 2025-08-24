"""
Contains Target Sum

Write a function `contains_target` that takes in a list of numbers and a target sum.
The function should return True if any two numbers in the list add up to the target sum,
False otherwise. You may use each number only once.

Example:
contains_target([2, 7, 11, 15], 9) → True  (2 + 7 = 9)
contains_target([3, 2, 4], 6) → True  (2 + 4 = 6)
contains_target([3, 3], 6) → True  (3 + 3 = 6)
contains_target([1, 2, 3], 10) → False

Test Cases (copy-paste below your function):

import time

def test_contains_target():
    # Test case 1: Contains target
    result1 = contains_target([2, 7, 11, 15], 9)
    print(f"Test 1 - Contains target: {result1 == True}")

    # Test case 2: Different target
    result2 = contains_target([3, 2, 4], 6)
    print(f"Test 2 - Different target: {result2 == True}")

    # Test case 3: Same number twice
    result3 = contains_target([3, 3], 6)
    print(f"Test 3 - Same number twice: {result3 == True}")

    # Test case 4: No target
    result4 = contains_target([1, 2, 3], 10)
    print(f"Test 4 - No target: {result4 == False}")

    # Test case 5: Empty list
    result5 = contains_target([], 5)
    print(f"Test 5 - Empty list: {result5 == False}")

    # Test case 6: Single element
    result6 = contains_target([5], 10)
    print(f"Test 6 - Single element: {result6 == False}")

    # Test case 7: Target at beginning
    result7 = contains_target([1, 2, 3, 4, 5], 3)
    print(f"Test 7 - Target at beginning: {result7 == True}")

    # Performance comparison test
    large_list = list(range(10000)) + [5000]  # Target sum 15000 (5000 + 10000)

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = contains_target(large_list, 15000)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,001 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_contains_target(numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return True
        return False

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_contains_target(large_list, 15000)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (10,001 elements, 100 iterations): {naive_time:.4f} seconds")
    print(f"Speedup: ~{naive_time/optimized_time:.1f}x faster")

# Run tests after implementing your function
# test_contains_target()
"""


def contains_target(numbers: list[int], target: int) -> bool:
    """
    Determines if there exist two numbers in the given list that sum up to the target value.

    Args:
        numbers (list[int]): A list of integers to search through.
        target (int): The target sum to find.

    Returns:
        bool: True if any two numbers in the list sum to the target, False otherwise.

    Example:
        >>> contains_target([1, 2, 3, 4], 5)
        True
        >>> contains_target([1, 2, 3, 4], 8)
        False
    """
    num_count = {}

    for num in numbers:
        complement = target - num
        if complement in num_count:
            if complement == num:
                if num_count[num] > 0:
                    return True
            else:
                return True
        else:
            num_count[num] = 1
    return False


def test_contains_target():
    # Test case 1: Contains target
    result1 = contains_target([2, 7, 11, 15], 9)
    print(f"Test 1 - Contains target: {result1 == True}")

    # Test case 2: Different target
    result2 = contains_target([3, 2, 4], 6)
    print(f"Test 2 - Different target: {result2 == True}")

    # Test case 3: Same number twice
    result3 = contains_target([3, 3], 6)
    print(f"Test 3 - Same number twice: {result3 == True}")

    # Test case 4: No target
    result4 = contains_target([1, 2, 3], 10)
    print(f"Test 4 - No target: {result4 == False}")

    # Test case 5: Empty list
    result5 = contains_target([], 5)
    print(f"Test 5 - Empty list: {result5 == False}")

    # Test case 6: Single element
    result6 = contains_target([5], 10)
    print(f"Test 6 - Single element: {result6 == False}")

    # Test case 7: Target at beginning
    result7 = contains_target([1, 2, 3, 4, 5], 3)
    print(f"Test 7 - Target at beginning: {result7 == True}")
    """
    # Performance comparison test
    large_list = list(range(10000)) + [5000]  # Target sum 15000 (5000 + 10000)

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = contains_target(large_list, 15000)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,001 elements, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive O(n²) approach
    def naive_contains_target(numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return True
        return False

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_contains_target(large_list, 15000)
    naive_time = time.time() - start_time

    print(
        f"Naive O(n²) time (10,001 elements, 100 iterations): {naive_time:.4f} seconds"
    )
    print(f"Speedup: ~{naive_time / optimized_time:.1f}x faster")
    """


# Run tests after implementing your function
test_contains_target()

"""
Alternative Set-Based Approach Challenge

Try implementing the same functionality using a set instead of a dictionary.
Since you only need to track "have I seen this number before?" (not count),
a set might be more straightforward.

Consider:
- How does set lookup compare to dict lookup?
- Does this simplify the self-complement case?
- Does it affect time/space complexity?
"""


def contains_target_set(numbers: list[int], target: int) -> bool:
    """
    Alternative implementation using set for tracking seen numbers.

    Args:
        numbers (list[int]): A list of integers to search through.
        target (int): The target sum to find.

    Returns:
        bool: True if any two numbers sum to target, False otherwise.
    """
    # Your set-based implementation here
    seen = set()

    for number in numbers:
        complement = target - number
        if complement in seen:
            return True
        seen.add(number)
    return False


# Test both implementations for comparison
print("Dict approach:", contains_target([3, 3], 6))
print("Set approach:", contains_target_set([3, 3], 6))

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- Used dict-based complement tracking with self-complement handling
- Correctly defended logic: "no point in incrementing if key exists" and "if key exists and complement == num, they are self complementary"
- All test cases passed

Alternative Set Implementation:
- Successfully implemented cleaner set-based version
- Recognized set approach eliminates complex self-complement logic
- Both solutions functionally equivalent with O(n) time/space complexity

Key Technical Insights:
- **Fundamental Understanding**: "aren't sets and dicts very similar data structures under the hood, one just tracks a value, while the other tracks a key and a value, and they're both 'hashes' right?" ✅
- Recognized both are hash tables: dict maps keys→values, set maps keys→dummy values
- Understood both use same hashing mechanism with O(1) average lookup
- Grasped core insight: "hashing is the core optimization pattern" regardless of implementation

Professional Development:
- Defended implementation choices with clear reasoning
- Showed willingness to try alternative approaches
- Demonstrated deep understanding of data structure fundamentals

Core Pattern Mastered:
Complement-finding with hash-based lookup - the foundation pattern for two-sum problems across multiple data structures
"""
