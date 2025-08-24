"""
First Repeated Element

Write a function `first_repeated` that takes in a string as an argument.
The function should return the first character that appears more than once in the string.
If no character repeats, return None.

Example:
first_repeated("hello") → 'l'
first_repeated("abcdef") → None
first_repeated("abccba") → 'c'
first_repeated("") → None

Test Cases (copy-paste below your function):

import time

def test_first_repeated():
    # Test case 1: Has repeated character
    result1 = first_repeated("hello")
    print(f"Test 1 - Has repeat: {result1 == 'l'}")

    # Test case 2: No repeated characters
    result2 = first_repeated("abcdef")
    print(f"Test 2 - No repeat: {result2 is None}")

    # Test case 3: Multiple repeats, return first
    result3 = first_repeated("abccba")
    print(f"Test 3 - First repeat: {result3 == 'c'}")

    # Test case 4: Empty string
    result4 = first_repeated("")
    print(f"Test 4 - Empty: {result4 is None}")

    # Test case 5: First character repeats
    result5 = first_repeated("aabcd")
    print(f"Test 5 - First char repeats: {result5 == 'a'}")

    # Test case 6: Last character repeats
    result6 = first_repeated("abcdd")
    print(f"Test 6 - Last char repeats: {result6 == 'd'}")

    # Test case 7: All same character
    result7 = first_repeated("aaaa")
    print(f"Test 7 - All same: {result7 == 'a'}")

    # Performance comparison test
    # Create string where repeated char is near the end
    large_string = ''.join([chr(65 + i % 26) for i in range(10000)]) + 'A'
    # This creates "ABCD...ZABCD...ZA" - first repeat is 'A' after 26*384 + 1 chars

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = first_repeated(large_string)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,001 chars, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive approach checking all previous chars
    def naive_first_repeated(s):
        for i in range(len(s)):
            for j in range(i):  # Check all previous characters
                if s[i] == s[j]:
                    return s[i]
        return None

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_first_repeated(large_string[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 chars, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time/10*100)/(optimized_time):.1f}x faster")

# Run tests after implementing your function
# test_first_repeated()
"""

import time


def first_repeated(s: str) -> str | None:
    """
    Returns the first character that appears more than once in the input string.

    Args:
        s (str): The string to search.

    Returns:
        str | None: The first repeated character, or None if no character repeats.
    """
    past_chars = set()

    for char in s:
        if char in past_chars:
            return char
        else:
            past_chars.add(char)


def test_first_repeated():
    # Test case 1: Has repeated character
    result1 = first_repeated("hello")
    print(f"Test 1 - Has repeat: {result1 == 'l'}")

    # Test case 2: No repeated characters
    result2 = first_repeated("abcdef")
    print(f"Test 2 - No repeat: {result2 is None}")

    # Test case 3: Multiple repeats, return first
    result3 = first_repeated("abccba")
    print(f"Test 3 - First repeat: {result3 == 'c'}")

    # Test case 4: Empty string
    result4 = first_repeated("")
    print(f"Test 4 - Empty: {result4 is None}")

    # Test case 5: First character repeats
    result5 = first_repeated("aabcd")
    print(f"Test 5 - First char repeats: {result5 == 'a'}")

    # Test case 6: Last character repeats
    result6 = first_repeated("abcdd")
    print(f"Test 6 - Last char repeats: {result6 == 'd'}")

    # Test case 7: All same character
    result7 = first_repeated("aaaa")
    print(f"Test 7 - All same: {result7 == 'a'}")

    # Performance comparison test
    # Create string where repeated char is near the end
    large_string = "".join([chr(65 + i % 26) for i in range(10000)]) + "A"
    # This creates "ABCD...ZABCD...ZA" - first repeat is 'A' after 26*384 + 1 chars

    # Time your optimized solution
    start_time = time.time()
    for _ in range(100):
        result = first_repeated(large_string)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (10,001 chars, 100 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

    # Reference: naive approach checking all previous chars
    def naive_first_repeated(s):
        for i in range(len(s)):
            for j in range(i):  # Check all previous characters
                if s[i] == s[j]:
                    return s[i]
        return None

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_first_repeated(large_string[:1000])
    naive_time = time.time() - start_time

    print(f"Naive O(n²) time (1,000 chars, 10 iterations): {naive_time:.4f} seconds")
    print(
        f"Estimated speedup: ~{(naive_time / 10 * 100) / (optimized_time):.1f}x faster"
    )


# Run tests after implementing your function
test_first_repeated()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Implementation:
- First used Counter approach, misunderstood requirement as "first character with count > 1"
- Failed Test 3: returned 'a' instead of 'c' for "abccba" 

Requirement Clarification:
- Quickly recognized misunderstanding: "ah, its a misunderstanding of the requirement"
- Understood distinction: "first repeated" = first moment of encountering duplicate, not first character with multiple occurrences

Corrected Implementation:
- Used optimal set-based approach: track seen characters, return on first duplicate encounter
- Pattern: `if char in past_chars: return char else: past_chars.add(char)`
- All test cases passed with early termination optimization

Complexity Analysis Performance:
- Best case: O(1) time/space (correctly identified) ✅
- Worst case: O(n) time/space ✅  
- Space growth understanding: "From O(1) to O(n) depending on when repeat found" ✅
- Good constant recognition: "O(2) -> very quick... O(1) because we drop constants"

Core Pattern Mastered:
"Have I seen this before?" detection with early termination - foundation for duplicate detection problems
"""
