"""
Create a Counter class with a dangerous class variable scenario.

Requirements:
- Class variable base_count = 0 
- Instance variable my_count starts equal to base_count
- Method increment() that adds 1 to my_count
- Method reset_to_base() that sets my_count back to base_count
- Class method set_base(new_base) that changes base_count for all instances

Test scenario:
counter1 = Counter()
counter2 = Counter()

print(f"Initial - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

counter1.increment()
counter1.increment()
print(f"After counter1 increments - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

Counter.set_base(10)
print(f"After base change - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

counter2.reset_to_base()
print(f"After counter2 reset - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")
"""

class Counter:
    base_count = 0

    def __init__(self):
        self.my_count = Counter.base_count
    
    def increment(self):
        self.my_count += 1
    
    def reset_to_base(self):
        self.my_count = Counter.base_count
    
    @classmethod
    def set_base(cls, new_base):
        cls.base_count = new_base

counter1 = Counter()
counter2 = Counter()

print(f"Initial - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

counter1.increment()
counter1.increment()
print(f"After counter1 increments - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

Counter.set_base(10)
print(f"After base change - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")

counter2.reset_to_base()
print(f"After counter2 reset - Counter1: {counter1.my_count}, Counter2: {counter2.my_count}")