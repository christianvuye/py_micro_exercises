"""
Counter class demonstrating private attribute behavior.

For detailed explanation of best practices, see:
private_attributes_best_practices.md

This implementation shows both correct usage (increment, get_count)
and demonstrates the pitfalls of accessing private attributes externally.
"""

"""
Understand the different behaviors when reading vs writing private attributes.

Requirements:
- Create a `Counter` class with:
  - __init__ takes: `start_value` (default: 0)
  - Create a private attribute __count and initialize it with the value passed to start_value
  - Method `get_count()` returns the current count
  - Method `increment()` increases __count by 1
  - Method `show_all_attributes()` prints all attributes using dir()

Test Scenario:
counter = Counter(5)
print(f"Initial count: {counter.get_count()}")    # Expected: 5

# Test 1: Try to READ private attribute (should fail)
try:
    print(counter.__count)
except AttributeError as e:
    print(f"Reading failed: {e}")

# Test 2: Try to WRITE private attribute (creates new attribute!)
counter.__count = 999
print(f"After writing __count = 999:")
print(f"get_count() still returns: {counter.get_count()}")  # Expected: Still 5!
print(f"counter.__count now returns: {counter.__count}")    # Expected: 999

counter.show_all_attributes()  # Expected: See both __count and _Counter__count

# Test 3: Increment should still work on the real private attribute
counter.increment()
print(f"After increment: {counter.get_count()}")           # Expected: 6
"""

class Counter:
    def __init__(self, start_value=0):
        self.__count = start_value # this gets renamed internally by Python to _Counter__count so you cannot read it using self.__count
    
    def get_count(self):
        return self.__count
    
    def increment(self):
        self.__count += 1
    
    def show_all_attributes(self):
        print(dir(self))


# Test Scenario:
counter = Counter(5)
print(f"Initial count: {counter.get_count()}")    # Expected: 5

# Test 1: Try to READ private attribute (should fail)
try:
    print(counter.__count)
except AttributeError as e:
    print(f"Reading failed: {e}")

# Test 2: Try to WRITE private attribute (creates new attribute!)

# this gets confusing though, because now you have both self.__count = 999 and self.count = 5 (which is represented as _Counter__count?)
counter.__count = 999 # 
print(f"After writing __count = 999:")
print(f"get_count() still returns: {counter.get_count()}")  # Expected: Still 5!
print(f"counter.__count now returns: {counter.__count}")    # Expected: 999

counter.show_all_attributes()  # Expected: See both __count and _Counter__count

# Test 3: Increment should still work on the real private attribute
counter.increment()
print(f"After increment: {counter.get_count()}")           # Expected: 6

"""
You Now Have TWO Different Attributes:

counter._Counter__count = 5 (the REAL private attribute, name-mangled)
counter.__count = 999 (a NEW attribute you just created)

Why This Happens:
Inside the class:
pythonself.__count = start_value  # Python applies name mangling → becomes _Counter__count
Outside the class:
pythoncounter.__count = 999  # Python does NOT apply name mangling → creates literal __count
The Key Rule:

Name mangling only happens when writing code INSIDE the class
From outside the class, Python treats __count as a literal attribute name

So you're right - it IS confusing! You have:

The "real" private counter (5 → 6 after increment)
A "fake" counter (999) that doesn't affect class behavior

This is exactly why private attributes provide protection - external code can't accidentally break the internal state!
"""