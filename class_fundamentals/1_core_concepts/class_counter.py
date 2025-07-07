# Your task: Define the Counter class with increment method
# Test it with: 
# counter = Counter()
# counter.increment()
# print(counter.count)  # Should print 1

class Counter:
    def __init__(self, count = 0):
        self.count = count
    
    def increment(self):
        self.count += 1

counter = Counter()
counter.increment()
print(counter.count)
