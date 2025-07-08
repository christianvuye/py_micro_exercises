"""
Practice inheritance with a banking system.

Requirements:
- Create an `Account` class with:
  - Attributes: `account_number`, `balance` (set in __init__)
  - Method `get_balance()` that returns the current balance
  - Method `can_withdraw(amount)` that returns True if amount <= balance

- Create a `SavingsAccount` class that inherits from `Account`:
  - Additional attribute: `interest_rate` (set in __init__)
  - Inherit all Account methods WITHOUT modifying them
  - Add method `calculate_interest()` that returns balance * interest_rate

Test Scenario:
account = Account("12345", 1000)
savings = SavingsAccount("67890", 2000, 0.03)

print("=== Account ===")
print(f"Balance: ${account.get_balance()}")                    # Expected: 1000
print(f"Can withdraw $500: {account.can_withdraw(500)}")       # Expected: True

print("\n=== Savings Account ===")
print(f"Balance: ${savings.get_balance()}")                    # Expected: 2000
print(f"Can withdraw $2500: {savings.can_withdraw(2500)}")     # Expected: False
print(f"Interest earned: ${savings.calculate_interest()}")     # Expected: 60.0
"""

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def can_withdraw(self, amount):
        return amount <= self.balance
    
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        Account.__init__(self, account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        return self.balance * self.interest_rate


account = Account("12345", 1000)
savings = SavingsAccount("67890", 2000, 0.03)

print("=== Account ===")
print(f"Balance: ${account.get_balance()}")                    # Expected: 1000
print(f"Can withdraw $500: {account.can_withdraw(500)}")       # Expected: True

print("\n=== Savings Account ===")
print(f"Balance: ${savings.get_balance()}")                    # Expected: 2000
print(f"Can withdraw $2500: {savings.can_withdraw(2500)}")     # Expected: False
print(f"Interest earned: ${savings.calculate_interest()}")     # Expected: 60.0