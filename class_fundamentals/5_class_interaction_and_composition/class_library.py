"""
Create a Library class that manages Book objects.

Requirements:
- Initialize with library_name and empty list of books
- Create method add_book(title, author) that creates and stores a book-like object
- Create method find_books_by_author(author) that returns list of matching titles
- Create method get_library_stats() that returns total books count

For this exercise, store books as dictionaries: {"title": title, "author": author}

Test your class:
library = Library("City Library")
library.add_book("1984", "Orwell")
library.add_book("Brave New World", "Huxley") 
library.add_book("Animal Farm", "Orwell")
print(library.find_books_by_author("Orwell"))  # Should print ['1984', 'Animal Farm']
print(library.get_library_stats())             # Should print 3
"""

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
    
    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
    
    def find_books_by_author(self, author):
        matching_titles = []
        for book in self.books:
            if author == book["author"]:
                matching_titles.append(book["title"])
        return matching_titles
    
    def get_library_stats(self):
        return len(self.books)

library = Library("City Library")
library.add_book("1984", "Orwell")
library.add_book("Brave New World", "Huxley") 
library.add_book("Animal Farm", "Orwell")
print(library.find_books_by_author("Orwell"))  # Should print ['1984', 'Animal Farm']
print(library.get_library_stats())             # Should print 3