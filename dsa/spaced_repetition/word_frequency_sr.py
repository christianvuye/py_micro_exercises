"""
Word Frequency - Spaced Repetition

Write a function, word_frequency, that takes in a string of text as an argument.
The function should return a dictionary where keys are words and values are
their frequency counts. Words are case-insensitive and separated by spaces.

Example:
word_frequency("hello world hello") → {'hello': 2, 'world': 1}
word_frequency("The cat and the dog") → {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
word_frequency("") → {}

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""

import random
import time
from collections import Counter, defaultdict


def word_frequency(text: str) -> dict[str, int]:
    """
    Calculates the frequency of each word in the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each word (in lowercase) to its frequency count.

    Example:
        >>> word_frequency("Hello world! Hello")
        {'hello': 2, 'world!': 1}
    """
    word_freq = defaultdict(int)
    text_lower = text.lower()
    words = text_lower.split()
    for word in words:
        word_freq[word] += 1
    return dict(word_freq)


def test_word_frequency():
    """
    Tests the word_frequency function with various input cases to ensure correct word counting.

    Test cases include:
    - Simple repeated words.
    - Case insensitivity and multiple words.
    - Empty string input.
    - Single long word with no spaces.
    - Leading/trailing spaces and punctuation.
    - Multiple punctuation marks as words.
    - Single character input.

    Each test asserts that the output matches the expected word frequency dictionary.
    """

    # Test 1
    text = "hello world hello"
    expected = {"hello": 2, "world": 1}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 2
    text = "The cat and the dog"
    expected = {"the": 2, "cat": 1, "and": 1, "dog": 1}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 3
    text = ""
    expected = {}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 4
    text = "wordwordwordwordwordorod"
    expected = {"wordwordwordwordwordorod": 1}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 5
    text = "     word.  "
    expected = {"word.": 1}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 6
    text = "     word.  .   .  "
    expected = {"word.": 1, ".": 2}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 7
    text = "w"
    expected = {"w": 1}
    result = word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )


test_word_frequency()

"""
Alternative approach with Counter()
"""


def count_word_frequency(text: str) -> dict[str, int]:
    """docstring"""
    return dict(Counter(text.lower().split()))


def test_count_word_frequency():
    """
    docstring
    """

    # Test 1
    text = "hello world hello"
    expected = {"hello": 2, "world": 1}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 2
    text = "The cat and the dog"
    expected = {"the": 2, "cat": 1, "and": 1, "dog": 1}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 3
    text = ""
    expected = {}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 4
    text = "wordwordwordwordwordorod"
    expected = {"wordwordwordwordwordorod": 1}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 5
    text = "     word.  "
    expected = {"word.": 1}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 6
    text = "     word.  .   .  "
    expected = {"word.": 1, ".": 2}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )

    # Test 7
    text = "w"
    expected = {"w": 1}
    result = count_word_frequency(text)
    assert expected == result, (
        f"TEST FAILED, Expected: {expected}, got {result} instead"
    )


test_count_word_frequency()


def generate_large_text(num_words, vocabulary_size=1000):
    """
    Generate large text for performance testing.

    Args:
        num_words: Total number of words to generate
        vocabulary_size: Number of unique words in vocabulary

    Returns:
        String with specified number of words
    """
    # Create vocabulary of random words
    vocabulary = [f"word{i}" for i in range(vocabulary_size)]

    # Generate random text
    words = random.choices(vocabulary, k=num_words)
    return " ".join(words)


def generate_predictable_text(num_words):
    """Generate predictable large text for consistent testing"""
    # Create pattern: word0 word1 word0 word2 word0 word3...
    # This ensures lots of duplicates for frequency counting
    words = []
    for i in range(num_words):
        if i % 3 == 0:
            words.append("common")  # Frequent word
        else:
            words.append(f"word{i}")  # Unique words

    return " ".join(words)


def performance_test():
    """
    Compare performance of defaultdict vs Counter approaches
    """
    print("Generating test data...")

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]

    for size in test_sizes:
        print(f"\nTesting with {size:,} words:")

        # Generate test data
        test_text = generate_large_text(size, vocabulary_size=size // 10)

        # Test defaultdict approach
        start_time = time.time()
        result1 = word_frequency(test_text)
        defaultdict_time = time.time() - start_time

        # Test Counter approach
        start_time = time.time()
        result2 = count_word_frequency(test_text)
        counter_time = time.time() - start_time

        # Verify results are identical
        assert result1 == result2, "Results don't match!"

        print(f"  defaultdict approach: {defaultdict_time:.4f} seconds")
        print(f"  Counter approach:     {counter_time:.4f} seconds")
        print(f"  Speedup ratio:        {defaultdict_time / counter_time:.2f}x")
        print(f"  Unique words found:   {len(result1):,}")


performance_test()

"""
=== EXERCISE #4 SUMMARY - WORD FREQUENCY (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG PROGRESSION
- Natural evolution from manual dictionary to defaultdict(int) and Counter
- Clean implementation pipeline: lowercase → split → count → convert
- Strong understanding of accumulation pattern across multiple data structures

Interview Readiness: 🟢 STRONG ANALYTICAL SKILLS
- Professional requirements clarification (punctuation handling)
- Smart choice of split() vs split(" ") for edge case handling
- Shows library knowledge while demonstrating fundamental understanding
- Caught instructor contradiction about large input testing vs performance benchmarking

Spaced Repetition Performance: 📈 ACCELERATING MASTERY
- Faster completion time showing pattern internalization
- Comprehensive edge case coverage (empty string, spaces, punctuation)
- Self-driven exploration of alternative approaches (Counter optimization)
- Advanced performance testing implementation (though not interview-standard)

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(n) where n = string length
Space Complexity: O(n) due to string processing and word storage
Pattern Type: Dictionary accumulation with preprocessing (case normalization)
Core Skills: Library usage, string processing, frequency counting

Key Strengths Demonstrated:
- Critical thinking about instructor advice contradictions
- Professional requirements clarification questions
- Technical progression: manual → defaultdict → Counter approaches
- Strong engineering instincts with performance benchmarking setup
- Understanding of interview vs production testing approaches

Areas for Interview Focus:
- Large input testing for correctness is reasonable
- Performance benchmarking timing is not standard interview practice
- Focus on complexity analysis over empirical timing measurements

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows strong engineering thinking beyond typical interview requirements
"""
