"""
Learn when and how to extend parent constructors vs replace them completely.

Requirements:
- Create a `Employee` class with:
  - Attributes: `name`, `salary`, `hire_date` (set in __init__)
  - Method `get_info()` that returns "{name} hired on {hire_date}, salary: ${salary}"

- Create a `Manager` class that inherits from `Employee`:
  - Additional attributes: `department`, `team_size`
  - EXTEND the parent constructor (call it, then add more setup)
  - Add method `management_info()` that returns "Manages {team_size} people in {department}"

- Create a `Contractor` class that inherits from `Employee`:
  - Additional attributes: `hourly_rate`, `contract_end_date`
  - REPLACE the parent constructor completely (different parameter structure)
  - Override `get_info()` to return "{name} contract ends {contract_end_date}, rate: ${hourly_rate}/hour"

Test Scenario:
manager = Manager("Alice", 75000, "2023-01-15", "Engineering", 8)
contractor = Contractor("Bob", 85, "2024-12-31")

print("=== Manager ===")
print(manager.get_info())           # Expected: "Alice hired on 2023-01-15, salary: $75000"
print(manager.management_info())    # Expected: "Manages 8 people in Engineering"

print("\n=== Contractor ===")
print(contractor.get_info())        # Expected: "Bob contract ends 2024-12-31, rate: $85/hour"
"""

class Employee:
    def __init__(self, name, salary, hire_date):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
    
    def get_info(self):
        return f"{self.name} hired on {self.hire_date}, salary: ${self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary, hire_date, department, team_size):
        Employee.__init__(self, name, salary, hire_date)
        self.department = department
        self.team_size = team_size
    
    def management_info(self):
        return f"Manages {self.team_size} people in {self.department}"
    
class Contractor(Employee):
    def __init__(self, name, hourly_rate, contract_end_date):
        self.name = name
        self.hourly_rate = hourly_rate
        self.contract_end_date = contract_end_date
    
    def get_info(self):
        return f"{self.name} contract ends {self.contract_end_date}, rate: ${self.hourly_rate}/hour"

# Test Scenario:
manager = Manager("Alice", 75000, "2023-01-15", "Engineering", 8)
contractor = Contractor("Bob", 85, "2024-12-31")

print("=== Manager ===")
print(manager.get_info())           # Expected: "Alice hired on 2023-01-15, salary: $75000"
print(manager.management_info())    # Expected: "Manages 8 people in Engineering"

print("\n=== Contractor ===")
print(contractor.get_info())        # Expected: "Bob contract ends 2024-12-31, rate: $85/hour"