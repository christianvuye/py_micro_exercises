"""
Group Anagrams - Signature-Based String Grouping

Given a list of strings, group all anagrams together. Two strings are anagrams
if they contain the same characters with the same frequencies, just in different orders.

Return the groups as a list of lists. The order of groups and strings within
groups doesn't matter.

This pattern is used in text analysis, duplicate detection, and linguistic
processing systems.
"""

from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """
    Groups a list of strings into lists of anagrams.

    Each group in the returned list contains strings that are anagrams of each other.
    Anagrams are determined by sorting the characters in each string and grouping
    strings with identical sorted character sequences.

    Args:
        strings (list[str]): A list of strings to be grouped.

    Returns:
        list[list[str]]: A list of groups, where each group is a list of anagram strings.
    """
    grouped = defaultdict(list)
    for string in strings:
        temp_list = []
        for char in string:
            temp_list.append(char)
        temp_list.sort()
        anagram = "".join(temp_list)
        grouped[anagram].append(string)
    return [value for value in dict(grouped).values()]


# Sample test cases (HackerRank format)
def test_group_anagrams():
    # Sample Case 1: Basic anagram groups
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Should group: [eat,tea,ate], [tan,nat], [bat]
    result1_sorted = [sorted(group) for group in result1]
    result1_sorted.sort()
    print(f"Test 1 groups count: {len(result1)}")
    print(f"Test 1 sorted result: {result1_sorted}")

    # Sample Case 2: No anagrams
    result2 = group_anagrams(["abc", "def", "ghi"])
    print(f"Test 2 groups count: {len(result2)} (should be 3)")

    # Sample Case 3: All same anagrams
    result3 = group_anagrams(["abc", "bac", "cab"])
    print(f"Test 3 groups count: {len(result3)} (should be 1)")

    print("Sample tests completed - analyze the patterns!")


# Run sample tests after implementation
test_group_anagrams()


"""
=== EXERCISE #31 SUMMARY - GROUP ANAGRAMS (SPACED REPETITION) ===

Pattern Mastery: 🟢 SIGNATURE-BASED GROUPING MASTERY
- Clean implementation of anagram signature creation (character sorting)
- Proper use of defaultdict(list) for automatic group creation  
- Manual character extraction showing understanding of underlying operations

Interview Readiness: 🟢 STRONG ALGORITHMIC FOUNDATION
- Professional requirements clarification about edge cases and character types
- Understanding of optimization possibilities (sorted() vs manual approach)
- Good debugging through sample test analysis

Spaced Repetition Performance: 📈 SOLID TIER 4 START
- Applied signature-based pattern to new domain (string normalization)
- Clean implementation without syntax struggles
- Strong grasp of algorithm structure and data flow

Next Review Schedule:
- Sept 3: 1st review (+3 days)
- Sept 6: 2nd review (+3 days)  
- Sept 9: 3rd review (+3 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n × s log s) where n=strings, s=avg string length (sorting dominates)
Space Complexity: O(n × s) - storing all strings and signature keys
Pattern Type: Signature-based grouping with string normalization
Core Skills: String sorting, hash-based grouping, anagram detection

Key Strengths Demonstrated:
- Understanding of hashable vs non-hashable types for dictionary keys
- Proper complexity analysis process with minor correction on sorting cost
- Professional edge case handling and requirements clarification
- Recognition of optimization opportunities while maintaining clarity

Areas for Daily Practice:
- **CRITICAL**: Sorting complexity memorization - O(k log k) always
- Continue building confidence with signature-based grouping patterns

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule
Note: Strong foundation with minor complexity analysis refinement needed
"""
