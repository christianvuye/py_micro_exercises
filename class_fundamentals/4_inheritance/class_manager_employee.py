"""
Model a corporate hierarchy with Manager and Employee classes.

Requirements for Employee class:
- Initialize with name, employee_id, and role.
- Should have an attribute `manager` initialized to None.
- Create method `assign_manager(manager)` that sets the employee's manager.
- Create method `get_employee_details()` that returns formatted info, including the manager's name if assigned.

Requirements for Manager class:
- Initialize with name, employee_id, and an empty list of `direct_reports`.
- Create method `add_direct_report(employee)` that adds an employee to their list of reports.
- Create method `remove_direct_report(employee_name)` that removes a report by name.
- Create method `get_team_size()` that returns the number of direct reports.

Combined Requirement:
- When a manager adds a direct report, the employee's `manager` attribute should be automatically updated to that manager.

Test your system:
manager = Manager("Christian", "M001")
emp1 = Employee("Alice", "E001", "Developer")
emp2 = Employee("Bob", "E002", "Designer")

# Adding a report should automatically assign the manager to the employee
manager.add_direct_report(emp1)
manager.add_direct_report(emp2)

print(manager.get_team_size())      # Should print 2
print(emp1.get_employee_details())  # Should show "Manager: Christian"
"""


class Employee:
    def __init__(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.manager = None

    def assign_manager(self, manager):  # this could be removed
        # self.manager = manager
        # Don't allow direct assignment - force through manager
        raise ValueError(
            f"Cannot assign {manager} from the Employee, use manager.add_direct_report() instead"
        )

    def get_employee_details(self):
        manager_name = self.manager.name if self.manager else "No manager assigned"
        return f"Employee name: {self.name}, Employee_id: {self.employee_id}, Role: {self.role}, Manager: {manager_name}"


"""
Single Entry Point Pattern for Bidirectional Relationships:
- Prevents data inconsistency (one-sided relationships)
- Reduces bugs by having only one "correct" way to establish relationships
- Easier maintenance - relationship logic centralized in one method
- Clear API design - users know which method to use
- Simpler debugging - only one code path to check when issues arise
"""


class Manager:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.direct_reports = []

    def add_direct_report(self, employee):
        self.direct_reports.append(employee)
        employee.manager = self

    def remove_direct_report(self, employee_name):
        for employee in self.direct_reports:
            if employee.name == employee_name:
                self.direct_reports.remove(employee)
                employee.manager = None  # Clear the reverse relationship
                break

    def get_team_size(self):
        return len(self.direct_reports)


manager = Manager("Christian", "M001")
emp1 = Employee("Alice", "E001", "Developer")
emp2 = Employee("Bob", "E002", "Designer")

# Adding a report should automatically assign the manager to the employee
manager.add_direct_report(emp1)
manager.add_direct_report(emp2)

print(manager.get_team_size())  # Should print 2
print(emp1.get_employee_details())  # Should show "Manager: Christian"
