"""
Create a class called `BankAccount` that takes an initial `balance` in its `__init__` method. 
Add methods `deposit` and `withdraw` that modify the balance. The `withdraw` method should only 
subtract if there are sufficient funds.

Your task: Define the BankAccount class with deposit and withdraw methods
Test it with:
account = BankAccount(100)
account.deposit(50)
print(account.balance)  # Should print 150
account.withdraw(30)
print(account.balance)  # Should print 120
account.withdraw(200)   # Should not change balance (insufficient funds)
print(account.balance)  # Should still print 120
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit (self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.balance)  # Should print 150
account.withdraw(30)
print(account.balance)  # Should print 120
account.withdraw(200)   # Should not change balance (insufficient funds)
print(account.balance)  # Should still print 120