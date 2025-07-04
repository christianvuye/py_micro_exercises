"""
Create a Library system with Book tracking.

Requirements for Book class:
- Class variable total_books = 0 (tracks all books ever created)
- Initialize with title, author, is_available (default: True)
- Create method check_out() that sets is_available to False
- Create method return_book() that sets is_available to True

Requirements for Library class:
- Class variable total_libraries = 0 (tracks all libraries created)
- Initialize with name, increment total_libraries counter
- Create method add_book(book) that adds Book object to library
- Create method get_available_books() that returns list of available book titles
- Create method get_library_stats() that returns dict with library info

Test your system:
book1 = Book("1984", "Orwell")
book2 = Book("Dune", "Herbert")
lib = Library("City Library")
lib.add_book(book1)
lib.add_book(book2)
book1.check_out()
print(lib.get_available_books())  # Should show only ["Dune"]
print(Book.total_books)           # Should show 2
"""


class Book:
    total_books = 0

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available
        Book.total_books += 1

    def check_out(self):
        self.is_available = False
    
    def return_book(self):
        self.is_available = True

class Library:
    total_libraries = 0

    def __init__(self, name):
        self.name = name
        self.books = []
        Library.total_libraries += 1
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_available_books(self):
        return [book.title for book in self.books if book.is_available]
    
    def get_library_stats(self):
        available_books = self.get_available_books()
        library_stats = {"name": str(self.name), "total_books": len(self.books), "available_books": len(available_books)}
        return library_stats

book1 = Book("1984", "Orwell")
book2 = Book("Dune", "Herbert")
lib = Library("City Library")
lib.add_book(book1)
lib.add_book(book2)
book1.check_out()
print(lib.get_available_books())  # Should show only ["Dune"]
print(Book.total_books)           # Should show 2
print(lib.get_library_stats())