"""
Learn Python's naming conventions for private attributes.

Requirements:
- Create a `BankAccount` class with:
  - Constructor takes: `account_number`, `balance`, `pin`
  - Public attribute: `account_number` (store as-is)
  - Protected attribute: `_balance` (store the balance parameter)
  - Private attribute: `__pin` (store the pin parameter)
  - Method `show_info()` that prints all three attributes from inside the class

Test Scenario:
account = BankAccount("12345", 1000, 1234)

# Test accessing from inside the class
print(account.show_info())            # Expected: Shows account_number=12345, _balance=1000, __pin=1234

# Test accessing from outside the class
print(account.account_number)         # Expected: 12345
print(account._balance)               # Expected: 1000 (works but not recommended)
# print(account.__pin)                # Expected: AttributeError

# Test what Python does to private attributes
print(dir(account))                   # Expected: See name mangling for __pin (becomes _BankAccount__pin)
"""

class BankAccount:
    def __init__ (self, account_number, balance, pin):
        self.account_number = account_number
        self._balance = balance
        self.__pin = pin

    def show_info(self):
        return f"account_number={self.account_number},  _balance={self._balance}, __pin={self.__pin}"

# Test Scenario:
account = BankAccount("12345", 1000, 1234)

# Test accessing from inside the class
print(account.show_info())            # Expected: Shows account_number=12345, _balance=1000, __pin=1234

# Test accessing from outside the class
print(account.account_number)         # Expected: 12345
print(account._balance)               # Expected: 1000 (works but not recommended)


# Test the AttributeError without crashing
try:
    print(account.__pin)               # This will raise AttributeError
except AttributeError as e:
    print(f"Error accessing __pin: {e}")


# Test what Python does to private attributes
print(dir(account))                   # Expected: See name mangling for __pin (becomes _BankAccount__pin)