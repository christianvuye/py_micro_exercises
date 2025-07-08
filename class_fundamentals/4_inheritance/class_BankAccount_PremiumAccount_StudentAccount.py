"""
Practice choosing class attribute access patterns in a banking context.

Requirements:
- Create a `BankAccount` class with:
  - Class attributes: `interest_rate = 0.01`, `fee_schedule = {"transfer": 2, "overdraft": 35}`
  - Instance attributes: `account_number`, `balance` (set in __init__)
  - Method `annual_interest()` that calculates balance * {?} interest_rate
  - Method `calculate_fee(fee_type)` that returns fee_schedule[fee_type]

- Create a `PremiumAccount` class that inherits from `BankAccount`:
  - Class attribute: `interest_rate = 0.03` (premium gets better rates)
  - DO NOT define __init__ (inherit automatically)
  - Add method `premium_earnings()` that calculates balance * {?} interest_rate
  - Add method `standard_rate_comparison()` that returns the base bank's interest_rate

- Create a `StudentAccount` class that inherits from `BankAccount`:
  - Class attribute: `fee_schedule = {"transfer": 0, "overdraft": 10}` (reduced fees)
  - DO NOT define __init__ (inherit automatically)
  - Add method `fee_savings(fee_type)` that returns standard_fee - {?} student_fee
  - Add method `my_transfer_fee()` that returns {?} transfer fee for this account type

YOUR TASK: For each {?}, choose the appropriate access pattern:
- self.attribute
- self.__class__.attribute  
- BankAccount.attribute

Consider: Should account types use their own rates/fees or the bank's standard ones?

Test Scenario:
premium = PremiumAccount("P001", 10000)
student = StudentAccount("S002", 1000)

# Your design choices will affect these results:
print(f"Premium annual interest: ${premium.annual_interest()}")           # Premium annual interest: $300.0
print(f"Premium earnings: ${premium.premium_earnings()}")                 # Premium earnings: $300.0
print(f"Student transfer fee: ${student.my_transfer_fee()}")               # Student transfer fee: $0
print(f"Student fee savings: ${student.fee_savings('overdraft')}")        # Student fee savings: $25
"""

class BankAccount:
    interest_rate = 0.01
    fee_schedule = {"transfer": 2, "overdraft": 35}

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def annual_interest(self):
        return self.balance * self.__class__.interest_rate
        # you always want the interest rate of the specific subclass, the specific bankaccount
    
    def calculate_fee(self, fee_type):
        return self.__class__.fee_schedule[fee_type]
        # student account has reduced fees, so you always want the specific subclass attribute

class PremiumAccount(BankAccount):
    interest_rate = 0.03

    def premium_earnings(self):
        return self.balance * PremiumAccount.interest_rate
        # you always want the interest from the premium account, the method is called premium_earnings!

    def standard_rate_comparison(self): # this does not really return a comparison
        return BankAccount.interest_rate # you want to always return the base rate from a regular BankAccount
    
class StudentAccount(BankAccount):
    fee_schedule = {"transfer": 0, "overdraft": 10}

    def fee_savings(self, fee_type):
        return BankAccount.fee_schedule[fee_type] - self.__class__.fee_schedule[fee_type]
        # you always want the original BankAccount fees to compare to 
        # if this class was called fee_savings_studentaccount, I would have used StudentAccount.fee_schedule[fee_type]
        # since it is not, and this method could be potentially reused in another Bank Account subclass, I am using self.__class__
    
    def my_transfer_fee(self):
        return StudentAccount.fee_schedule["transfer"]
        # since this is a method specifically for StudentAccount, I am using Student Account here
        # if it would be extended beyond this specific sub class, I would probably use self.__class__.fee_schedule
        # because this method would be extended by inheriting from Student Account

premium = PremiumAccount("P001", 10000)
student = StudentAccount("S002", 1000)

# Your design choices will affect these results:
print(f"Premium annual interest: ${premium.annual_interest()}")           # Premium annual interest: $300.0
print(f"Premium earnings: ${premium.premium_earnings()}")                 # Premium earnings: $300.0
print(f"Student transfer fee: ${student.my_transfer_fee()}")               # Student transfer fee: $0
print(f"Student fee savings: ${student.fee_savings('overdraft')}")        # Student fee savings: $25