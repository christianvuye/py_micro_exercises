"""
Create a BankAccount class with method chaining and validation.

Requirements:
- Initialize with account_holder, balance (default: 0), account_type ("checking" or "savings")
- Create method deposit(amount) that adds to balance, validates amount > 0, returns self
- Create method withdraw(amount) that subtracts if sufficient funds, returns self  
- Create method apply_interest() that adds 2% if savings account, 0.5% if checking, returns self
- Create method get_account_summary() that returns formatted string with all details
- All methods should validate inputs and handle edge cases gracefully

Note: Methods should be chainable AND handle invalid operations gracefully.

Test your class:
account = BankAccount("Alice", 1000, "savings")
result = account.deposit(500).apply_interest().withdraw(100).get_account_summary()
print(result)  # Should show updated balance with interest applied

# Test edge cases
account2 = BankAccount("Bob", 50, "checking")
account2.withdraw(100).deposit(-50).apply_interest()  # Should handle gracefully
print(account2.get_account_summary())
"""

class BankAccount:    
    def __init__(self, account_holder, balance=0, account_type="checking"):
        if not account_holder.replace(" ","").isalpha():
            raise ValueError((f"Invalid account holder {account_holder}. Must be strings only - no hyphens or apostrophes allowed.")) # for simplicity and scope, otherwise regex is required (out of scope)
        
        if not isinstance(balance,  (int, float)):
            raise ValueError(f"Invalid balance: {balance}. Balance must be an an int or float")

        if not self.validate_account_type(account_type):
            raise ValueError((f"Invalid account type {account_type}. Must be 'savings' or 'checking'."))
        
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
    
    @staticmethod
    def validate_account_type(account_type):
        valid_types = ("savings", "checking")
        return account_type in valid_types
    
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0: self.balance += amount
        return self
    
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount <= self.balance: self.balance -= amount
        return self

    def apply_interest(self):
        if self.account_type == "savings": self.balance *= 1.02
        if self.account_type == "checking": self.balance *= 1.005
        return self
    
    def get_account_summary(self):
        return f"Account holder: {self.account_holder}, balance: {self.balance}, account type: {self.account_type}"


account = BankAccount("Alice", 1000, "savings")
result = account.deposit(500).apply_interest().withdraw(100).get_account_summary()
print(result)  # Should show updated balance with interest applied

# Test edge cases
account2 = BankAccount("Bob", 50, "checking")
account2.withdraw(100).deposit(-50).apply_interest()  # Should handle gracefully
print(account2.get_account_summary())