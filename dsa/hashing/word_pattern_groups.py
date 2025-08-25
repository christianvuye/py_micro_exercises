"""
Word Pattern Groups

Write a function `word_pattern_groups` that takes a list of words.
Group words that follow the same letter pattern together.

Two words have the same pattern if there's a one-to-one mapping between
characters in the first word and characters in the second word.

Example:
word_pattern_groups(["abc", "def", "aab", "xxy", "aba", "cdc"])
→ {"abc": ["abc", "def"], "aab": ["aab", "xxy"], "aba": ["aba", "cdc"]}

word_pattern_groups(["paper", "title", "abc", "def"])
→ {"paper": ["paper", "title"], "abc": ["abc", "def"]}

Test Cases (copy-paste below your function):

import time

def test_word_pattern_groups():
    # Test case 1: Basic patterns
    result1 = word_pattern_groups(["abc", "def", "aab", "xxy", "aba", "cdc"])
    # Normalize for comparison (use sorted keys and values)
    normalized1 = {min(v): sorted(v) for v in result1.values()}
    expected1 = {"abc": ["abc", "def"], "aab": ["aab", "xxy"], "aba": ["aba", "cdc"]}
    normalized_expected1 = {min(v): sorted(v) for v in expected1.values()}
    print(f"Test 1 - Basic patterns: {normalized1 == normalized_expected1}")

    # Test case 2: Different word lengths
    result2 = word_pattern_groups(["paper", "title", "abc", "def"])
    normalized2 = {min(v): sorted(v) for v in result2.values()}
    expected2 = {"paper": ["paper", "title"], "abc": ["abc", "def"]}
    normalized_expected2 = {min(v): sorted(v) for v in expected2.values()}
    print(f"Test 2 - Different lengths: {normalized2 == normalized_expected2}")

    # Test case 3: No patterns match
    result3 = word_pattern_groups(["abc", "def", "ghi"])
    print(f"Test 3 - No matches: {len(result3) == 3}")  # Each word in own group

    # Test case 4: All same pattern
    result4 = word_pattern_groups(["abc", "def", "ghi", "jkl"])
    print(f"Test 4 - All same pattern: {len(result4) == 1}")  # One group

    # Test case 5: Empty and single word
    result5 = word_pattern_groups([])
    result6 = word_pattern_groups(["hello"])
    print(f"Test 5 - Empty: {result5 == {}}")
    print(f"Test 6 - Single word: {len(result6) == 1}")

    # Test case 7: Complex patterns
    result7 = word_pattern_groups(["abcdef", "123456", "aabbcc", "ddeeff", "abccba", "defgfd"])
    print(f"Test 7 - Complex: {len(result7) == 3}")  # Three different patterns

    # Performance test
    import string
    import random

    # Generate words with known patterns
    patterns = ["abc", "aab", "aba", "abcd", "aabb", "abba", "abca"]
    large_list = []

    for _ in range(5000):
        pattern = random.choice(patterns)
        # Create word following this pattern
        char_map = {}
        word = ""
        next_char_idx = 0

        for char in pattern:
            if char not in char_map:
                char_map[char] = string.ascii_lowercase[next_char_idx]
                next_char_idx += 1
            word += char_map[char]

        large_list.append(word)

    start_time = time.time()
    for _ in range(50):
        result = word_pattern_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (5,000 words, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Pattern groups found: {len(word_pattern_groups(large_list))}")

    # Naive approach - compare every word to every other word
    def naive_word_pattern_groups(words):
        def same_pattern(w1, w2):
            if len(w1) != len(w2):
                return False
            mapping = {}
            reverse_mapping = {}
            for c1, c2 in zip(w1, w2):
                if c1 in mapping:
                    if mapping[c1] != c2:
                        return False
                else:
                    if c2 in reverse_mapping:
                        return False
                    mapping[c1] = c2
                    reverse_mapping[c2] = c1
            return True

        if not words:
            return {}

        groups = []
        used = [False] * len(words)

        for i, word in enumerate(words):
            if used[i]:
                continue
            group = [word]
            used[i] = True
            for j in range(i + 1, len(words)):
                if not used[j] and same_pattern(word, words[j]):
                    group.append(words[j])
                    used[j] = True
            groups.append(group)

        return {group[0]: group for group in groups}

    start_time = time.time()
    for _ in range(5):
        naive_result = naive_word_pattern_groups(large_list[:200])
    naive_time = time.time() - start_time

    print(f"Naive O(n² × m) time (200 words, 5 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time * 25 * 10) / optimized_time:.1f}x faster")

# test_word_pattern_groups()
"""

import time
from collections import defaultdict


def word_pattern_groups(words: list[str]) -> dict[str, list[str]]:
    """
    Groups words by their structural pattern.

    Each word is assigned a signature based on the order of unique characters as they appear.
    Words with the same character pattern (regardless of actual characters) are grouped together.

    For example, "foo" and "app" both have the pattern "011", so they will be grouped together.

    Args:
        words (list[str]): A list of words to group by pattern.

    Returns:
        dict[str, list[str]]: A dictionary mapping pattern signatures to lists of words sharing that pattern.
    """
    grouped = defaultdict(list)
    for word in words:
        temp_dict = {}
        next_number = 0
        signature_parts = []
        for char in word:
            if char not in temp_dict:
                signature_parts.append(str(next_number))
                temp_dict[char] = next_number
                next_number += 1
            else:
                signature_parts.append(str(temp_dict[char]))
        signature = "".join(signature_parts)
        grouped[signature].append(word)
    return grouped


def test_word_pattern_groups():
    # Test case 1: Basic patterns
    result1 = word_pattern_groups(["abc", "def", "aab", "xxy", "aba", "cdc"])
    # Normalize for comparison (use sorted keys and values)
    normalized1 = {min(v): sorted(v) for v in result1.values()}
    expected1 = {"abc": ["abc", "def"], "aab": ["aab", "xxy"], "aba": ["aba", "cdc"]}
    normalized_expected1 = {min(v): sorted(v) for v in expected1.values()}
    print(f"Test 1 - Basic patterns: {normalized1 == normalized_expected1}")

    # Test case 2: Different word lengths
    result2 = word_pattern_groups(["paper", "title", "abc", "def"])
    normalized2 = {min(v): sorted(v) for v in result2.values()}
    expected2 = {"paper": ["paper", "title"], "abc": ["abc", "def"]}
    normalized_expected2 = {min(v): sorted(v) for v in expected2.values()}
    print(f"Test 2 - Different lengths: {normalized2 == normalized_expected2}")

    # Test case 3: All same pattern (corrected)
    result3 = word_pattern_groups(["abc", "def", "ghi"])
    print(f"Test 3 - All same pattern: {len(result3) == 1}")  # Should be 1, not 3
    print(f"Debug - All have pattern '012': {list(result3.keys()) == ['012']}")

    # Test case 4: All same pattern
    result4 = word_pattern_groups(["abc", "def", "ghi", "jkl"])
    print(f"Test 4 - All same pattern: {len(result4) == 1}")  # One group

    # Test case 5: Empty and single word
    result5 = word_pattern_groups([])
    result6 = word_pattern_groups(["hello"])
    print(f"Test 5 - Empty: {result5 == {}}")
    print(f"Test 6 - Single word: {len(result6) == 1}")

    # Test case 7: Complex patterns
    result7 = word_pattern_groups(
        ["abcdef", "123456", "aabbcc", "ddeeff", "abccba", "defgfd"]
    )

    print(f"Test 7 - Complex: {len(result7) == 4}")  # Should be 4, not 3

    # Performance test
    import random
    import string

    # Generate words with known patterns
    patterns = ["abc", "aab", "aba", "abcd", "aabb", "abba", "abca"]
    large_list = []

    for _ in range(5000):
        pattern = random.choice(patterns)
        # Create word following this pattern
        char_map = {}
        word = ""
        next_char_idx = 0

        for char in pattern:
            if char not in char_map:
                char_map[char] = string.ascii_lowercase[next_char_idx]
                next_char_idx += 1
            word += char_map[char]

        large_list.append(word)

    start_time = time.time()
    for _ in range(50):
        result = word_pattern_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (5,000 words, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Pattern groups found: {len(word_pattern_groups(large_list))}")

    # Naive approach - compare every word to every other word
    def naive_word_pattern_groups(words):
        def same_pattern(w1, w2):
            if len(w1) != len(w2):
                return False
            mapping = {}
            reverse_mapping = {}
            for c1, c2 in zip(w1, w2):
                if c1 in mapping:
                    if mapping[c1] != c2:
                        return False
                else:
                    if c2 in reverse_mapping:
                        return False
                    mapping[c1] = c2
                    reverse_mapping[c2] = c1
            return True

        if not words:
            return {}

        groups = []
        used = [False] * len(words)

        for i, word in enumerate(words):
            if used[i]:
                continue
            group = [word]
            used[i] = True
            for j in range(i + 1, len(words)):
                if not used[j] and same_pattern(word, words[j]):
                    group.append(words[j])
                    used[j] = True
            groups.append(group)

        return {group[0]: group for group in groups}

    start_time = time.time()
    for _ in range(5):
        naive_result = naive_word_pattern_groups(large_list[:200])
    naive_time = time.time() - start_time

    print(f"Naive O(n² × m) time (200 words, 5 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time * 25 * 10) / optimized_time:.1f}x faster")

    print("Debug - Four distinct patterns found:")
    print(f"Debug - result7 keys: {list(result7.keys())}")
    print(f"Debug - result7 values: {list(result7.values())}")
    for pattern, words in result7.items():
        print(f"  Pattern '{pattern}': {words}")


test_word_pattern_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Word Pattern Groups
Pattern: Character relationship normalization with hash-based grouping

Developer's Solution Approach:
- Used character-to-number mapping for pattern signature generation
- Applied "first appearance numbering" (0, 1, 2...) for consistent signatures
- Self-optimized from O(s²) string concatenation to O(s) list joining
- Correctly identified and debugged incorrect test expectations

Technical Evolution:
Initial approach: String concatenation (O(n × s²))
Optimized approach: List building + join (O(n × s))
- Demonstrated strong performance awareness and optimization instincts

Complexity Analysis Mastery:
- Time: O(n × s) - correctly identified optimal complexity for input processing
- Space: O(n × s) - linear storage of all input data plus signatures
- Recognized string concatenation as performance bottleneck independently
- Applied list-building optimization without prompting

Problem-Solving Process:
- Built signature generation algorithm step-by-step with guidance
- Debugged test failures by examining actual vs expected outputs
- Correctly identified test specification errors rather than implementation bugs
- Maintained focus on algorithmic correctness throughout

Key Learning Moments:
- Pattern recognition: "Character relationships, not actual characters"
- First-appearance numbering: Consistent signature generation technique
- String performance: += creates new objects, list+join is O(n)
- Test validation: Always verify test expectations against problem requirements

Critical Thinking Demonstrated:
- Questioned test failures and investigated actual behavior
- Proved implementation correctness through systematic analysis
- Identified specification errors in provided test cases
- Self-corrected minor code inconsistencies

Next Focus: Continue with more advanced hash-based optimization patterns in Tier 2.
"""
