"""
Create a class called `Counter` with a class variable `total_counters` that tracks how many Counter 
instances have been created. Each instance should have its own `count` starting at 0.

Your task: Define Counter class with both class and instance variables
Test it with:
c1 = Counter()
c2 = Counter()
print(Counter.total_counters)  # Should print 2
print(c1.count)                # Should print 0
"""

class Counter:
    total_counters = 0
    
    def __init__(self, count = 0):
        self.count = count
        Counter.total_counters += 1

c1 = Counter()
c2 = Counter()
print(Counter.total_counters)  # Should print 2
print(c1.count)                # Should print 0
