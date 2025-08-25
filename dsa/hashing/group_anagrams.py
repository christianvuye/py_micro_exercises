"""
Group Anagrams

Write a function `group_anagrams` that takes in a list of strings.
The function should return a list of lists, where each inner list contains
strings that are anagrams of each other.

Example:
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
→ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

group_anagrams(["abc", "bca", "cab", "xyz"])
→ [["abc", "bca", "cab"], ["xyz"]]

group_anagrams([]) → []

Test Cases (copy-paste below your function):

import time

def test_group_anagrams():
    # Test case 1: Basic functionality
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists for comparison since order within groups doesn't matter
    result1_sorted = [sorted(group) for group in result1]
    result1_sorted.sort()
    expected1 = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected1.sort()
    print(f"Test 1 - Basic: {result1_sorted == expected1}")

    # Test case 2: Different groups
    result2 = group_anagrams(["abc", "bca", "cab", "xyz"])
    result2_sorted = [sorted(group) for group in result2]
    result2_sorted.sort()
    expected2 = [["abc", "bca", "cab"], ["xyz"]]
    expected2.sort()
    print(f"Test 2 - Different groups: {result2_sorted == expected2}")

    # Test case 3: Empty list
    result3 = group_anagrams([])
    expected3 = []
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: No anagrams
    result4 = group_anagrams(["cat", "dog", "bird"])
    result4_sorted = [sorted(group) for group in result4]
    result4_sorted.sort()
    expected4 = [["bird"], ["cat"], ["dog"]]
    expected4.sort()
    print(f"Test 4 - No anagrams: {result4_sorted == expected4}")

    # Test case 5: All anagrams
    result5 = group_anagrams(["abc", "bac", "cab"])
    result5_sorted = [sorted(group) for group in result5]
    expected5 = [["abc", "bac", "cab"]]
    print(f"Test 5 - All anagrams: {result5_sorted == expected5}")

    # Performance comparison test
    # Generate anagram groups: ["abc", "bac", "cab", "def", "fed", "efd", ...]
    large_list = []
    for i in range(1000):
        base = f"word{i:03d}"
        anagram1 = ''.join(sorted(base))  # Sorted version
        anagram2 = base[::-1]  # Reversed version
        anagram3 = base[1:] + base[0]  # Rotated version
        large_list.extend([anagram1, anagram2, anagram3])
    # Total: 3000 strings forming 1000 anagram groups

    # Time your solution
    start_time = time.time()
    for _ in range(10):
        result = group_anagrams(large_list)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (3,000 strings, 10 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Number of anagram groups: {len(group_anagrams(large_list))}")

    # Reference: naive O(n² * m) approach where m = average string length
    def naive_group_anagrams(strs):
        def are_anagrams(s1, s2):
            return sorted(s1) == sorted(s2)  # O(m log m) per comparison

        groups = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and are_anagrams(strs[i], strs[j]):
                    group.append(strs[j])
                    used[j] = True

            groups.append(group)

        return groups

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_group_anagrams(large_list[:300])  # Smaller subset
    naive_time = time.time() - start_time

    print(f"Naive O(n² * m log m) time (300 strings, 10 iterations): {naive_time:.4f} seconds")
    print(f"Estimated speedup: ~{(naive_time * 3000/300) / optimized_time:.1f}x faster")

# Run tests after implementing your function
# test_group_anagrams()
"""

import time
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups a list of strings into lists of anagrams.

    Args:
        strs (list[str]): A list of strings to be grouped.

    Returns:
        list[list[str]]: A list of lists, where each sublist contains strings that are anagrams of each other.

    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    strs_by_alpha = defaultdict(list)
    for str_i in strs:
        alpha_sorted_str = "".join(sorted(str_i))
        strs_by_alpha[alpha_sorted_str].append(str_i)
    return list(strs_by_alpha.values())


def test_group_anagrams():
    # Test case 1: Basic functionality
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists for comparison since order within groups doesn't matter
    result1_sorted = [sorted(group) for group in result1]
    result1_sorted.sort()
    expected1 = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected1.sort()
    print(f"Test 1 - Basic: {result1_sorted == expected1}")

    # Test case 2: Different groups
    result2 = group_anagrams(["abc", "bca", "cab", "xyz"])
    result2_sorted = [sorted(group) for group in result2]
    result2_sorted.sort()
    expected2 = [["abc", "bca", "cab"], ["xyz"]]
    expected2.sort()
    print(f"Test 2 - Different groups: {result2_sorted == expected2}")

    # Test case 3: Empty list
    result3 = group_anagrams([])
    expected3 = []
    print(f"Test 3 - Empty: {result3 == expected3}")

    # Test case 4: No anagrams
    result4 = group_anagrams(["cat", "dog", "bird"])
    result4_sorted = [sorted(group) for group in result4]
    result4_sorted.sort()
    expected4 = [["bird"], ["cat"], ["dog"]]
    expected4.sort()
    print(f"Test 4 - No anagrams: {result4_sorted == expected4}")

    # Test case 5: All anagrams
    result5 = group_anagrams(["abc", "bac", "cab"])
    result5_sorted = [sorted(group) for group in result5]
    expected5 = [["abc", "bac", "cab"]]
    print(f"Test 5 - All anagrams: {result5_sorted == expected5}")

    # Performance comparison test
    # Generate anagram groups: ["abc", "bac", "cab", "def", "fed", "efd", ...]
    large_list = []
    for i in range(1000):
        base = f"word{i:03d}"
        anagram1 = "".join(sorted(base))  # Sorted version
        anagram2 = base[::-1]  # Reversed version
        anagram3 = base[1:] + base[0]  # Rotated version
        large_list.extend([anagram1, anagram2, anagram3])
    # Total: 3000 strings forming 1000 anagram groups

    # Time your solution
    start_time = time.time()
    for _ in range(10):
        result = group_anagrams(large_list)
    optimized_time = time.time() - start_time

    print("\nPerformance Test (3,000 strings, 10 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")
    print(f"Number of anagram groups: {len(group_anagrams(large_list))}")

    # Reference: naive O(n² * m) approach where m = average string length
    def naive_group_anagrams(strs):
        def are_anagrams(s1, s2):
            return sorted(s1) == sorted(s2)  # O(m log m) per comparison

        groups = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and are_anagrams(strs[i], strs[j]):
                    group.append(strs[j])
                    used[j] = True

            groups.append(group)

        return groups

    start_time = time.time()
    for _ in range(10):
        naive_result = naive_group_anagrams(large_list[:300])  # Smaller subset
    naive_time = time.time() - start_time

    print(
        f"Naive O(n² * m log m) time (300 strings, 10 iterations): {naive_time:.4f} seconds"
    )
    print(
        f"Estimated speedup: ~{(naive_time * 3000 / 300) / optimized_time:.1f}x faster"
    )


# Run tests after implementing your function
test_group_anagrams()

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Exercise: Group Anagrams
Pattern: Hash-based grouping with string normalization signature

Developer's Solution Approach:
- Used sorted string as signature: "".join(sorted(str_i))
- Applied defaultdict(list) for automatic group creation
- Single-pass grouping with O(1) hash lookups
- Clean transformation pipeline: sort → join → group → return

Complexity Analysis Process:
Developer initially confused variable names (n vs s) but self-corrected well.
- Time: O(n × s log s) where n = strings, s = avg string length
- Space: O(n × s) broken down as (n×s) + (n×s) + n
- Demonstrated strong understanding of space vs time trade-offs

Technical Learning Moments:
- Learned O(s log s) represents divide-and-conquer sorting complexity
- Understood "log s" as number of binary splits needed
- Correctly identified that space complexity tracks total content, not container count
- Self-corrected variable confusion and applied proper mathematical breakdown

Key Insights Gained:
- Pattern recognition: "anagram signature" → consistent hash key for grouping
- Algorithm elegance: sorting provides natural normalization
- Complexity composition: understood how individual operations combine into total complexity

Communication & Process:
- Caught instructor error (imports in docstring giving hints away)
- Asked clarifying questions about anagram definition before implementing
- Showed mathematical rigor in complexity analysis
- Demonstrated learning autonomy throughout

Next Focus: Continue Tier 2 with more advanced hash-based grouping patterns
"""
