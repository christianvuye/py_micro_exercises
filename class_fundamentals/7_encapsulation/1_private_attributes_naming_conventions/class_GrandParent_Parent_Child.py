"""
Understand how private attributes behave across multiple inheritance levels.

Requirements:
- Create a `GrandParent` class with:
  - __init__ takes: `family_name`
  - Private attribute: `__family_secret`
  - Method `reveal_secret()` that prints the family secret

- Create a `Parent` class that inherits from `GrandParent`:
  - __init__ takes: `family_name`, `generation`
  - Call grandparent constructor
  - Private attribute: `__parent_info`
  - Method `show_parent_data()` that prints parent info and tries to access grandparent secret

- Create a `Child` class that inherits from `Parent`:
  - __init__ takes: `family_name`, `generation`, `child_name`
  - Call parent constructor
  - Private attribute: `__child_secret`
  - Method `show_all_data()` that tries to access all three levels of private attributes

Test Scenario:
# Test three-level inheritance
child = Child("Smith", "Gen2", "Tommy")

# Test method inheritance works
child.reveal_secret()         # Expected: Works (inherited from GrandParent)
child.show_parent_data()      # Expected: Works (inherited from Parent)
child.show_all_data()         # Expected: Shows what child can/cannot access

# Test name mangling across levels
print("Child's attributes:", [attr for attr in dir(child) if attr.startswith('_') and 'secret' in attr or 'info' in attr])
"""

class GrandParent:
    def __init__(self, family_name):
        self.family_name = family_name
        self.__family_secret = "This is the family's secret"
    
    def reveal_secret(self):
        print(self.__family_secret)
    
class Parent(GrandParent):
    def __init__(self, family_name, generation):
        GrandParent.__init__(self, family_name)
        self.generation = generation
        self.__parent_info = "This is the secret parent info"
    
    def show_parent_data(self):
        print(self.__parent_info)
        # Note: This is bad practice - accessing private attribute via mangled name
        print(self._GrandParent__family_secret) # type: ignore

class Child(Parent):
    def __init__(self,family_name, generation, child_name):
        Parent.__init__(self, family_name, generation)
        self.child_name = child_name
        self.__child_secret = "This is the secret child info"
    
    def show_all_data(self):
        print(self.__child_secret)
        print(self._Parent__parent_info) # type: ignore
        print(self._GrandParent__family_secret) # type: ignore
        
# Test Scenario:
# Test three-level inheritance
child = Child("Smith", "Gen2", "Tommy")

# Test method inheritance works
child.reveal_secret()         # Expected: Works (inherited from GrandParent)
child.show_parent_data()      # Expected: Works (inherited from Parent)
child.show_all_data()         # Expected: Shows what child can/cannot access

# Test name mangling across levels
print("Child's attributes:", [attr for attr in dir(child) if attr.startswith('_') and 'secret' in attr or 'info' in attr])