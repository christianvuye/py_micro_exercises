"""
Character Type Groups

Write a function `character_type_groups` that takes a list of strings.
Group strings that share the same character composition pattern.

Example:
character_type_groups(["abc", "xyz", "123", "789", "a1b", "x2y"])
→ Groups strings by their character type pattern

character_type_groups(["hello", "world", "12345", "67890"])
→ Groups strings by their character type pattern

Test Cases (copy-paste below your function):

import time

def test_character_type_groups():
    # Test case 1: Mixed character types
    result1 = character_type_groups(["abc", "xyz", "123", "789", "a1b", "x2y"])
    print(f"Test 1 result: {result1}")

    # Test case 2: All same pattern
    result2 = character_type_groups(["hello", "world", "python"])
    print(f"Test 2 result: {result2}")

    # Test case 3: Different lengths, same pattern
    result3 = character_type_groups(["ab", "xyz", "hello"])
    print(f"Test 3 result: {result3}")

    # Test case 4: Numbers and letters
    result4 = character_type_groups(["123", "abc", "456", "def"])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = character_type_groups([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = ["abc"] * 1000 + ["123"] * 1000 + ["a1b"] * 1000

    start_time = time.time()
    for _ in range(100):
        result = character_type_groups(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (3,000 strings, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(character_type_groups(large_list))}")

# test_character_type_groups()
"""

import time
from collections import defaultdict


def character_type_groups(strings: list[str]) -> dict[str, list[str]]:
    """
    Groups a list of strings based on their character types: all letters, all digits, or mixed.

    Args:
        strings (list[str]): A list of strings to be grouped.

    Returns:
        dict[str, list[str]]: A dictionary with keys "all letters", "all digits", and "mixed",
            each mapping to a list of strings that fit the respective category.
            - "all letters": Strings containing only alphabetic characters.
            - "all digits": Strings containing only numeric characters.
            - "mixed": Strings containing both alphabetic and numeric characters.
    """
    grouped = defaultdict(list)
    char_identifier = "a"
    nr_identifier = "n"
    for string in strings:
        temp_set = set()
        for char in string:
            if char.isalpha():
                temp_set.add(char_identifier)
            elif char.isnumeric():
                temp_set.add(nr_identifier)
        if char_identifier in temp_set and nr_identifier in temp_set:
            grouped["mixed"].append(string)
        elif char_identifier in temp_set:
            grouped["all letters"].append(string)
        elif nr_identifier in temp_set:
            grouped["all digits"].append(string)
    return dict(grouped)


def test_character_type_groups():
    # Test case 1: Mixed character types
    result1 = character_type_groups(["abc", "xyz", "123", "789", "a1b", "x2y"])
    print(f"Test 1 result: {result1}")

    # Test case 2: All same pattern
    result2 = character_type_groups(["hello", "world", "python"])
    print(f"Test 2 result: {result2}")

    # Test case 3: Different lengths, same pattern
    result3 = character_type_groups(["ab", "xyz", "hello"])
    print(f"Test 3 result: {result3}")

    # Test case 4: Numbers and letters
    result4 = character_type_groups(["123", "abc", "456", "def"])
    print(f"Test 4 result: {result4}")

    # Test case 5: Empty list
    result5 = character_type_groups([])
    expected5 = {}
    print(f"Test 5 - Empty: {result5 == expected5}")

    # Performance test
    large_list = ["abc"] * 1000 + ["123"] * 1000 + ["a1b"] * 1000

    start_time = time.time()
    for _ in range(100):
        result = character_type_groups(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (3,000 strings, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Groups found: {len(character_type_groups(large_list))}")


test_character_type_groups()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Character Type Groups
Pattern: Structural analysis with signature-based grouping (Exercise 13 variant)

Developer's Solution Approach:
- Used set-based character type detection with identifier flags
- Applied Exercise 13 pattern: analyze structure → create signature → group by signature  
- Fixed logical errors independently (conditional logic and missing append)
- Used defaultdict(list) for automatic group creation

Technical Implementation Evolution:
- Initial bugs: incorrect conditional precedence and missing append operation
- Self-corrected both issues after seeing incorrect output
- Clean character analysis using isalpha() and isnumeric() methods
- Effective use of set to track presence of character types

Complexity Analysis Skills:
- Time: O(n × s) - correctly identified nested loop structure
- Space: Minor error on temporary set size (O(s) vs O(1))  
- Tendency to overcomplicate with constant factor analysis
- Overall understanding sound despite minor overcomplication

Algorithm Design Approach:
- Used set membership to elegantly track character type presence
- Proper three-way conditional logic for categorization
- Handled edge cases (empty strings/lists) correctly
- Demonstrated debugging skills through output analysis

Pattern Recognition Mastery:
- Successfully applied Exercise 13's analyze-then-group structure
- Extended pattern to new domain (word patterns → character type patterns)
- Maintained consistent signature-based grouping approach
- Required minimal guidance for pattern transfer

Next Focus: Pattern reinforcement cycle complete - ready for Tier 3 advancement.
"""
