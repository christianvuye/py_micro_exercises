"""
Fizz Buzz - Spaced Repetition

Write a function, fizz_buzz, that takes in a number n as an argument. The function
should return a list containing numbers from 1 to n, replacing certain numbers
according to the following rules:

* if the number is divisible by 3, make the element "fizz"
* if the number is divisible by 5, make the element "buzz"
* if the number is divisible by 3 and 5, make the element "fizzbuzz"

Example:
fizz_buzz(5) → [1, 2, "fizz", 4, "buzz"]
fizz_buzz(15) → [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def fizz_buzz(n: int) -> list[int | str]:
    """docstring"""
    if n < 1:
        return []
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 5 == 0:
            result.append("buzz")
        elif i % 3 == 0:
            result.append("fizz")
        else:
            result.append(i)
    return result


def test_fizz_buzz():
    """docstring"""

    # Test 1
    input = -1
    expected = []
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 2
    input = 0
    expected = []
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 3
    input = 1
    expected = [1]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 4
    input = 2
    expected = [1, 2]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 5
    input = 3
    expected = [1, 2, "fizz"]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 6
    input = 4
    expected = [1, 2, "fizz", 4]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 7
    input = 5
    expected = [1, 2, "fizz", 4, "buzz"]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 8
    input = 15
    expected = [
        1,
        2,
        "fizz",
        4,
        "buzz",
        "fizz",
        7,
        8,
        "fizz",
        "buzz",
        11,
        "fizz",
        13,
        14,
        "fizzbuzz",
    ]
    result = fizz_buzz(input)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    print("ALL TESTS PASSED!")


# Run your tests
test_fizz_buzz()

"""
=== EXERCISE #8 SUMMARY - FIZZ BUZZ (SPACED REPETITION) ===

Pattern Mastery: 🟢 SOLID CONDITIONAL LOGIC
- Correct conditional precedence (fizzbuzz before fizz/buzz)
- Clean list building with mixed data types (int | str)
- Proper edge case handling for n < 1 scenarios
- Sound iterative approach with appropriate range usage

Interview Readiness: 🟢 COMPREHENSIVE APPROACH
- Professional input validation questions about constraints
- Excellent progressive test coverage (1→2→3→4→5→15)
- Accurate complexity analysis with realistic optimization assessment  
- Minor type hint correction needed (list[int, str] → list[int | str])

Spaced Repetition Performance: 📈 BUILDING PATTERN DIVERSITY
- Fourth different algorithmic pattern (after hash tables, math, conditional logic)
- Strong edge case intuition across multiple problem types
- Correct skepticism about optimization possibilities (O(n) is inherent)
- Good analysis of alternative implementation trade-offs

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)  
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(n) - must process every position from 1 to n
Space Complexity: O(n) - output list grows linearly with input
Pattern Type: Iterative list construction with conditional logic
Core Skills: Modulo operations, conditional precedence, mixed-type lists

Key Strengths Demonstrated:
- Proper conditional ordering to handle overlapping cases (divisible by both)
- Comprehensive test strategy with incremental complexity building
- Realistic understanding of algorithmic limitations (no sub-O(n) solution exists)
- Good analysis of alternative approaches and their trade-offs
- Professional constraint clarification before implementation

Areas for Refinement:
- Python type hint syntax for union types (| operator)
- Continue building confidence in complexity analysis accuracy

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows strong pattern recognition across diverse algorithm types
"""
