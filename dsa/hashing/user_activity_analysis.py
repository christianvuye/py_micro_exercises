"""
User Activity Analysis

You're building an analytics dashboard for a web application. Given raw user activity logs,
you need to analyze user behavior patterns to generate insights for the product team.

Each log entry is a tuple: (user_id, action_type, timestamp, page_url)

Your function should return insights about user engagement patterns that help identify:
- Power users who perform many actions
- Popular content that gets frequent visits
- User journey patterns

The product team needs actionable data to improve user experience.

Example log entries:
[
    ("user_123", "page_view", "2024-01-15 10:30:00", "/dashboard"),
    ("user_456", "button_click", "2024-01-15 10:31:00", "/settings"),
    ("user_123", "page_view", "2024-01-15 10:32:00", "/profile"),
    ("user_789", "form_submit", "2024-01-15 10:33:00", "/signup")
]

Test Cases (copy-paste below your function):

import time

def test_user_activity_analysis():
    # Test case 1: Mixed user activities
    logs1 = [
        ("user_123", "page_view", "2024-01-15 10:30:00", "/dashboard"),
        ("user_456", "button_click", "2024-01-15 10:31:00", "/settings"),
        ("user_123", "page_view", "2024-01-15 10:32:00", "/profile"),
        ("user_789", "form_submit", "2024-01-15 10:33:00", "/signup"),
        ("user_123", "button_click", "2024-01-15 10:34:00", "/dashboard"),
        ("user_456", "page_view", "2024-01-15 10:35:00", "/help")
    ]
    result1 = user_activity_analysis(logs1)
    print(f"Test 1 result: {result1}")

    # Test case 2: Single user, multiple actions
    logs2 = [
        ("user_100", "page_view", "2024-01-15 09:00:00", "/home"),
        ("user_100", "button_click", "2024-01-15 09:01:00", "/home"),
        ("user_100", "form_submit", "2024-01-15 09:02:00", "/contact")
    ]
    result2 = user_activity_analysis(logs2)
    print(f"Test 2 result: {result2}")

    # Test case 3: Empty logs
    logs3 = []
    result3 = user_activity_analysis(logs3)
    print(f"Test 3 result: {result3}")

    # Test case 4: Same action repeated
    logs4 = [
        ("user_200", "page_view", "2024-01-15 08:00:00", "/product"),
        ("user_200", "page_view", "2024-01-15 08:01:00", "/product"),
        ("user_300", "page_view", "2024-01-15 08:02:00", "/product")
    ]
    result4 = user_activity_analysis(logs4)
    print(f"Test 4 result: {result4}")

    # Performance test
    large_logs = []
    for i in range(10000):
        user_id = f"user_{i % 500}"  # 500 different users
        action = ["page_view", "button_click", "form_submit"][i % 3]
        timestamp = f"2024-01-15 {(i//60):02d}:{(i%60):02d}:00"
        page = ["/home", "/dashboard", "/profile", "/settings"][i % 4]
        large_logs.append((user_id, action, timestamp, page))

    start_time = time.time()
    for _ in range(50):
        result = user_activity_analysis(large_logs)
    optimized_time = time.time() - start_time

    print(f"\nPerformance Test (10,000 log entries, 50 iterations):")
    print(f"Your solution time: {optimized_time:.4f} seconds")

# test_user_activity_analysis()
"""


def user_activity_analysis(logs):
    # Your implementation here
    pass
