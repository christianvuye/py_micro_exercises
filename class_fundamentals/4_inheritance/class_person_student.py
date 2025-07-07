"""
Create your first inheritance relationship.

Requirements:
- Create a `Person` class with:
  - Attributes: `name` and `age` (set in __init__)
  - Method `introduce()` that returns "Hi, I'm {name} and I'm {age} years old"
  - Method `can_vote()` that returns True if age >= 18, False otherwise

- Create a `Student` class that inherits from `Person`:
  - Additional attribute: `school` (set in __init__)
  - Inherit all Person methods WITHOUT modifying them
  - Add a new method `study()` that returns "{name} is studying at {school}"

Test Scenario:
person = Person("Alice", 25)
student = Student("Bob", 17, "High School")

print("=== Person ===")
print(person.introduce())
print(f"Can vote: {person.can_vote()}")

print("\n=== Student ===")
print(student.introduce())  # Should work automatically!
print(f"Can vote: {student.can_vote()}")  # Should work automatically!
print(student.study())  # New method
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def can_vote(self):
        return self.age >= 18

class Student(Person):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        self.school = school
    
    def study(self):
        return f"{self.name} is studying at {self.school}"

person = Person("Alice", 25)
student = Student("Bob", 17, "High School")

print("=== Person ===")
print(person.introduce())
print(f"Can vote: {person.can_vote()}")

print("\n=== Student ===")
print(student.introduce())  # Should work automatically!
print(f"Can vote: {student.can_vote()}")  # Should work automatically!
print(student.study())  # New method