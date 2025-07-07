"""
Create a class called `Person` with `name` and `age` parameters. 
Add a method `introduce` that returns a string like "Hi, I'm [name] and I'm [age] years old."

Your task: Define the Person class with introduce method
Test it with:
person = Person("Alice", 30)
print(person.introduce())  # Should print "Hi, I'm Alice and I'm 30 years old."
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

person = Person("Alice", 30)
print(person.introduce())  # Should print "Hi, I'm Alice and I'm 30 years old."