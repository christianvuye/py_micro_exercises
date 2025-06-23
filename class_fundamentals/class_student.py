"""
Create a class called `Student` that stores a student's `name` and `grade`. 
Add a method called `is_passing` that returns `True` if the grade is 60 or above, `False` otherwise.

Your task: Define the Student class with is_passing method
Test it with:
student1 = Student("Alice", 75)
student2 = Student("Bob", 45)
print(student1.is_passing())  # Should print True
print(student2.is_passing())  # Should print False
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def is_passing(self):
        return self.grade
student1 = Student("Alice", 75)
student2 = Student("Bob", 45)

print(student1.is_passing())
print(student2.is_passing())