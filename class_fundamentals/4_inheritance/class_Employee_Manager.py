"""
Learn complex constructor chaining where child validation depends on parent data.

Requirements:
- Create a `Employee` class with:
  - Required: `name`, `employee_id`
  - Optional: `salary` (default: 50000), `start_date` (default: "2024-01-01"), `department` (default: "General")
  - Validate: salary >= 30000, employee_id must be 6 digits
  - Method `get_details()` showing employee info

- Create a `Manager` class that inherits from `Employee`:
  - EXTEND parent constructor
  - Add optional: `team_size` (default: 5), `bonus_percentage` (default: 0.1)
  - Force department to be "Management"
  - Validate: salary >= 80000, team_size > 0, bonus_percentage between 0-0.5
  - Add method `calculate_total_compensation()`
  - OVERRIDE get_details() to include management info

Test Scenario:
basic_employee = Employee("John Doe", 123456)
senior_employee = Employee("Jane Smith", 654321, salary=75000, start_date="2023-06-15", department="Marketing")
basic_manager = Manager("Bob Wilson", 111111, salary=90000)
senior_manager = Manager("Alice Brown", 222222, salary=120000, team_size=12, bonus_percentage=0.25)

print(basic_employee.get_details())
print(senior_employee.get_details())
print(basic_manager.get_details())
print(senior_manager.get_details())
print(f"Total comp: ${senior_manager.calculate_total_compensation():.2f}")
"""


class Employee:
    def __init__(
        self,
        name,
        employee_id,
        salary=50000,
        start_date="2024-01-01",
        department="General",
    ):
        self.name = name
        self.employee_id = self._validate_employee_id(employee_id)
        self.department = department
        self.salary = self._validate_salary(salary)
        self.start_date = start_date

    @staticmethod
    def _validate_salary(salary):
        minimum_salary = 30000
        if not salary >= minimum_salary:
            raise ValueError(f"Salary must be {minimum_salary} or more!")
        else:
            return salary

    @staticmethod
    def _validate_employee_id(employee_id):
        if not isinstance(
            employee_id, int
        ):  # because of conversion to str for len(), input could be 6 word str and pass validation
            raise TypeError(f"{employee_id} is not an integer!")
        if len(str(employee_id)) != 6:
            raise ValueError(f"{employee_id} must be 6 numbers")
        return employee_id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Salary: ${self.salary}, Start Date: {self.start_date}"


class Manager(Employee):
    def __init__(
        self,
        name,
        employee_id,
        salary=80000,
        start_date="2024-01-01",
        team_size=5,
        bonus_percentage=0.1,
    ):  # raised default salary to minimum value
        salary = Manager._validate_manager_salary(salary)
        Employee.__init__(
            self, name, employee_id, salary, start_date, department="Management"
        )
        self.team_size = self._validate_team_size(team_size)
        self.bonus_percentage = self._validate_bonus_percentage(bonus_percentage)

    @staticmethod
    def _validate_manager_salary(salary):
        minimum_manager_salary = 80000  # fucking hell mate 50k more for being a fucking managers whats up with that
        if not salary >= minimum_manager_salary:
            raise ValueError(f"Salary must be {minimum_manager_salary} or more!")
        else:
            return salary

    @staticmethod
    def _validate_team_size(team_size):
        # a team is technically minimum 2 people, or manager + employee, so min_team_size >= 1
        if not team_size > 0:
            raise ValueError("Team size should be above 0")
        else:
            return team_size

    @staticmethod
    def _validate_bonus_percentage(bonus_percentage):
        if not (0 <= bonus_percentage <= 0.5):
            raise ValueError(f"{bonus_percentage} should be between 0 and 0.5")
        else:
            return bonus_percentage

    def calculate_total_compensation(self):
        return self.salary * (1 + self.bonus_percentage)

    def get_details(self):
        return (
            f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, "
            f"Salary: ${self.salary}, Start Date: {self.start_date}, "
            f"Team Size: {self.team_size}, Bonus Percentage: {self.bonus_percentage}"
        )


# Test Scenario:
basic_employee = Employee("John Doe", 123456)
senior_employee = Employee(
    "Jane Smith", 654321, salary=75000, start_date="2023-06-15", department="Marketing"
)
basic_manager = Manager("Bob Wilson", 111111, salary=90000)
senior_manager = Manager(
    "Alice Brown", 222222, salary=120000, team_size=12, bonus_percentage=0.25
)

print(basic_employee.get_details())
print(senior_employee.get_details())
print(basic_manager.get_details())
print(senior_manager.get_details())
print(f"Total comp: ${senior_manager.calculate_total_compensation():.2f}")
