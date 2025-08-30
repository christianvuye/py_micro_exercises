"""
Anagrams - Spaced Repetition

Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether the two strings are anagrams of each other.

Two strings are anagrams if they contain the same characters with the same frequencies.
Only consider alphabetic characters and ignore case.

Sample Test Cases:
anagrams("restful", "fluster") → True
anagrams("cats", "tocs") → False

After completing, analyze time and space complexity.
"""


def anagrams(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams, considering only alphabetic characters and ignoring case.
    Returns True if both strings have the same character frequencies, False otherwise.
    """
    s1_unique_char_freq = {}
    for char in s1:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower not in s1_unique_char_freq:
                s1_unique_char_freq[char_lower] = 1
            else:
                s1_unique_char_freq[char_lower] += 1
    for char in s2:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower not in s1_unique_char_freq:
                return False
            s1_unique_char_freq[char_lower] -= 1
            if s1_unique_char_freq[char_lower] < 0:
                return False
    return all(count == 0 for count in s1_unique_char_freq.values())


def test_anagrams_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Basic anagram
    result = anagrams("restful", "fluster")
    expected = True
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Different characters
    result = anagrams("cats", "tocs")
    expected = False
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_anagrams_sample()

"""
=== EXERCISE #12 SUMMARY - ANAGRAMS (SPACED REPETITION) ===

Pattern Mastery: 🟡 FUNCTIONAL WITH OPTIMIZATION INSIGHTS
- Correct frequency counting approach with case normalization
- Proper filtering of non-alphabetic characters using .isalpha()
- Evolved from basic two-dictionary comparison to single-pass optimization
- Strong understanding of early termination logic and algorithm improvement

Interview Readiness: 🟡 NEEDS ADDITIONAL PRACTICE
- Professional edge case clarification questions (excellent interview behavior)
- **Struggle Point**: Initial logic bug (char vs char_lower in condition)
- **Struggle Point**: Dead code in elif/else chain during optimization attempt
- **Critical Gap**: Needed guidance on generator expressions and all() function

Spaced Repetition Performance: 🔴 REQUIRES INTENSIVE PRACTICE
- Asked appropriate clarifying questions about case sensitivity and filtering
- Successfully debugged implementation with hints
- Showed strong algorithmic thinking about optimization opportunities
- **Must drill**: Generator expressions, all() function, early termination patterns

Next Review Schedule:
- **Daily practice required** until completely fluent without assistance
- Tomorrow (Aug 31): 1st review - focus on syntax and logic flow
- Sept 1: 2nd review (+1 day due to struggles)
- Sept 3: 3rd review (+2 days) 
- Sept 6: 4th review (+3 days)
- Sept 9: Final review before interview

Time Complexity: O(n + m) worst case, early termination optimization possible
Space Complexity: O(1) - maximum 26 characters for English alphabet
Pattern Type: Frequency counting with character filtering and case normalization
Core Skills: Dictionary manipulation, string processing, optimization thinking

Key Strengths Demonstrated:
- Professional interview communication with edge case questions
- Strong algorithmic optimization intuition (early termination concept)
- Successful debugging of logic errors with guidance
- Evolution from working solution to optimized single-pass algorithm
- Understanding of space complexity with alphabet size constraints

Areas for Major Improvement:
- **Critical**: Generator expressions and all() function comprehension
- **Critical**: Early termination implementation without dead code
- **Important**: Single-pass optimization patterns for frequency problems
- **Important**: String processing with filtering and normalization fluency

Status: 🔄 REQUIRES DAILY REPETITION - Algorithm understanding solid, syntax fluency needed
Note: Strong problem-solving approach but struggled with Python syntax implementation
"""
