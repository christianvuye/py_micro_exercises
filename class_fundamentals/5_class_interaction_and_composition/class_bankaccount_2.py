"""
Create a class called `BankAccount` with instance variables `account_number` and `balance`. 
Add methods `get_balance` and `transfer` that moves money to another BankAccount instance.

Your task: Define BankAccount class with transfer functionality
Test it with:
acc1 = BankAccount("123", 1000)
acc2 = BankAccount("456", 500)
acc1.transfer(acc2, 200)
print(acc1.get_balance())  # Should print 800
print(acc2.get_balance())  # Should print 700
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def get_balance(self):
        return self.balance # couldnt this be done by simply calling the instance variable? acc1.balance?
    
    def transfer(self, account_to_transfer, amount):
        self.balance -= amount
        account_to_transfer.balance += amount


acc1 = BankAccount("123", 1000)
acc2 = BankAccount("456", 500)
acc1.transfer(acc2, 200)
print(acc1.get_balance())  # Should print 800
print(acc2.get_balance())  # Should print 700