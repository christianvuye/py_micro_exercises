"""
You're building a user authentication system. Create a User class that stores username, 
email, and encrypted password. Add methods for password validation and user info display.

Your task: Create a User class for an authentication system
Test with:
user = User("john_doe", "john@email.com", "hashed_pass_123")
print(user.validate_password("hashed_pass_123"))  # Should print True
print(user.get_user_info())  # Should return formatted user details
"""

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def get_user_info(self):
        return f"{self.username}, {self.email}"
    
    def validate_password(self, password_to_validate):
        return password_to_validate == self.password
    
user = User("john_doe", "john@email.com", "hashed_pass_123")
print(user.validate_password("hashed_pass_123"))  # Should print True
print(user.get_user_info())  # Should return formatted user details