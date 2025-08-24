"""
Word Frequency Counter

Write a function `word_frequency` that takes in a string of text as an argument.
The function should return a dictionary where keys are words and values are
their frequency counts. Words are case-insensitive and separated by spaces.

Example:
word_frequency("hello world hello") → {'hello': 2, 'world': 1}
word_frequency("The cat and the dog") → {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
word_frequency("") → {}

Test Cases (copy-paste below your function):

import time

def test_word_frequency():
    # Test case 1: Basic functionality
    result1 = word_frequency("hello world hello")
    expected1 = {'hello': 2, 'world': 1}
    print(f"Test 1 - Basic: {result1 == expected1}")

    # Test case 2: Case insensitive
    result2 = word_frequency("The cat and the dog")
    expected2 = {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
    print(f"Test 2 - Case insensitive: {result2 == expected2}")

    # Test case 3: Empty string
    result3 = word_frequency("")
    expected3 = {}
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: Single word
    result4 = word_frequency("python")
    expected4 = {'python': 1}
    print(f"Test 4 - Single word: {result4 == expected4}")

    # Test case 5: Repeated word
    result5 = word_frequency("test test test")
    expected5 = {'test': 3}
    print(f"Test 5 - Repeated: {result5 == expected5}")

    # Performance comparison test
    large_text = "word " * 5000 + "other " * 3000 + "text " * 2000  # 10,000 words

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = word_frequency(large_text)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,000 words, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive approach
    def naive_word_frequency(text):
        words = text.lower().split()
        result = {}
        for word in words:
            count = 0
            for w in words:  # Count each word by scanning entire list
                if w == word:
                    count += 1
            result[word] = count
        return result

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_word_frequency(large_text)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (10,000 words, 100 iterations): {naive_time:.4f} seconds")
    print(f"Speedup: ~{naive_time/optimized_time:.1f}x faster")

# Run tests after implementing your function
# test_word_frequency()
"""

import time
from collections import Counter


def word_frequency(text: str) -> dict[str, int]:
    """
    Calculates the frequency of each word in the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each word (in lowercase) to its frequency count.

    Example:
        >>> word_frequency("Hello world hello")
        {'hello': 2, 'world': 1}
    """
    if not len(text):
        return {}
    return Counter(text.lower().split(" "))


def test_word_frequency():
    # Test case 1: Basic functionality
    result1 = word_frequency("hello world hello")
    expected1 = {"hello": 2, "world": 1}
    print(f"Test 1 - Basic: {result1 == expected1}")

    # Test case 2: Case insensitive
    result2 = word_frequency("The cat and the dog")
    expected2 = {"the": 2, "cat": 1, "and": 1, "dog": 1}
    print(f"Test 2 - Case insensitive: {result2 == expected2}")

    # Test case 3: Empty string
    result3 = word_frequency("")
    expected3 = {}
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: Single word
    result4 = word_frequency("python")
    expected4 = {"python": 1}
    print(f"Test 4 - Single word: {result4 == expected4}")

    # Test case 5: Repeated word
    result5 = word_frequency("test test test")
    expected5 = {"test": 3}
    print(f"Test 5 - Repeated: {result5 == expected5}")

    # Performance comparison test
    large_text = "word " * 5000 + "other " * 3000 + "text " * 2000  # 10,000 words

    # Time your solution
    start_time = time.time()
    for _ in range(100):
        result = word_frequency(large_text)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,000 words, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive approach
    def naive_word_frequency(text):
        words = text.lower().split()
        result = {}
        for word in words:
            count = 0
            for w in words:  # Count each word by scanning entire list
                if w == word:
                    count += 1
            result[word] = count
        return result

    start_time = time.time()
    for _ in range(100):
        naive_result = naive_word_frequency(large_text)
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (10,000 words, 100 iterations): {naive_time:.4f} seconds")
    print(f"Speedup: ~{naive_time / optimized_time:.1f}x faster")


# Run tests after implementing your function
test_word_frequency()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- Used optimal Counter approach: `Counter(text.lower().split(" "))`
- Clean preprocessing: lowercase conversion then space splitting
- All test cases passed
- Performance test: naive O(n²) approach so slow it crashed debugger

Complexity Analysis Performance:
- Time: Correctly identified O(n) for each operation (lower, split, Counter) → O(n) overall ✅
- Understood early return for empty string gives O(1) ✅  
- Space: Excellent insight "if there's a lot of variety its a big dict, if there's little variety its a small dict" ✅
- Correctly identified space as O(k) where k=unique words, worst case O(n) ✅

Key Learning Moments:
- Demonstrated understanding that sequential O(n) operations stay O(n) (not O(n²))
- Recognized space complexity depends on data variety, not just input size
- Performance difference so dramatic it broke naive approach execution

Core Pattern Mastered:
Word-level frequency counting with case normalization and efficient hashing
"""
