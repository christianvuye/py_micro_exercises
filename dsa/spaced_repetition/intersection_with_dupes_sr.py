"""
Intersection with Dupes - Intersection Preserving Counts

Write a function `intersection_with_dupes` that takes in two lists as arguments.
The function should return a new list containing elements that appear in both lists.
The elements in the result should appear as many times as they occur in both input lists.
You can return the result in any order.
"""

from collections import Counter


def intersection_with_dupes(list_a: list, list_b: list) -> list:
    """docstring"""
    if not list_a or not list_b:
        return []
    a_freq = Counter(list_a)
    b_freq = {}
    for element in list_b:
        if element in a_freq:
            if element not in b_freq:
                b_freq[element] = 1
            else:
                b_freq[element] += 1
    result = []
    for k in b_freq.keys():
        freq = min(a_freq[k], b_freq[k])
        for _ in range(freq):
            result.append(k)
    return sorted(result)


def test_intersection_with_dupes_sample():
    """Sample test cases (visible in HackerRank)"""

    # Sample Case 1: Different counts per element
    result = intersection_with_dupes([4, 2, 1, 6], [3, 6, 9, 2, 10])
    expected = [2, 6]
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"

    # Sample Case 2: Multiple occurrences
    result = intersection_with_dupes([1, 2, 2, 1], [2, 2, 3, 1])
    expected = [1, 2, 2]
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"

    # Sample Case 3: No intersection
    result = intersection_with_dupes([1, 2], [3, 4])
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

    print("Sample tests passed!")


# Run sample tests
test_intersection_with_dupes_sample()

"""
=== EXERCISE #19 SUMMARY - INTERSECTION WITH DUPES (SPACED REPETITION) ===

Pattern Mastery: 🟡 ALGORITHM CORRECT, SYNTAX NEEDS REFINEMENT
- Correct frequency intersection logic: Counter + manual counting + min() approach
- Proper handling of count preservation requirement  
- Early return optimization for empty lists
- Algorithm works but acknowledged "not the prettiest" implementation
- Shows understanding of frequency-based intersection concepts

Interview Readiness: 🟡 NEEDS COMPLEXITY ANALYSIS MASTERY
- Solution correctness: All hidden tests passed
- Time performance: ~18 minutes (met target)
- Major gap: Missed sorting cost dominance in time complexity analysis
- Space complexity reasoning solid but needs precision on result bounds
- Professional clarifying questions about edge cases

Spaced Repetition Performance: ⚠️ CRITICAL GAPS IDENTIFIED
- **DAILY PRACTICE REQUIRED**: Time complexity analysis precision
- **DAILY PRACTICE REQUIRED**: Understanding sorting cost impact O(k log k)
- Algorithmic thinking strong, complexity analysis needs drilling
- Pattern recognition good (frequency counting + intersection)

**PRIORITY DAILY PRACTICE SCHEDULE**:
- **Every day until automatic**: Time complexity with sorting costs
- **Every day until automatic**: Space complexity bounds and edge cases
- Sept 2: 1st review (+1 day)
- Sept 4: 2nd review (+2 days) 
- Continue daily until complexity analysis is effortless

Time Complexity: O(n + m + k log k) [MISSED: sorting dominance]
Space Complexity: O(n + u + r) where r = result size [REFINEMENT NEEDED]
Pattern Type: Frequency intersection with count preservation
Core Skills: Counter usage, frequency counting, min() for intersections

Key Strengths Demonstrated:
- Correct algorithmic approach for frequency preservation
- Professional edge case clarification questions
- Early return optimization for empty inputs
- All test cases passed with working solution

**CRITICAL AREAS FOR DAILY DRILLING**:
- Sorting cost analysis: O(k log k) vs O(n + m) dominance
- Result size bounds: r ≤ min(n,m) precision
- Time complexity composition and which terms dominate
- Space complexity component analysis

Status: ⚠️ NEEDS INTENSIVE DAILY PRACTICE - Complexity analysis gaps must be resolved
Note: Algorithm mastery present, complexity analysis precision requires daily focus
"""
