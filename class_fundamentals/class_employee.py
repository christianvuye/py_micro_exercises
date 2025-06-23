"""
Create a class called `Employee` with class variable `company_name = "TechCorp"`. 
Add instance variables `name` and `salary`. Add a method `get_details` that returns 
a string with employee name, salary, and company.

Your task: Define Employee class with class and instance variables
Test it with:
emp = Employee("Alice", 75000)
print(emp.get_details())  # Should print "Alice works at TechCorp with salary $75000"
"""

class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.name} works at {Employee.company_name} with salary ${self.salary}"
    

emp = Employee("Alice", 75000)
print(emp.get_details())  # Should print "Alice works at TechCorp with salary $75000"