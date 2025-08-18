"""
Create a Library Book Reservation system with Members and Books.

Requirements for Member class:
- Initialize with name, member_id, and empty lists for borrowed_books and reserved_books
- Create method borrow_book(book) - moves from reserved to borrowed if reserved, or borrows directly
- Create method reserve_book(book) - adds to reserved list if available
- Create method return_book(book_title) - removes from borrowed, makes book available
- Create method cancel_reservation(book_title) - removes from reserved list

Requirements for Book class:
- Initialize with title, isbn, status ("available", "borrowed", "reserved")
- Create method reserve_by(member) - changes status, updates member's reserved list
- Create method borrow_by(member) - changes status, updates member's borrowed list
- Create method return_by_member() - resets status to available, updates member

Complex Requirements:
- Prevent double-reservations and impossible state transitions
- Handle reservation → borrowing workflow seamlessly
- Maintain consistent state across all objects
- Include comprehensive error handling

Test comprehensive workflow:
member = Member("Alice", "M001")
book = Book("Python Guide", "978-0134853989")

# Test full reservation → borrowing → returning cycle
member.reserve_book(book)
member.borrow_book(book)  # Should work since it's reserved
member.return_book("Python Guide")
print(f"Final book status: {book.status}")  # Should be "available"
"""

import re

TITLE_RE = re.compile(
    r'^[A-Za-z0-9][A-Za-z0-9\s\'’“”":;,\-–—.!?&]*(?:[:\-–—]\s*[A-Za-z0-9\s\'’“”":;,\-–—.!?&]+)?$'
)
ISBN_RE = re.compile(
    r"(?i)^(?:ISBN(?:-1[03])?:?\s*)?(?:(?:97[89][-\s]?(?:\d[-\s]?){9}\d)|(?:\d[-\s]?){9}[\dX])$"
)


class Member:
    def __init__(self, name, member_id):
        if isinstance(name, str):
            self.name = name
        if isinstance(member_id, int):
            self.member_id = member_id
        self.borrowed_books = []
        self.reserved_books = []

    def reserve_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"{book} should be a Book object")

        if book.status != "available":
            return False

        if book not in self.reserved_books and book not in self.borrowed_books:
            self.reserved_books.append(book)
            book.status = "reserved"
            return True
        return False

    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"{book} should be a Book object")

        if book in self.borrowed_books or book.status == "borrowed":
            return False

        if book in self.reserved_books and book.status == "reserved":
            self.reserved_books.remove(book)
            self.borrowed_books.append(book)
            book.status = "borrowed"
            return True

        if book.status == "reserved":
            return False

        self.borrowed_books.append(book)
        book.status = "borrowed"
        return True

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                book.status = "available"
                return True
        return False

    def cancel_reservation(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"{book} should be a Book object")
        if book in self.reserved_books and book.status == "reserved":
            self.reserved_books.remove(book)
            book.status = "available"
            return True
        return False


class Book:
    def __init__(self, title, isbn, status="available"):
        self.title = self._validate_title(title)
        self.isbn = self._validate_isbn(isbn)
        self.status = self._validate_status(status)

    @staticmethod
    def _validate_title(title):
        if not bool(TITLE_RE.match(title)):
            raise ValueError(f"{title} is not the right format")
        else:
            return title

    @staticmethod
    def _validate_isbn(isbn):
        if not bool(ISBN_RE.match(isbn)):
            raise ValueError(f"{isbn} is not the right format")
        else:
            return isbn

    @staticmethod
    def _validate_status(status):
        allowed_status = ("available", "borrowed", "reserved")
        if status not in allowed_status:
            raise ValueError(f"Status should be one of the following: {allowed_status}")
        return status

    def reserve_by(self, member):
        if not isinstance(member, Member):
            raise TypeError(f"{member} should be a Member object")
        return member.reserve_book(self)

    def borrow_by(self, member):
        if not isinstance(member, Member):
            raise TypeError(f"{member} should be a Member object")
        return member.borrow_book(self)

    def return_by_member(self, member):
        return member.return_book(self.title)


member = Member("Alice", "M001")
book = Book("Python Guide", "978-0134853989")

member.reserve_book(book)
member.borrow_book(book)  # Should work since it's reserved
member.return_book("Python Guide")
print(f"Final book status: {book.status}")  # Should be "available"
