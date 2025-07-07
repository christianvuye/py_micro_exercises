"""
Create a BankAccount class demonstrating different method types.

Requirements:
- Class variable bank_name = "Python Bank"
- Initialize with account_number, balance (default: 0)
- Instance method deposit(amount) - adds to balance, returns new balance
- Instance method withdraw(amount) - subtracts if sufficient funds, returns success/failure
- Class method create_savings_account(account_number) - returns new instance with 100 bonus
- Static method validate_account_number(account_num) - returns True if exactly 10 digits

Test your class:
# Instance methods
acc = BankAccount("1234567890", 500)
print(acc.deposit(100))  # Should return 600

# Class method  
savings = BankAccount.create_savings_account("9876543210")
print(savings.balance)   # Should show 100

# Static method
print(BankAccount.validate_account_number("1234567890"))  # Should return True
print(BankAccount.validate_account_number("123"))        # Should return False
"""

class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Succesfully withdrew {amount}, remaining balance: {self.balance}"
        else:
            return f"Current balance: {self.balance} not sufficient to withdraw {amount}."
    
    @classmethod
    def create_savings_account(cls, account_number):
        return BankAccount(account_number, 100)
    
    @staticmethod
    def validate_account_number(account_number):
        return len(account_number) == 10 and account_number.isdigit()

acc = BankAccount("1234567890", 500)
print(acc.deposit(100))  # Should return 600

# Class method  
savings = BankAccount.create_savings_account("9876543210")
print(savings.balance)   # Should show 100

# Static method
print(BankAccount.validate_account_number("1234567890"))  # Should return True
print(BankAccount.validate_account_number("123"))        # Should return False