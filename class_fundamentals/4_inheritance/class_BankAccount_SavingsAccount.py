"""
Learn to handle optional parameters and different validation strategies.

Requirements:
- Create a `BankAccount` class with:
  - Required: `account_number`, `initial_balance`
  - Optional: `account_type` (default: "checking"), `overdraft_limit` (default: 0)
  - Validate: initial_balance >= 0, overdraft_limit >= 0
  - Method `get_info()` showing account details

- Create a `SavingsAccount` class that inherits from `BankAccount`:
  - EXTEND parent constructor
  - Add optional: `interest_rate` (default: 0.01)
  - Force account_type to always be "savings"
  - Validate: interest_rate must be between 0 and 0.1
  - OVERRIDE get_info() to include interest_rate in the output

Test Scenario:
# Test different ways to create accounts
basic = BankAccount("12345", 1000)
checking = BankAccount("23456", 500, "checking", 100)
savings = SavingsAccount("34567", 2000, overdraft_limit=0, interest_rate=0.025)

print(basic.get_info())     # Expected: basic account info
print(checking.get_info())  # Expected: checking with overdraft
print(savings.get_info())   # Expected: savings with interest rate
"""

class BankAccount:
    def __init__(self, account_number, initial_balance, account_type="checking", overdraft_limit=0):
        self.account_number = account_number
        self.initial_balance = self._validate_initial_balance(initial_balance)
        self.account_type = account_type
        self.overdraft_limit = self._validate_overdraft_limit(overdraft_limit)
    
    @staticmethod
    def _validate_initial_balance(initial_balance):
        if not initial_balance >= 0:
            raise ValueError(f"{initial_balance} is below 0!")
        else: 
            return initial_balance
    
    @staticmethod
    def _validate_overdraft_limit(overdraft_limit):
        if not overdraft_limit >= 0:
            raise ValueError(f"{overdraft_limit} is below 0!")
        else: 
            return overdraft_limit
    
    def get_info(self):
        return f"{self.account_number} {self.initial_balance} {self.account_type} {self.overdraft_limit}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance, overdraft_limit=0, interest_rate=0.01):
        BankAccount.__init__(self, account_number, initial_balance, "savings", overdraft_limit)
        self.interest_rate = self._validate_interest_rate(interest_rate)
    
    @staticmethod
    def _validate_interest_rate(interest_rate):
        if not (0 <= interest_rate <= 0.1):
            raise ValueError(f"{interest_rate} is not between 0 and 0.1!")
        else:
            return interest_rate
    
    def get_info(self):
        return f"{self.account_number} {self.initial_balance} {self.account_type} {self.overdraft_limit} {self.interest_rate}"

# Test different ways to create accounts
basic = BankAccount("12345", 1000)
checking = BankAccount("23456", 500, "checking", 100)
savings = SavingsAccount("34567", 2000, overdraft_limit=0, interest_rate=0.025)

print(basic.get_info())     # Expected: basic account info
print(checking.get_info())  # Expected: checking with overdraft
print(savings.get_info())   # Expected: savings with interest rate