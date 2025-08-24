"""
Character Frequency Counter

Write a function `character_frequency` that takes in a string as an argument.
The function should return a dictionary where keys are characters and values
are their frequency counts in the string.

This is a foundational hashing pattern that converts O(n²) list operations
to O(n) dictionary operations.

Example:
character_frequency("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
character_frequency("aabbcc") → {'a': 2, 'b': 2, 'c': 2}
character_frequency("") → {}

Test Cases (copy-paste below your function):

import time
from collections import defaultdict

def test_character_frequency():
    # Test case 1: Basic functionality
    result1 = character_frequency("hello")
    expected1 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(f"Test 1 - Basic: {result1 == expected1}")
    print(f"Result: {result1}")

    # Test case 2: Empty string
    result2 = character_frequency("")
    expected2 = {}
    print(f"Test 2 - Empty: {result2 == expected2}")

    # Test case 3: Repeated characters
    result3 = character_frequency("aabbcc")
    expected3 = {'a': 2, 'b': 2, 'c': 2}
    print(f"Test 3 - Repeated: {result3 == expected3}")

    # Test case 4: Single character
    result4 = character_frequency("aaaa")
    expected4 = {'a': 4}
    print(f"Test 4 - Single char: {result4 == expected4}")

    # Performance comparison test
    large_string = "abcdefghijklmnopqrstuvwxyz" * 1000  # 26,000 chars

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = character_frequency(large_string)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (26,000 chars, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: what a naive O(n²) approach might look like
    def naive_frequency(s):
        result = {}
        for char in s:
            count = 0
            for c in s:  # This creates O(n²) complexity
                if c == char:
                    count += 1
            result[char] = count
        return result

    start_time = time.time()
    for _ in range(10):  # Less iterations due to slowness
        naive_result = naive_frequency(large_string[:1000])  # Smaller string
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 chars, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_character_frequency()
"""

import time
from collections import Counter


def character_frequency(s: str) -> dict[str, int]:
    """
    Calculates the frequency of each character in the given string.

    Args:
        s (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each character to its frequency count in the string.
    """
    return Counter(s)


def test_character_frequency():
    # Test case 1: Basic functionality
    result1 = character_frequency("hello")
    expected1 = {"h": 1, "e": 1, "l": 2, "o": 1}
    print(f"Test 1 - Basic: {result1 == expected1}")
    print(f"Result: {result1}")

    # Test case 2: Empty string
    result2 = character_frequency("")
    expected2 = {}
    print(f"Test 2 - Empty: {result2 == expected2}")

    # Test case 3: Repeated characters
    result3 = character_frequency("aabbcc")
    expected3 = {"a": 2, "b": 2, "c": 2}
    print(f"Test 3 - Repeated: {result3 == expected3}")

    # Test case 4: Single character
    result4 = character_frequency("aaaa")
    expected4 = {"a": 4}
    print(f"Test 4 - Single char: {result4 == expected4}")

    # Performance comparison test
    large_string = "abcdefghijklmnopqrstuvwxyz" * 1000  # 26,000 chars

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = character_frequency(large_string)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (26,000 chars, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: what a naive O(n²) approach might look like
    def naive_frequency(s):
        result = {}
        for char in s:
            count = 0
            for c in s:  # This creates O(n²) complexity
                if c == char:
                    count += 1
            result[char] = count
        return result

    start_time = time.time()
    for _ in range(10):  # Less iterations due to slowness
        naive_result = naive_frequency(large_string[:1000])  # Smaller string
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 chars, 10 iterations): {naive_time:.4f} seconds")
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_character_frequency()

"""
Manual Implementation Challenge

Implement the same functionality without using Counter or any imports.
"""


def character_frequency_manual(s: str) -> dict[str, int]:
    """
    Implements character frequency counting without using Counter.

    Args:
        s (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each character to its frequency count.
    """
    character_count = {}
    for char in s:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count


def test_both_implementations():
    """Test both Counter and manual implementations for correctness."""
    test_strings = ["hello", "", "aabbcc", "aaaa", "abcdef"]

    print("Comparing Counter vs Manual implementations:")
    for test_str in test_strings:
        counter_result = character_frequency(test_str)
        manual_result = character_frequency_manual(test_str)
        matches = dict(counter_result) == manual_result
        print(
            f"'{test_str}': Counter={dict(counter_result)}, Manual={manual_result}, Match={matches}"
        )


# Uncomment after implementing manual version:
test_both_implementations()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation Approach:
- Used Counter(s) for clean, Pythonic solution
- Demonstrated understanding of built-in optimization tools
- Achieved 24.9x performance improvement over naive O(n²) approach

Complexity Analysis Performance:
- Time Complexity: O(n) ✅ (correctly identified linear dependence on string length)
- Space Complexity: Initially said O(1), corrected to O(k) where k=unique chars, worst case O(n) ✅

Manual Implementation Challenge:
- Successfully implemented manual version using basic dictionary operations
- Used classic "check key existence, initialize if needed, then increment" pattern
- Pattern: `if char not in dict: dict[char] = 1 else: dict[char] += 1`
- All test cases passed with identical results to Counter implementation

Key Learning Moments:
- Recognized that Counter is syntactic sugar over manual dictionary operations
- Understood both approaches have identical time/space complexity
- Correctly identified that high-level tools are convenience wrappers over fundamental patterns

Professional Development Notes:
- Provided constructive feedback: "These hints are giving away too much... I need to figure these things out for myself"
- Shows strong learning autonomy and desire for genuine problem-solving practice
- Interview readiness: ✅ Can implement both clean Pythonic and manual fundamental versions

Core Pattern Mastered: 
Dictionary-based counting for O(n) frequency analysis - foundation for many hashing optimizations
"""
