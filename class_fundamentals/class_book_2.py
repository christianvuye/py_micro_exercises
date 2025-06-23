"""
Create a class called `Book` with instance variables `title`, `author`, and `pages`. 
Add a method `reading_time` that calculates reading time assuming 250 words per page 
and 200 words per minute reading speed.

Your task: Define Book class with reading time calculation
Test it with:
book = Book("1984", "Orwell", 300)
print(book.reading_time())  # Should print 375.0 (minutes)
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def reading_time(self):
        return (self.pages * 250) / 200

book = Book("1984", "Orwell", 300)
print(book.reading_time())  # Should print 375.0 (minutes)