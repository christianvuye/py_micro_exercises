"""
Word Frequency Counter - Advanced Word Counting Techniques

Build a word frequency analyzer for text processing. Given a string of text,
count how many times each word appears and return the words that appear more than once.

Requirements:
- Words are separated by spaces
- Ignore case (so 'The' and 'the' are the same word)
- Remove punctuation from words
- Return list of words that appear more than once
- Optimize for processing large text documents

The input text could be quite large - think about efficiency.
"""


def word_frequency_counter(text: str) -> list[str]:
    """
    Returns a list of words that appear more than once in the given text.

    The function processes the input text by:
    - Converting all characters to lowercase.
    - Splitting the text into words.
    - Removing non-alphabetic characters from each word.
    - Counting the frequency of each cleaned word.
    - Returning a list of words that occur more than once.

    Args:
        text (str): The input text to analyze.

    Returns:
        list[str]: A list of words (in lowercase, alphabetic only) that appear more than once.
    """
    text_lower = text.lower()
    words = text_lower.split()
    word_freq = {}
    for word in words:
        temp_word = []
        for char in word:
            if char.isalpha():
                temp_word.append(char)
        cleaned_word = "".join(temp_word)
        if len(cleaned_word) > 0:
            if cleaned_word not in word_freq:
                word_freq[cleaned_word] = 1
            else:
                word_freq[cleaned_word] += 1
    return [k for k, v in word_freq.items() if v > 1]


# Sample test cases (HackerRank format)
def test_word_frequency_counter():
    # Sample Case 1: Basic duplicate detection
    text1 = "the quick brown fox jumps over the lazy dog the fox"
    result1 = word_frequency_counter(text1)
    expected1 = ["the", "fox"]
    assert set(result1) == set(expected1), f"Expected {expected1}, got {result1}"

    # Sample Case 2: Case insensitive
    text2 = "Hello world hello WORLD"
    result2 = word_frequency_counter(text2)
    expected2 = ["hello", "world"]
    assert set(result2) == set(expected2), f"Expected {expected2}, got {result2}"

    # Sample Case 3: Punctuation handling
    text3 = "apple, banana apple. orange! banana?"
    result3 = word_frequency_counter(text3)
    expected3 = ["apple", "banana"]
    assert set(result3) == set(expected3), f"Expected {expected3}, got {result3}"

    print("Sample tests passed!")


# Run sample tests after implementation
test_word_frequency_counter()

"""
=== EXERCISE #29 SUMMARY - WORD FREQUENCY COUNTER (SPACED REPETITION) ===

Pattern Mastery: 🟢 CLEAN TEXT PROCESSING EXECUTION
- Manual character filtering with .isalpha() approach
- Proper edge case handling for empty words after punctuation removal
- Clean frequency counting with manual dictionary management

Interview Readiness: 🟢 EXCEPTIONAL COMPLEXITY REASONING
- Precise O(n × m) complexity analysis correctly identifying nested loop structure
- Corrected instructor's oversimplified O(n) analysis with sophisticated reasoning
- Advanced understanding of string processing costs and character-level operations
- Professional edge case consideration (empty strings, punctuation-only words)

Spaced Repetition Performance: 📈 STRONG PROBLEM-SOLVING APPROACH
- Creative solution using .isalpha() instead of regex or library functions
- Quick debugging and fix for empty word edge case
- Superior algorithmic analysis demonstrating deep understanding of nested processing

Next Review Schedule:
- Sept 2: 1st review (+2 days)
- Sept 5: 2nd review (+3 days)
- Sept 9: 3rd review (+4 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n × m) where n=words, m=avg chars per word (equivalent to O(N) total chars)
Space Complexity: O(N) - multiple string copies and dictionary storage
Pattern Type: Text preprocessing + frequency analysis with manual character filtering
Core Skills: String processing, character validation, nested loop analysis

Key Strengths Demonstrated:
- **Superior complexity analysis**: Correctly identified O(n × m) nested structure
- **Critical thinking**: Questioned and corrected instructor's complexity simplification
- **Precise algorithmic reasoning**: Distinguished between loop structure and total work
- **Advanced understanding**: Recognized equivalence between O(n × m) and O(N) notations

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule
Note: Shows exceptional algorithmic analysis skills - corrected instructor's oversimplification
"""
