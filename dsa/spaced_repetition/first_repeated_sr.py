"""
First Repeated - Spaced Repetition

Write a function, first_repeated, that takes in a string as an argument.
The function should return the first character that appears more than once
in the string. If no character repeats, return None.

Example:
first_repeated("abccba") → "c"
first_repeated("abcdef") → None
first_repeated("hello") → "l"
first_repeated("") → None

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def first_repeated(string: str) -> str | None:
    """
    Finds and returns the first repeated character in a given string.

    Args:
        string (str): The input string to search for repeated characters.

    Returns:
        str | None: The first character that repeats in the string, or None if no character repeats.
    """
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return char
        else:
            unique_chars.add(char)
    return None


def test_first_repeated():
    """Test cases in assertion format for practice validation"""

    # Test Case 1: Basic example from problem
    assert first_repeated("abccba") == "c", (
        f"Expected 'c', got {first_repeated('abccba')}"
    )

    # Test Case 2: No repeats
    assert first_repeated("abcdef") is None, (
        f"Expected None, got {first_repeated('abcdef')}"
    )

    # Test Case 3: Basic example with 'l' repeat
    assert first_repeated("hello") == "l", (
        f"Expected 'l', got {first_repeated('hello')}"
    )

    # Test Case 4: Empty string
    assert first_repeated("") is None, f"Expected None, got {first_repeated('')}"

    # Test Case 5: Single character
    assert first_repeated("a") is None, f"Expected None, got {first_repeated('a')}"

    # Test Case 6: Immediate repeat
    assert first_repeated("aabcd") == "a", (
        f"Expected 'a', got {first_repeated('aabcd')}"
    )

    # Test Case 7: Multiple repeats - first one wins
    assert first_repeated("abcabc") == "a", (
        f"Expected 'a', got {first_repeated('abcabc')}"
    )

    # Test Case 8: Case sensitivity - different cases
    assert first_repeated("Aa") is None, f"Expected None, got {first_repeated('Aa')}"

    # Test Case 9: Special characters
    assert first_repeated("a!b!c") == "!", (
        f"Expected '!', got {first_repeated('a!b!c')}"
    )

    # Test Case 10: All same character
    assert first_repeated("aaaa") == "a", f"Expected 'a', got {first_repeated('aaaa')}"

    print("All tests passed!")


test_first_repeated()

"""
=== EXERCISE #9 SUMMARY - FIRST REPEATED (SPACED REPETITION) ===

Pattern Mastery: 🟢 EXCELLENT PATTERN TRANSFER
- Applied "have I seen this before?" pattern from has_duplicates/all_unique
- Set-based tracking with early termination optimization perfectly executed
- Clean single-pass algorithm with optimal early return logic
- Strong understanding of pattern family variations (existence vs identification)

Interview Readiness: 🟢 PROFESSIONAL APPROACH
- Excellent clarifying questions about case sensitivity and input types
- Caught instructor error on Python best practice (`is None` vs `== None`)
- Understanding of HackerRank interview format vs practice testing approaches
- Clean implementation with proper type hints and documentation

Spaced Repetition Performance: 📈 ACCELERATING PATTERN RECOGNITION
- Immediate recognition of similarity to previous set-based exercises
- Faster implementation time showing pattern internalization
- Self-correction on Python idioms showing attention to code quality
- Efficient edge case handling without prompting

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(1) best case, O(n) worst case
Space Complexity: O(1) best case, O(n) worst case
Pattern Type: Set-based character tracking with early termination
Core Skills: Hash table optimization, early return patterns, string processing

Key Strengths Demonstrated:
- Immediate pattern recognition from previous similar exercises
- Professional clarifying questions about requirements and constraints
- Python best practice knowledge (`is None` over `== None`)
- Understanding of real interview platform constraints vs practice testing
- Accurate complexity analysis with clear best/worst case identification
- Clean code with proper type hints and documentation

Areas of Excellence:
- Pattern transfer ability across similar but distinct problems
- Code quality attention to Python idioms and best practices
- Professional interview question behavior matching real scenarios

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows strong progression in both pattern recognition and interview readiness
"""
