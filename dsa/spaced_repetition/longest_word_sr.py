"""
Longest Word - Spaced Repetition

Write a function, longest_word, that takes in a sentence string as an argument.
The function should return the longest word in the sentence. If there is a tie,
return the word that occurs later in the sentence.

You can assume that the sentence is non-empty.

Example:
longest_word("when in rome do as the romans do") → "romans"
longest_word("I love dogs") → "dogs"

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def longest_word(sentence: str) -> str:
    """
    Finds and returns the longest word in a given sentence. If multiple words have the same maximum length, returns the last one encountered.

    Args:
        sentence (str): The input sentence as a string.

    Returns:
        str: The longest word found in the sentence.
    """
    words = sentence.split(" ")
    longest_word = ""
    for word in words:
        if len(word) >= len(longest_word):
            longest_word = word
    return longest_word


def test_longest_word():
    """
    Tests the longest_word function with multiple sentences to verify correct identification of the longest word.

    Test Cases:
        1. Sentence: "when in rome do as the romans do"
           Expected Result: "romans"
        2. Sentence: "I love dogs"
           Expected Result: "love"

    Raises:
        Exception: If the actual result does not match the expected result for any test case.
    """
    # Test case 1
    sentence = "when in rome do as the romans do"
    expected = "romans"
    result = longest_word(sentence)
    if result == expected:
        print(f"TEST PASSED: Expected result: {expected} == Actual Result: {result}")
    else:
        raise Exception(
            f"TEST FAILED: Expected result: {expected} != Actual Result: {result}"
        )

    # Test case 2
    sentence = "I love dogs"
    expected = "dogs"
    result = longest_word(sentence)
    if result == expected:
        print(f"TEST PASSED: Expected result: {expected} == Actual Result: {result}")
    else:
        raise Exception(
            f"TEST FAILED: Expected result: {expected} != Actual Result: {result}"
        )

    # Test case 3
    sentence = "I"
    expected = "I"
    result = longest_word(sentence)
    if result == expected:
        print(f"TEST PASSED: Expected result: {expected} == Actual Result: {result}")
    else:
        raise Exception(
            f"TEST FAILED: Expected result: {expected} != Actual Result: {result}"
        )

    # Test case 4
    sentence = "same same same same"
    expected = "same"
    result = longest_word(sentence)
    if result == expected:
        print(f"TEST PASSED: Expected result: {expected} == Actual Result: {result}")
    else:
        raise Exception(
            f"TEST FAILED: Expected result: {expected} != Actual Result: {result}"
        )

    # Test case 5
    sentence = "A sentence with punctuation, with the current approach, means that a words lenght also includes the punctuation around it. Is that how it should be?"
    expected = "punctuation,"
    result = longest_word(sentence)
    if result == expected:
        print(f"TEST PASSED: Expected result: {expected} == Actual Result: {result}")
    else:
        raise Exception(
            f"TEST FAILED: Expected result: {expected} != Actual Result: {result}"
        )


# Run your tests
test_longest_word()


def longest_word_alternative(sentence: str) -> str:
    current_max_len = 0
    current_max_len_word = ""
    current_len = 0
    current_word = ""

    for char in sentence:
        if char != " ":
            current_len += 1
            current_word += char
        else:  # char == " "
            if current_len >= current_max_len:
                current_max_len = current_len
                current_max_len_word = current_word
            # Reset for next word
            current_word = ""
            current_len = 0

    # HANDLE LAST WORD (no trailing space)
    if current_len >= current_max_len:
        current_max_len_word = current_word

    return current_max_len_word


"""
=== EXERCISE #2 SUMMARY - LONGEST WORD (SPACED REPETITION) ===

Pattern Mastery: 🟢 STRONG PROGRESS
- String manipulation and iteration pattern well understood
- Correct tie-breaking logic implementation (>= operator)
- Clean single-pass approach with proper edge case handling

Interview Readiness: 🟢 VERY PROMISING
- Excellent critical thinking - correctly rejected instructor's flawed "optimization"
- Robust testing methodology with comprehensive edge cases
- Strong complexity analysis with proper variable definitions
- Good attention to requirements (caught instructor error in example)

Spaced Repetition Performance: 📈 EXCELLENT FIRST ATTEMPT
- Comprehensive test coverage including punctuation scenarios
- Proper documentation of assumptions about word boundaries
- Advanced algorithmic thinking about alternative approaches
- Critical evaluation of trade-offs and complexity

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(w × m) where w=words, m=avg word length
Space Complexity: O(w × m) due to split operation creating word list
Pattern Type: Linear scan with conditional updates and tie-breaking
Core Skills: String processing, tie-breaking logic, critical algorithm analysis

Key Strengths Demonstrated:
- Caught instructor error in problem example (attention to detail)
- Correctly rejected "optimization" that was actually worse (O(w × m²))
- Comprehensive test coverage with edge cases
- Strong complexity analysis and variable definition clarity
- Excellent critical thinking about algorithmic trade-offs

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows advanced analytical skills beyond typical first attempts
"""
