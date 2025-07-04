"""
Create a Book class with basic structure.

Requirements:
- Initialize with title, author, and page_count
- Store all three as instance variables
- Create a simple method that returns book info as a string

Test your class:
book = Book("1984", "George Orwell", 328)
print(book.get_info())  # Should show title, author, pages
"""

class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
    
    def get_info(self):
        return f"{self.title}, {self.author}, {self.page_count}"
    

book = Book("book title", "Christian", 325)
print(book.get_info())