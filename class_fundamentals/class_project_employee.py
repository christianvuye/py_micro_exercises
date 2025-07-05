"""
Create a project management system with Projects and Employees.

Requirements for Project class:
- Initialize with project_name, deadline, and empty list of assigned_employees
- Create method assign_employee(employee) that adds employee to project
- Create method remove_employee(employee_name) that removes employee by name
- Create method is_understaffed() that returns True if fewer than 3 employees
- Create method get_project_summary() that returns project info and team size

Requirements for Employee class:
- Initialize with name, employee_id, role, and empty list of assigned_projects
- Create method join_project(project) that adds project to employee's list
- Create method leave_project(project_name) that removes project by name
- Create method get_workload() that returns number of assigned projects
- Create method get_employee_details() that returns employee info and project names

Test your system:
proj1 = Project("Website Redesign", "2024-12-31")
proj2 = Project("Mobile App", "2024-11-15")
emp1 = Employee("Alice", "E001", "Developer")
emp2 = Employee("Bob", "E002", "Designer")

proj1.assign_employee(emp1)
emp1.join_project(proj1)
proj1.assign_employee(emp2)
emp2.join_project(proj1)
proj2.assign_employee(emp1)
emp1.join_project(proj2)

print(proj1.is_understaffed())  # Should print True (only 2 employees)
print(emp1.get_workload())      # Should print 2 (working on 2 projects)
print(emp1.get_employee_details())  # Should show both projects
"""

class Project:
    def __init__(self, project_name, deadline):
        self.project_name = project_name
        self.deadline = deadline
        self.assigned_employees = []

    def assign_employee(self, employee):
        self.assigned_employees.append(employee)
    
    def remove_employee(self, employee_name):
        for employee in self.assigned_employees:
            if employee.name == employee_name:
                self.assigned_employees.remove(employee)
                break
    
    def is_understaffed(self):
        return len(self.assigned_employees) < 3

    def get_project_summary(self):
        return f"Project name: {self.project_name}, deadline: {self.deadline}, team size: {len(self.assigned_employees)}"


class Employee:
    def __init__(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.assigned_projects = []
    
    def join_project(self, project):
        self.assigned_projects.append(project)
    
    def leave_project(self, project_name):
        for project in self.assigned_projects:
            if project.project_name == project_name:
                self.assigned_projects.remove(project)
                break
    
    def get_workload(self):
        return len(self.assigned_projects)
    
    # get_employee_details() that returns employee info and project names
    def get_employee_details(self):
        return f"Employee name: {self.name}, ID: {self.employee_id}, role: {self.role}, project(s): {[project.project_name for project in self.assigned_projects]}"
    
proj1 = Project("Website Redesign", "2024-12-31")
proj2 = Project("Mobile App", "2024-11-15")
emp1 = Employee("Alice", "E001", "Developer")
emp2 = Employee("Bob", "E002", "Designer")

proj1.assign_employee(emp1)
emp1.join_project(proj1)
proj1.assign_employee(emp2)
emp2.join_project(proj1)
proj2.assign_employee(emp1)
emp1.join_project(proj2)

print(proj1.is_understaffed())  # Should print True (only 2 employees)
print(emp1.get_workload())      # Should print 2 (working on 2 projects)
print(emp1.get_employee_details())  # Should show both projects

    


