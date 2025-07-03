"""
Create a BankAccount class:
- Initialize with account_holder name and starting balance
- Store both as instance variables

Add to your BankAccount class:
- deposit(amount) method that adds to balance
- get_balance() method that returns current balance
- withdraw(amount) method that:
  * Subtracts from balance if sufficient funds
  * Returns True if successful, False if insufficient funds
- get_account_info() method that returns a formatted string like:
  "Account holder: John Doe, Balance: $150.00"
"""

class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount 

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    
    def get_account_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"