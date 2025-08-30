"""
Most Frequent Char - Spaced Repetition

Write a function, most_frequent_char, that takes in a string as an argument.
The function should return the most frequently occurring character in the string.
If there are ties, return the character that appears earliest in the string.

Example:
most_frequent_char("bookeeper") → "e"
most_frequent_char("david") → "d"
most_frequent_char("abcdefghijklmnopqrstuvwxyz") → "a"
most_frequent_char("") → ""

After completing, analyze time and space complexity.
"""

from collections import defaultdict


def most_frequent_char(string: str) -> str:
    """
    Returns the most frequently occurring non-space character in the given string.
    If the string is empty, returns the empty string.

    Args:
        string (str): The input string to analyze.

    Returns:
        str: The character that appears most frequently (excluding spaces).
    """
    if not string:
        return string
    char_freq = defaultdict(list)
    for index, char in enumerate(string):
        if char != " ":
            char_freq[char].append(index)
    return max(char_freq, key=lambda char: len(char_freq[char]))


def test_most_frequent_char():
    """Comprehensive test cases for validation"""

    # Test Case 1: Basic example from problem
    input_data = "bookeeper"
    expected = "e"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 2: Early position wins tie
    input_data = "david"
    expected = "d"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 3: All unique characters
    input_data = "abcdefghijklmnopqrstuvwxyz"
    expected = "a"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 4: Empty string
    input_data = ""
    expected = ""
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 5: Single character
    input_data = "a"
    expected = "a"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 6: Clear frequency winner
    input_data = "aabbbbcc"
    expected = "b"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 7: Tie between multiple characters
    input_data = "aabbcc"
    expected = "a"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 8: Case sensitivity
    input_data = "AaAa"
    expected = "A"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 9: Numbers and special characters
    input_data = "112233!"
    expected = "1"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 10: Spaces included
    input_data = "a b b c"
    expected = "b"
    result = most_frequent_char(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")


# Run your tests
test_most_frequent_char()

"""
=== EXERCISE #11 SUMMARY - MOST FREQUENT CHAR (SPACED REPETITION) ===

Pattern Mastery: 🟡 FUNCTIONAL BUT SYNTAX-DEPENDENT
- Correct frequency counting approach using defaultdict(list) 
- Proper space filtering and edge case handling (empty string)
- Elegant tie-breaking via dictionary insertion order (Python 3.7+)
- Working solution but struggled significantly with lambda/max syntax

Interview Readiness: 🟡 NEEDS SYNTAX FLUENCY IMPROVEMENT  
- Asked for hints appropriately (per Affirm interview guidance)
- Fixed implementation bug quickly (list overwrite → append)
- Professional clarification questions about input constraints
- **Critical Gap**: Lambda expressions and max() key parameter confusion

Spaced Repetition Performance: 🔴 REQUIRES INTENSIVE PRACTICE
- Requested hints due to syntax barriers rather than algorithmic confusion
- Understood the problem logic but struggled with Python implementation details
- Alternative manual solutions (basic dict + two loops) may be clearer for interviews
- **Must drill**: max(dict, key=lambda) pattern until fluent

Next Review Schedule:
- **Daily practice required** until lambda/max syntax is automatic
- Tomorrow (Aug 31): 1st review - focus on syntax fluency
- Sept 1: 2nd review (+1 day due to syntax struggles)  
- Sept 3: 3rd review (+2 days)
- Sept 6: 4th review (+3 days)
- Sept 9: Final review before interview

Time Complexity: O(n) - single pass + dictionary key iteration
Space Complexity: O(n) - stores all non-space character positions
Pattern Type: Frequency counting with position-based tie-breaking
Core Skills: Dictionary usage, defaultdict, enumerate, max() with custom key

Key Strengths Demonstrated:
- Correct algorithmic thinking for frequency + tie-breaking problem
- Professional hint-requesting behavior (matches Affirm interview expectations)
- Quick bug identification and correction (append vs overwrite)
- Understanding of space complexity with index storage
- Recognition that dictionary insertion order handles ties elegantly

Areas for Major Improvement:
- **Critical**: Lambda expressions and max() key parameter syntax
- **Critical**: max(container, key=function) pattern recognition  
- Alternative manual approaches for clearer interview communication
- Complexity analysis over-complication (simpler explanations preferred)

Status: 🔄 REQUIRES DAILY REPETITION - Syntax mastery essential for interview
Note: Algorithm understanding is solid; syntax fluency is the blocking issue
"""
