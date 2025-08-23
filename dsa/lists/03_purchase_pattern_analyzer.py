"""
Interviewer Problem Statement:
"We need to analyze e-commerce purchase data to find users who bought items
from multiple categories. This helps us identify our most diverse customers
for targeted marketing.

You'll get a list of purchase records, where each record contains a user ID
and a product category. I want you to find all users who purchased from more
than one category.

For example, if I give you:
[('user1', 'electronics'), ('user2', 'books'), ('user1', 'clothing'),
 ('user3', 'electronics'), ('user2', 'electronics')]

You should return ['user1', 'user2'] because:
- user1 bought from electronics AND clothing (2 categories)
- user2 bought from books AND electronics (2 categories)
- user3 only bought from electronics (1 category) - not included

The purchase data could be quite large - we process millions of transactions
daily, so efficiency matters."

Interviewer Requirements:
- Process purchase records to identify diverse customers
- Find users who purchased from more than one product category
- Handle large datasets efficiently (hundreds of thousands of records)
- Return list of user IDs that meet the criteria
- Consider both time and space efficiency for production use
- Handle edge cases like empty data and single purchases

Tests that the code should pass:
# Test case 1: Basic multi-category users
purchases1 = [('user1', 'electronics'), ('user2', 'books'), ('user1', 'clothing'),
              ('user3', 'electronics'), ('user2', 'electronics')]
result1 = find_diverse_customers(purchases1)  # Expected: ['user1', 'user2']

# Test case 2: No diverse customers
purchases2 = [('user1', 'books'), ('user2', 'books'), ('user3', 'electronics')]
result2 = find_diverse_customers(purchases2)  # Expected: []

# Test case 3: All users are diverse
purchases3 = [('user1', 'electronics'), ('user1', 'books'),
              ('user2', 'clothing'), ('user2', 'sports')]
result3 = find_diverse_customers(purchases3)  # Expected: ['user1', 'user2']

# Test case 4: Single user, multiple categories
purchases4 = [('user1', 'electronics'), ('user1', 'books'), ('user1', 'clothing')]
result4 = find_diverse_customers(purchases4)  # Expected: ['user1']

# Test case 5: Empty purchases
purchases5 = []
result5 = find_diverse_customers(purchases5)  # Expected: []

After implementation: Analyze time and space complexity, and discuss how this
would scale with millions of records
"""


def find_diverse_customers(purchase_records: list[tuple]) -> list[str]:
    """
    Identifies customers who have purchased items from more than one category.

    Args:
        purchase_records (list[tuple]): A list of tuples, where each tuple contains
        a customer identifier and a category identifier.

    Returns:
        list[str]: A list of customer identifiers who have purchased from multiple categories.
    """
    user_category_count = {}
    for purchase_record in purchase_records:
        if purchase_record[0] not in user_category_count:
            user_category_count[purchase_record[0]] = {purchase_record[1]}
        else:
            user_category_count[purchase_record[0]].add(purchase_record[1])
    return [k for k, v in user_category_count.items() if len(v) > 1]


# Test case 1: Basic multi-category users
purchases1 = [
    ("user1", "electronics"),
    ("user2", "books"),
    ("user1", "clothing"),
    ("user3", "electronics"),
    ("user2", "electronics"),
]
result1 = find_diverse_customers(purchases1)  # Expected: ['user1', 'user2']
print(result1)

# Test case 2: No diverse customers
purchases2 = [("user1", "books"), ("user2", "books"), ("user3", "electronics")]
result2 = find_diverse_customers(purchases2)  # Expected: []
print(result2)

# Test case 3: All users are diverse
purchases3 = [
    ("user1", "electronics"),
    ("user1", "books"),
    ("user2", "clothing"),
    ("user2", "sports"),
]
result3 = find_diverse_customers(purchases3)  # Expected: ['user1', 'user2']
print(result3)

# Test case 4: Single user, multiple categories
purchases4 = [("user1", "electronics"), ("user1", "books"), ("user1", "clothing")]
result4 = find_diverse_customers(purchases4)  # Expected: ['user1']
print(result4)

# Test case 5: Empty purchases
purchases5 = []
result5 = find_diverse_customers(purchases5)  # Expected: []
print(result5)

"""
Time Complexity, worst-case: 
    - O(n), linear time complexity dependent on len of input list
Space Complexity, worst-case: 
    - O(n), linear time complexity dependent on len of input list
    - Two new data structures are created: a dict and a list
    - Both are 'constrained' in size by the original input list
    - Dict will only have unique keys and values, so lower in space than input list
    - Returned list will be even smaller than that as it onlu returns strings from 
      the original list if a certain condition is met
"""

"""
=== INTERVIEWER COMMUNICATION SUMMARY ===

Initial Request: 
"Analyze e-commerce purchase data to find users who bought items from multiple categories. 
Handle large datasets efficiently with millions of transactions daily."

Developer Clarifications Asked:
- "Can I assume that the data provided will be clean? User and category strings will be all correctly and consistently formatted?"

Interviewer Responses:
- Confirmed clean data assumptions - no need for validation or error handling
- Focus on core algorithm rather than data cleaning

Final Technical Decisions:
- Dictionary with sets as values: {user_id: {categories}} 
- Sets provide O(1) membership and addition operations
- Linear O(n) time and space complexity
- Learned that sets handle duplicate additions gracefully (no errors)
- Algorithm scales linearly - optimal for this problem since each record must be examined

Assumptions Documented:
- Set operations (add, membership) are O(1) average case
- Cannot improve beyond O(n) since every record must be processed at least once
- For 1 million records: main bottlenecks would be memory usage and I/O, not algorithm efficiency
- Algorithm is production-ready for large-scale e-commerce data processing
"""
