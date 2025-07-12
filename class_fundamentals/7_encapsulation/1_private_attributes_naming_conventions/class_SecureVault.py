"""
Learn to distinguish between creating new attributes vs accessing existing private attributes.

Requirements:
- Create a `SecureVault` class with:
  - __init__ takes: `vault_id`, `initial_contents`
  - Private attributes: `__vault_id`, `__contents`, `__access_count` (start at 0)
  - Method `access_vault()` increments __access_count and returns contents
  - Method `get_access_count()` returns the access count
  - Method `show_real_attributes()` prints all actual private attributes using dir()

Test Scenario:
vault = SecureVault("V001", "gold coins")

# Test normal operation
print(f"Contents: {vault.access_vault()}")    # Expected: gold coins
print(f"Access count: {vault.get_access_count()}")  # Expected: 1

# Test accidentally creating fake attributes
vault.__vault_id = "FAKE_ID"
vault.__contents = "fake contents"
vault.__access_count = 999

print("After creating fake attributes:")
print(f"Real contents: {vault.access_vault()}")       # Expected: Still gold coins
print(f"Real access count: {vault.get_access_count()}")  # Expected: 2
print(f"Fake vault_id: {vault.__vault_id}")           # Expected: FAKE_ID
print(f"Fake contents: {vault.__contents}")           # Expected: fake contents

vault.show_real_attributes()  # Expected: Shows both real and fake attributes
"""

class SecureVault:
    def __init__(self, vault_id, initial_contents):
        self.__vault_id = vault_id
        self.__contents = initial_contents
        self.__access_count = 0
    
    def access_vault(self):
        self.__access_count += 1
        return self.__contents

    def get_access_count(self):
        return self.__access_count
    
    def show_real_attributes(self):
        print("All attributes:", [attr for attr in dir(self) if 'vault' in attr or 'contents' in attr or 'access' in attr])

# Test Scenario:
vault = SecureVault("V001", "gold coins")

# Test normal operation
print(f"Contents: {vault.access_vault()}")    # Expected: gold coins
print(f"Access count: {vault.get_access_count()}")  # Expected: 1

# Test accidentally creating fake attributes
vault.__vault_id = "FAKE_ID"
vault.__contents = "fake contents"
vault.__access_count = 999

print("After creating fake attributes:")
print(f"Real contents: {vault.access_vault()}")       # Expected: Still gold coins
print(f"Real access count: {vault.get_access_count()}")  # Expected: 2
print(f"Fake vault_id: {vault.__vault_id}")           # Expected: FAKE_ID
print(f"Fake contents: {vault.__contents}")           # Expected: fake contents

vault.show_real_attributes()  # Expected: Shows both real and fake attributes