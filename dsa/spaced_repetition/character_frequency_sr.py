"""
Character Frequency - Spaced Repetition

Write a function, character_frequency, that takes in a string as an argument.
The function should return a dictionary where keys are characters and values
are their frequency counts in the string.

Example:
character_frequency("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
character_frequency("aabbcc") → {'a': 2, 'b': 2, 'c': 2}
character_frequency("") → {}

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def character_frequency(s: str) -> dict[str, int]:
    """
    Calculates the frequency of each character in the input string.

    Args:
        s (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each character in the string to its frequency count.
    """
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency


def test_character_frequency():
    """
    Tests the character_frequency function with multiple test cases.

    Test cases:
        1. Checks frequency of characters in "hello".
        2. Checks frequency of characters in "aabbcc".
        3. Checks frequency of characters in an empty string.
        4. Checks frequency of characters in a string with repeated 'a's.
        5. Checks frequency of characters in a single-character string "a".
        6. Checks frequency of characters in a string with spaces and punctuation "a b!".

    Asserts that the output of character_frequency matches the expected result for each case.
    """
    # Test 1
    string = "hello"
    expected = {"h": 1, "e": 1, "l": 2, "o": 1}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )

    # Test 2
    string = "aabbcc"
    expected = {"a": 2, "b": 2, "c": 2}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )

    # Test 3
    string = ""
    expected = {}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )

    # Test 4
    string = "aaaaaaaaaa"
    expected = {"a": 10}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )

    # Test 5
    string = "a"
    expected = {"a": 1}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )

    # Test 6
    string = "a b!"
    expected = {"a": 1, " ": 1, "b": 1, "!": 1}
    result = character_frequency(string)
    assert expected == result, (
        f"TEST FAILED: Expected value {expected} != result: {result}"
    )


test_character_frequency()

"""
=== EXERCISE #3 SUMMARY - CHARACTER FREQUENCY (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG PROGRESS
- Dictionary accumulation pattern implemented cleanly
- Manual approach shows solid understanding of fundamentals
- Correct if-else logic for key existence checking

Interview Readiness: 🟢 EXCELLENT ANALYTICAL SKILLS
- Outstanding requirements clarification questions (spaces, punctuation)
- Caught instructor error in space complexity explanation
- Strong critical thinking about what data structures actually store
- Knowledge of library alternatives (defaultdict, Counter) with trade-offs

Spaced Repetition Performance: 📈 EXCELLENT FIRST ATTEMPT
- Clean manual implementation without library dependencies
- Comprehensive test coverage with assert statements
- Good edge case thinking (empty string, repeated characters)
- Professional approach to ambiguous requirements

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(n) where n = string length
Space Complexity: O(k) where k = unique characters, worst case O(n)
Pattern Type: Dictionary accumulation with frequency counting
Core Skills: Hash table operations, key existence checking, requirements clarification

Key Strengths Demonstrated:
- Excellent requirements clarification: "should I count spaces and punctuation?"
- Caught instructor's imprecise space complexity explanation
- Correct understanding that frequency storage is additional space beyond input
- Knowledge of defaultdict(int) and Counter alternatives
- Clean manual implementation demonstrating fundamental understanding

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows exceptional analytical thinking and professional interview behavior
"""
