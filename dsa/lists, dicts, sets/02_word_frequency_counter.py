"""
Interviewer Problem Statement:
"I want you to build a word frequency analyzer for text processing. Given a string of text,
count how many times each word appears and return the words that appear more than once.

For example, if I give you:
'the quick brown fox jumps over the lazy dog the fox'

You should return something like ['the', 'fox'] because those words appear multiple times.

A few things to consider:
- Words are separated by spaces
- Ignore case (so 'The' and 'the' are the same word)
- Remove punctuation from words
- The input text could be quite large - think about efficiency

Here's a simple example: if the input is 'Hello world hello', you should return ['hello']."

Interviewer Requirements:
- Process text strings to identify frequently occurring words
- Handle case-insensitive matching (Hello = hello)
- Remove punctuation from words before counting
- Return list of words that appear more than once
- Optimize for processing large text documents (thousands of words)
- Handle edge cases like empty strings and single words

Tests that the code should pass:
# Test case 1: Basic duplicate detection
text1 = "the quick brown fox jumps over the lazy dog the fox"
result1 = find_duplicate_words(text1)  # Expected: ['the', 'fox'] (order doesn't matter)

# Test case 2: Case insensitive
text2 = "Hello world hello WORLD"
result2 = find_duplicate_words(text2)  # Expected: ['hello', 'world']

# Test case 3: Punctuation handling
text3 = "apple, banana apple. orange! banana?"
result3 = find_duplicate_words(text3)  # Expected: ['apple', 'banana']

# Test case 4: No duplicates
text4 = "every word appears once only"
result4 = find_duplicate_words(text4)  # Expected: []

# Test case 5: Empty string
text5 = ""
result5 = find_duplicate_words(text5)  # Expected: []

# Test case 6: Single word
text6 = "hello"
result6 = find_duplicate_words(text6)  # Expected: []

After implementation: Explain the time and space complexity and discuss potential optimizations
"""

import string


def find_duplicate_words(text: str) -> list[str]:
    """
    Finds and returns a list of words that appear more than once in the given text.

    The function removes punctuation, converts the text to lowercase, splits it into words,
    and identifies words that occur multiple times.

    Args:
        text (str): The input string to search for duplicate words.

    Returns:
        list[str]: A list of duplicate words found in the text.
    """
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    words = text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return [k for k, v in word_count.items() if v > 1]


# Test case 1: Basic duplicate detection
text1 = "the quick brown fox jumps over the lazy dog the fox"
result1 = find_duplicate_words(text1)  # Expected: ['the', 'fox'] (order doesn't matter)
print(result1)

# Test case 2: Case insensitive
text2 = "Hello world hello WORLD"
result2 = find_duplicate_words(text2)  # Expected: ['hello', 'world']
print(result2)

# Test case 3: Punctuation handling
text3 = "apple, banana apple. orange! banana?"
result3 = find_duplicate_words(text3)  # Expected: ['apple', 'banana']
print(result3)

# Test case 4: No duplicates
text4 = "every word appears once only"
result4 = find_duplicate_words(text4)  # Expected: []
print(result4)

# Test case 5: Empty string
text5 = ""
result5 = find_duplicate_words(text5)  # Expected: []
print(result5)

# Test case 6: Single word
text6 = "hello"
result6 = find_duplicate_words(text6)  # Expected: []
print(result6)

"""
Time complexity:
- Worst case: O(n), linear time complexity with the lenght of the string
(unless these string methods are doing something funky)

Space complexity:
- Worst case: O(n)
(unless these string methods are doing something funky)
"""


def find_top_k_words(text: str, k: int) -> list[tuple[str, int]]:
    """
    Finds the top k most frequent words in a given text.

    Args:
        text (str): The input text to analyze.
        k (int): The number of top frequent words to return.

    Returns:
        list[tuple[str, int]]: A list of tuples, each containing a word and its frequency.
        The list is sorted by frequency in descending order (most frequent words first).

    Note:
        Punctuation is removed and text is converted to lowercase before counting word frequencies.
        If fewer than k unique words exist in the text, returns all words sorted by frequency.
    """
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    words = text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    word_count_sorted = sorted(
        word_count.items(), key=lambda item: item[1], reverse=True
    )
    return word_count_sorted[:k]


"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Request: 
"Build a word frequency analyzer. Count how many times each word appears and return words that appear more than once. 
Handle case-insensitive matching, remove punctuation, optimize for large text documents."

Developer Clarifications Asked:
- "Can I import any libraries?"
- "Can I use regex generators or AI tools for regex?"
- "Is looking up syntax generally fine?"

Interviewer Responses:
- Approved basic Python libraries (string, re) but core logic should be implemented personally
- No AI tools or generators allowed
- Basic syntax lookup is typically fine, but avoid looking up solutions

Final Technical Decisions:
- Used string.punctuation with str.maketrans for punctuation removal
- Dictionary-based counting approach for O(n) time complexity
- Extended to top-K problem using sorted() with lambda key function
- Time complexity changed from O(n) to O(n log n) with sorting requirement
- Space complexity remains O(n) for word storage

Assumptions Documented:
- String methods (translate, lower, split) are all O(n) operations
- Sorting dictionary items is O(k log k) where k = unique words
- For top-K problems, full sorting may be suboptimal when k << n, but current solution is clean and correct
"""
