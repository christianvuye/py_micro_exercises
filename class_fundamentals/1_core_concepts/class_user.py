"""
Create a class called `User` with instance variables `username` and `password`. 
Add methods `change_password` that updates the password and `check_password` 
that returns True if the provided password matches.

Your task: Define User class with password management
Test it with:
user = User("alice", "secret123")
print(user.check_password("secret123"))  # Should print True
user.change_password("newpass456")
print(user.check_password("secret123"))  # Should print False
print(user.check_password("newpass456")) # Should print True
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def change_password(self, new_password):
        self.password = new_password
    
    def check_password(self, provided_password):
        return provided_password == self.password

user = User("alice", "secret123")
print(user.check_password("secret123"))  # Should print True
user.change_password("newpass456")
print(user.check_password("secret123"))  # Should print False
print(user.check_password("newpass456")) # Should print True