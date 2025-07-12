"""
Demonstrate private attribute protection through proper encapsulation design.

Requirements:
- Create a `ProtectedData` class with:
  - __init__ takes: `data_value`
  - Private attribute: `__data`
  - Private attribute: `__modification_count` (start at 0)
  - Method `get_data()` returns the data
  - Method `update_data(new_value)` changes __data and increments __modification_count
  - Method `get_modification_count()` returns modification count
  - Method `get_debug_info()` returns a dict with both private values (for debugging only)

Test Scenario:
data = ProtectedData("sensitive_info")

# Test normal operation
print(f"Initial data: {data.get_data()}")           # Expected: sensitive_info
data.update_data("new_info")
print(f"Updated data: {data.get_data()}")           # Expected: new_info
print(f"Modifications: {data.get_modification_count()}")  # Expected: 1

# Test encapsulation protection (external testing)
print("\n=== Testing Protection ===")

# Try to access private data directly
try:
    print(data.__data)                               # Expected: AttributeError
except AttributeError as e:
    print(f"✅ Protection works: {e}")               # Expected: 'ProtectedData' object has no attribute '__data'

# Try to modify private data externally  
data.__data = "hacked"
print(f"After 'hacking': {data.get_data()}")        # Expected: new_info (unchanged!)

# Show debug info for development purposes
print(f"Debug info: {data.get_debug_info()}")       # Expected: {'data': 'new_info', 'modification_count': 1}
"""

class ProtectedData:
    def __init__(self, data_value):
        self.__data = data_value
        self.__modification_count = 0

    def get_data(self):
        return self.__data
    
    def update_data(self, new_value):
        self.__data = new_value
        self.__modification_count += 1
    
    def get_modification_count(self):
        return self.__modification_count
    
    def get_debug_info(self):
        return {'data': self.__data, 'modification_count': self.__modification_count}

# Test Scenario:
data = ProtectedData("sensitive_info")

# Test normal operation
print(f"Initial data: {data.get_data()}")           # Expected: sensitive_info
data.update_data("new_info")
print(f"Updated data: {data.get_data()}")           # Expected: new_info
print(f"Modifications: {data.get_modification_count()}")  # Expected: 1

# Test encapsulation protection (external testing)
print("\n=== Testing Protection ===")

# Try to access private data directly
try:
    print(data.__data)                               # Expected: AttributeError
except AttributeError as e:
    print(f"✅ Protection works: {e}")               # Expected: 'ProtectedData' object has no attribute '__data'

# Try to modify private data externally  
data.__data = "hacked"
print(f"After 'hacking': {data.get_data()}")        # Expected: new_info (unchanged!)

# Show debug info for development purposes
print(f"Debug info: {data.get_debug_info()}")       # Expected: {'data': 'new_info', 'modification_count': 1}