"""
Duplicate Groups - Spaced Repetition

Write a function, duplicate_groups, that takes in a list as an argument.
The function should return a dictionary where keys are duplicate values and values are lists of indices where those duplicates occur.

Only include values that appear more than once in the input list.

Sample Test Cases:
duplicate_groups([1, 2, 3, 2, 1, 4]) → {1: [0, 4], 2: [1, 3]}
duplicate_groups(['a', 'b', 'a', 'c', 'b']) → {'a': [0, 2], 'b': [1, 4]}

After completing, analyze time and space complexity.
"""


def duplicate_groups(lst: list) -> dict[list]:
    """
    Finds all duplicate values in the input list and groups their indices.

    Args:
        lst (list): The list to search for duplicate values.

    Returns:
        dict[list]: A dictionary where each key is a duplicated value from the input list,
                    and the corresponding value is a list of indices where that value occurs.
                    Only values that appear more than once are included.
    """
    duplicate_values = {}
    for index, value in enumerate(lst):
        if value not in duplicate_values:
            duplicate_values[value] = [index]
        else:
            duplicate_values[value].append(index)
    return {k: v for k, v in duplicate_values.items() if len(v) > 1}


def test_duplicate_groups_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Numbers with duplicates
    result = duplicate_groups([1, 2, 3, 2, 1, 4])
    expected = {1: [0, 4], 2: [1, 3]}
    assert result == expected, f"Expected {expected}, got {result}"

    # Sample Case 2: Strings with duplicates
    result = duplicate_groups(["a", "b", "a", "c", "b"])
    expected = {"a": [0, 2], "b": [1, 4]}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_duplicate_groups_sample()

"""
=== EXERCISE #13 SUMMARY - DUPLICATE GROUPS (SPACED REPETITION) ===

Pattern Mastery: 🟢 CORRECT ALGORITHM WITH SYNTAX ERRORS
- Perfect index collection approach using enumerate and dictionary accumulation
- Correct understanding of filtering duplicates (len(v) > 1) after collection phase
- Clean two-phase approach: collect all indices, then filter for duplicates only
- Strong grasp of dictionary key-value relationship for grouping problem

Interview Readiness: 🟡 SYNTAX FLUENCY NEEDED
- **Struggle Point**: Used set comprehension `{(k, v) for...}` instead of dict comprehension `{k: v for...}`
- **Error Analysis**: Attempted to put tuples containing lists into a set (unhashable type error)
- Professional debugging approach when encountering TypeError
- Quick correction once syntax difference was clarified

Spaced Repetition Performance: 🔴 REQUIRES DAILY SYNTAX PRACTICE
- Algorithm understanding was solid from the start
- Implementation logic was perfect (collect first, filter second)
- **Critical Gap**: Dictionary vs set comprehension syntax confusion
- **Must drill**: Comprehension syntax until automatic - this is basic Python fluency

Next Review Schedule:
- **Daily practice required** until dict comprehension syntax is automatic
- Tomorrow (Sept 1): 1st review - focus on comprehension syntax
- Sept 2: 2nd review (+1 day due to syntax struggles)
- Sept 4: 3rd review (+2 days)
- Sept 7: 4th review (+3 days)
- Sept 9: Final review before interview

Time Complexity: O(n) - enumerate through list + dictionary iteration for filtering
Space Complexity: O(n) - stores all n indices across all value lists, plus O(k) keys
Pattern Type: Index collection with duplicate filtering via dictionary accumulation
Core Skills: enumerate usage, dictionary comprehension, duplicate detection

Key Strengths Demonstrated:
- Perfect algorithmic approach for index grouping problem
- Excellent complexity analysis including edge cases and optimization insights
- Understanding of two-phase processing (collect all, filter duplicates)
- Strong debugging skills when encountering type errors
- Comprehensive edge case consideration (empty lists, single elements, mixed types)

Areas for Major Improvement:
- **Critical**: Dictionary comprehension syntax vs set comprehension syntax
- **Critical**: Understanding when to use `{k: v for...}` vs `{(k, v) for...}` vs `[k for...]`
- **Important**: Basic Python comprehension patterns must be automatic for interviews

Status: 🔄 REQUIRES DAILY REPETITION - Algorithm perfect, syntax mastery essential
Note: This is fundamental Python syntax that must be fluent for technical interviews
"""
