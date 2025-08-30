"""
Purchase Pattern Analyzer - Multi-Category Analysis

You need to analyze e-commerce purchase data to find users who bought items from multiple categories.
This helps identify diverse customers for targeted marketing.

You'll get a list of purchase records, where each record contains a user ID and a product category.
Find all users who purchased from more than one category.

The purchase data could be quite large - handle millions of transactions efficiently.
"""


def purchase_pattern_analyzer(purchase_records: list[tuple]) -> list[str]:
    """
    Analyzes purchase records to identify users who have purchased more than one unique item.

    Args:
        purchase_records (list[tuple]): A list of tuples, where each tuple contains a user ID and an item ID.

    Returns:
        list[str]: A list of user IDs who have purchased more than one unique item.
    """
    grouped_by_user_id = {}
    for record in purchase_records:
        if record[0] not in grouped_by_user_id:
            grouped_by_user_id[record[0]] = set()
        grouped_by_user_id[record[0]].add(record[1])
    return [k for k, v in grouped_by_user_id.items() if len(v) > 1]


# Sample test cases (HackerRank format)
def test_purchase_pattern_analyzer():
    # Sample Case 1: Basic multi-category users
    purchases1 = [
        ("user1", "electronics"),
        ("user2", "books"),
        ("user1", "clothing"),
        ("user3", "electronics"),
        ("user2", "electronics"),
    ]
    result1 = purchase_pattern_analyzer(purchases1)
    expected1 = ["user1", "user2"]
    assert set(result1) == set(expected1), f"Expected {expected1}, got {result1}"

    # Sample Case 2: No diverse customers
    purchases2 = [("user1", "books"), ("user2", "books"), ("user3", "electronics")]
    result2 = purchase_pattern_analyzer(purchases2)
    expected2 = []
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    # Sample Case 3: All users are diverse
    purchases3 = [
        ("user1", "electronics"),
        ("user1", "books"),
        ("user2", "clothing"),
        ("user2", "sports"),
    ]
    result3 = purchase_pattern_analyzer(purchases3)
    expected3 = ["user1", "user2"]
    assert set(result3) == set(expected3), f"Expected {expected3}, got {result3}"

    print("Sample tests passed!")


# Run sample tests after implementation
test_purchase_pattern_analyzer()

"""
=== EXERCISE #28 SUMMARY - PURCHASE PATTERN ANALYZER (SPACED REPETITION) ===

Pattern Mastery: 🟢 CLEAN EXECUTION
- Dictionary + set aggregation pattern implemented correctly
- Proper grouping logic: user_id as key, categories as set values
- Correct filtering: len(categories) > 1 for multi-category users

Interview Readiness: 🟢 ADVANCED COMPLEXITY REASONING
- Sophisticated space complexity analysis considering data distribution
- Understanding of typical vs worst-case scenarios in real e-commerce data
- Professional requirements clarification about data quality and edge cases
- Recognition of O(n) as optimal for group-and-count problems

Spaced Repetition Performance: 📈 STRONG TECHNICAL PRECISION
- No syntax struggles with dictionary initialization or set operations
- Clean manual dictionary approach showing fundamental understanding
- Efficient use of sets for automatic deduplication per user

Next Review Schedule:
- Sept 2: 1st review (+2 days)
- Sept 5: 2nd review (+3 days)
- Sept 9: 3rd review (+4 days)
- Interview Sept 10: Pattern should be automatic

Time Complexity: O(n) - must process every record, optimal for grouping problems
Space Complexity: O(u × avg_categories) typically, O(n) worst case
Pattern Type: Group-by aggregation with set deduplication per group
Core Skills: Dictionary grouping, set operations, data distribution analysis

Key Strengths Demonstrated:
- Advanced understanding of how data characteristics affect space complexity
- Clean implementation of grouping pattern without helper libraries
- Professional edge case consideration and data quality assumptions
- Sophisticated reasoning about typical vs worst-case algorithmic behavior

Status: 🔄 NEEDS SPACED REPETITION - Follow review schedule
Note: Shows advanced grasp of real-world algorithmic performance considerations
"""
