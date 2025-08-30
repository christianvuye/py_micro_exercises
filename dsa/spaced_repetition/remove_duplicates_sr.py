"""
Remove Duplicates - Spaced Repetition

Write a function, remove_duplicates, that takes in a list as an argument.
The function should return a new list with duplicate elements removed.
The order of elements should be preserved based on their first occurrence.

Example:
remove_duplicates([1, 2, 3, 2, 1, 4]) → [1, 2, 3, 4]
remove_duplicates([5, 5, 5, 5]) → [5]
remove_duplicates([]) → []
remove_duplicates([1]) → [1]
remove_duplicates(['a', 'b', 'a', 'c', 'b']) → ['a', 'b', 'c']

Write your own test cases and implement the solution.
After completing, analyze time and space complexity.
"""


def remove_duplicates(lst: list) -> list:
    """
    Removes duplicate elements from a list while preserving the original order.

    Args:
        lst (list[Any]): The input list from which duplicates should be removed.

    Returns:
        list[Any]: A new list containing only the first occurrence of each element from the input list.

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1])
        [1, 2, 3]
    """
    unique_values = set()
    lst_deduplicated = []
    for element in lst:
        if element not in unique_values:
            unique_values.add(element)
            lst_deduplicated.append(element)
    return lst_deduplicated


def test_remove_duplicates():
    """Comprehensive test cases for validation"""

    # Test Case 1: Basic example from problem
    input_data = [1, 2, 3, 2, 1, 4]
    expected = [1, 2, 3, 4]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 2: All same elements
    input_data = [5, 5, 5, 5]
    expected = [5]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 3: Empty list
    input_data = []
    expected = []
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 4: Single element
    input_data = [1]
    expected = [1]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 5: Mixed types
    input_data = ["a", "b", "a", "c", "b"]
    expected = ["a", "b", "c"]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 6: No duplicates
    input_data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 7: Mixed data types
    input_data = [1, "a", 1.5, "a", 1]
    expected = [1, "a", 1.5]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 8: Boolean/integer equality edge case
    input_data = [1, True, 0, False]
    expected = [1, 0]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 9: Float/integer equality
    input_data = [1, 1.0, 2, 2.0]
    expected = [1, 2]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 10: Special characters and strings
    input_data = ["!", "@", "!", "#", "@"]
    expected = ["!", "@", "#"]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    # Test Case 11: None values
    input_data = [None, 1, None, 2]
    expected = [None, 1, 2]
    result = remove_duplicates(input_data)
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")


test_remove_duplicates()

"""
=== EXERCISE #10 SUMMARY - REMOVE DUPLICATES (SPACED REPETITION) ===

Pattern Mastery: 🟢 OPTIMAL ALGORITHM SELECTION
- Perfect combination of set (tracking) + list (order preservation)
- Correct understanding that sets alone cannot solve order-preserving deduplication
- Clean single-pass implementation with proper edge case handling
- Strong grasp of data structure trade-offs for specific requirements

Interview Readiness: 🟢 EXCELLENT ENGINEERING PRACTICES
- Empirical testing of alternative approaches (list(set(lst)))
- Accurate complexity analysis with minor clarification needed
- Professional input constraint questions about mixed types and hashability
- Understanding of Python equality edge cases (1/True, 0/False, 1/1.0)

Spaced Repetition Performance: 📈 STRONG ANALYTICAL VERIFICATION
- Applied familiar set-based pattern to new order-preservation requirement
- Self-directed testing of theoretical assumptions vs practical results
- Demonstrated that empirical evidence beats theoretical reasoning
- Quick recognition of optimal approach for constraint satisfaction

Next Review Schedule:
- Tomorrow (Aug 30): 1st review
- Sept 1: 2nd review (+2 days)
- Sept 4: 3rd review (+3 days)
- Sept 8: 4th review (+4 days)
- Interview Sept 10: Should be automatic by then

Time Complexity: O(n) - always scan entire input regardless of duplicates
Space Complexity: O(k) where k = unique elements, worst case O(n)
Pattern Type: Set-based tracking with order-preserving list construction
Core Skills: Data structure combination, order preservation, empirical validation

Key Strengths Demonstrated:
- Optimal algorithm selection for order-preserving deduplication
- Empirical testing of alternative solutions (engineering rigor)
- Accurate complexity analysis understanding with search results validation
- Professional handling of mixed type constraints and equality edge cases
- Strong pattern adaptation from basic set operations to order-preservation

Areas for Minor Refinement:
- Type hint syntax (list[Any] vs list[any], or simpler list for interviews)
- Time complexity precision (always O(n), not conditional on duplicate distribution)

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule to achieve mastery
Note: Shows excellent engineering verification practices and optimal solution design
"""
