# type: ignore
"""
Employee Email Generation: Generate company emails from employee names (format: firstname.lastname@company.com)
"""

employee_names = [("John", "Smith"), ("Jane", "Doe"), ("Bob", "Johnson")]

employee_email = map(lambda x: x[0].lower() + "." + x[1].lower() + "@company.com", employee_names)

print(list(employee_email))