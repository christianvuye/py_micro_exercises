"""
Explore how name mangling behaves in different contexts and edge cases.

Requirements:
- Create a `Parent` class with:
  - __init__ takes: `name`
  - Instance attributes created in __init__:
    - Private: `__secret`, `__data` (assign any values you want)
    - Protected: `_info` (assign any value you want)
    - Public: `name` (store the name parameter)
  - Method `show_parent_internals()` that prints all three private/protected attributes

- Create a `Child` class that inherits from `Parent`:
  - __init__ takes: `name`, `child_data`
  - Call parent constructor
  - Add its own private instance attribute: `__secret` (same name as parent!)
  - Add method `show_child_internals()` that tries to access both parent and child __secret

Test Scenario:
# Test basic name mangling
parent = Parent("Dad")
parent.show_parent_internals()

# Test inheritance name mangling
child = Child("Kid", "child_info") 
child.show_parent_internals()  # Expected: Works fine
child.show_child_internals()   # Expected: Shows both secrets don't conflict

# Test external access patterns
print("\nTesting external access:")
print(f"Parent public: {parent.name}")
print(f"Parent protected: {parent._info}")

# Test what dir() shows for both classes
print("\nParent attributes:", [attr for attr in dir(parent) if 'secret' in attr or 'data' in attr])
print("Child attributes:", [attr for attr in dir(child) if 'secret' in attr or 'data' in attr])
"""

class Parent:
    def __init__(self, name):
        self.name = name
        self.__secret = "Parent secret attribute"
        self.__data = "Parent data attribute"
        self._info = "Parent protected attribute"
    
    def show_parent_internals(self):
        print(f"{self.name}, {self.__secret}, {self.__data}, {self._info}")
    
class Child(Parent):
    def __init__(self, name, child_data):
        Parent.__init__(self, name)
        self.child_data = child_data
        self.__secret = "Child secret attribute"
    
    def show_child_internals(self):
        print(f"Child info: {self.name}, {self.child_data}, {self._info}")
        print(f"Child's __secret: {self.__secret}")  # This is _Child__secret
        
        # Try to access parent's __secret using the mangled name
        try:
            parent_secret = self._Parent__secret  # This is _Parent__secret # type: ignore
            print(f"Parent's __secret (via mangled name): {parent_secret}")
        except AttributeError as e:
            print(f"Cannot access parent's __secret: {e}")
    
# Test Scenario:
# Test basic name mangling
parent = Parent("Dad")
parent.show_parent_internals()

# Test inheritance name mangling
child = Child("Kid", "child_info") 
child.show_parent_internals()  # Expected: Works fine
child.show_child_internals()   # Expected: Shows both secrets don't conflict

# Test external access patterns
print("\nTesting external access:")
print(f"Parent public: {parent.name}")
print(f"Parent protected: {parent._info}")

# Test what dir() shows for both classes
print("\nParent attributes:", [attr for attr in dir(parent) if 'secret' in attr or 'data' in attr])
print("Child attributes:", [attr for attr in dir(child) if 'secret' in attr or 'data' in attr])