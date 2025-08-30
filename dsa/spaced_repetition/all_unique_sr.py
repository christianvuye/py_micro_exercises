"""
All Unique - Spaced Repetition

Write a function, all_unique, that takes in a list. The function should return
a boolean indicating whether or not the list contains unique items.

Example:
all_unique([1, 2, 3, 4]) → True
all_unique([1, 2, 2, 3]) → False
all_unique([]) → True
all_unique(['a', 'b', 'c']) → True
all_unique(['a', 'a']) → False

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def all_unique(lst: list[int | str | tuple | bool | float | None]) -> bool:
    """
    Checks if all elements in the given list are unique.

    Args:
        lst (list[int | str | tuple | bool | float | None]): The list of elements to check for uniqueness.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    unique_values = set()
    for item in lst:
        if item in unique_values:
            return False
        else:
            unique_values.add(item)
    return True


Value = int | str | tuple | bool


def generate_large_list(
    n: int,
    a: Value,
    b: Value | None = None,
) -> list[Value]:
    """
    Generates a list of specified length, filled with one or two repeated values.

    Args:
        n (int): The length of the list to generate.
        a (Value): The primary value to repeat in the list.
        b (Value | None, optional): The secondary value to alternate with. If None, only 'a' is used.

    Returns:
        list[Value]: A list containing the repeated value(s).

    Examples:
        >>> generate_large_list(3, 'a')
        ['a', 'a', 'a']
        >>> generate_large_list(4, 1, 2)
        [1, 2, 1, 2]
        >>> generate_large_list(5, True, False)
        [True, False, True, False, True]
    """
    if b is None:
        return [a] * n
    return [a, b] * (n // 2) + ([a] if n % 2 else [])


def test_all_unique():
    """
    Tests the all_unique function with various input cases to verify its correctness.

    The test cases include:
    - Lists with all unique elements (integers and strings).
    - Lists with duplicate elements.
    - An empty list.
    - Lists with string elements, both unique and duplicate.

    Asserts that the output of all_unique matches the expected result for each test case.
    Prints "All tests passed!" if all assertions succeed.
    """

    # Test 1
    to_evaluate = [1, 2, 3, 4]
    expected = True
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 2
    to_evaluate = [1, 2, 2, 3]
    expected = False
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 3
    to_evaluate = []
    expected = True
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 4
    to_evaluate = ["a", "b", "c"]
    expected = True
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 5
    to_evaluate = ["a", "a"]
    expected = False
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 6
    to_evaluate = generate_large_list(1000, "chris")
    expected = False
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    # Test 7
    to_evaluate = generate_large_list(1000, "chris", 25)
    expected = False
    result = all_unique(to_evaluate)
    assert expected == result, f"TEST FAILED, Expected: {expected}, got {result}"

    print("All tests passed!")


test_all_unique()

"""
=== EXERCISE #6 SUMMARY - ALL UNIQUE (SPACED REPETITION) ===

Pattern Mastery: 🟢 SOLID UNDERSTANDING
- Set-based existence checking pattern well applied from has_duplicates
- Correct early termination logic after initial bug fix
- Clean implementation with proper edge case handling (empty list)

Interview Readiness: 🟢 STRONG PROFESSIONAL APPROACH  
- Excellent clarifying questions about data types and empty list behavior
- Quick error recognition and correction when logic bug pointed out
- Good complexity analysis with minor notation precision needed
- Self-aware about testing approaches and interview norms

Spaced Repetition Performance: 📈 BUILDING CONSISTENCY
- Applied previous set-based pattern correctly
- Initial logic inversion bug shows need for careful verification
- Strong testing instincts (though over-engineered for interview context)
- Good learning adaptation when given feedback about interview norms

Next Review Schedule:
- Tomorrow (Aug 30): 1st review  
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(1) best case, O(n) worst case
Space Complexity: O(1) best case, O(n) worst case  
Pattern Type: Set-based uniqueness verification with early termination
Core Skills: Hash table optimization, boolean logic, early return patterns

Key Strengths Demonstrated:
- Professional requirements clarification (data types, empty list edge case)
- Quick debugging when logic error identified
- Understanding of early termination optimization benefits
- Adaptability when learning interview vs production testing approaches
- Solid complexity analysis with good intuition for best/worst cases

Areas for Refinement:
- Complexity notation precision (avoid "O(2) but O(1)" type statements)
- Interview-focused testing over performance stress testing
- Initial implementation verification before assuming correctness

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows strong pattern transfer ability and professional interview instincts
"""
