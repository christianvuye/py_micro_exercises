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
        """
        With the approach that is # commented out, the book state only changes when calling the reserve_by method in the Book class!
        Here in the Member class you only update the borrowed_books and reserved_books list, not the actual state!
        Avoid doing this, because you will get inconsistent states.

        Instead, have a "Single Source of Truth for State Changes" in one class -> centralize state changes in one class instead of
        across multiple classes.

        member.reserve_book(book)  # ✅ Book added to member.reserved_books
                                   # ❌ book.status still "available" (not updated)

        member.borrow_book(book)   # ✅ Moves from reserved to borrowed in member
                                   # ❌ book.status still "available" (not updated)

        member.return_book("Python Guide")  # ✅ Removes from member.borrowed_books
                                            # ❌ book.status still "available"

        Centralize state changes in Member class, not in Book class:
        Why Centralize in Member (not Book)?
            Member is the Actor: Members take actions (reserve, borrow, return)
            Book is Passive: Books don't decide their own fate
            Business Logic: "A member reserves a book" not "A book gets reserved by someone"

        # Actor class contains the state-changing logic
        actor.perform_action(target)  # Updates both actor and target

        # Target class just delegates
        target.action_performed_by(actor)  # Calls actor.perform_action(self)
        """
        if not isinstance(book, Book):
            raise TypeError(f"{book} should be a Book object")

        if (
            book.status != "available"
        ):  # so the book is reserved or borrowed already, you dont need to check if the status is reserved or borrowed, this does it
            return False

        if (
            book not in self.reserved_books and book not in self.borrowed_books
        ):  # check again that it is not reserved or borrowed, (so it is available)
            self.reserved_books.append(
                book
            )  # but this time in the list AND for this particular member instance!
            book.status = "reserved"  # Update book status
            return True
        return False  # this return statement seems unneccesary, or is it to return false when the book somehow did end up in the borrowed or reserved books list?

    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"{book} should be a Book object")

        # if book in self.borrowed_books: return False -> do not do this, see state change management doc string above

        if (
            book in self.borrowed_books or book.status == "borrowed"
        ):  # check if this member has already borrowed the book
            return False  # or it could be in another members borrowed book list

        if (
            book in self.reserved_books and book.status == "reserved"
        ):  # book is in this members reserved list and is reserved by that same member
            self.reserved_books.remove(book)
            self.borrowed_books.append(book)
            book.status = "borrowed"
            return True

        if book.status == "reserved":
            return False  # this book is reserved by some other member so this member instance cannot borrow it

        # all other cases (it's available - it can't be anything else at this point)
        self.borrowed_books.append(book)
        book.status = "borrowed"
        return True

    def return_book(
        self, book_title
    ):  # no type checking needed here, if the book title is not present nothing will happen - could add an else
        for book in (
            self.borrowed_books
        ):  # this already checks if the book is in THIS members borrowed book list
            if book.title == book_title:  # if its not, then nothing happens
                self.borrowed_books.remove(book)
                book.status = "available"
                return True
        return False

    def cancel_reservation(self, book):  # can only check for THIS member instance
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
        # theres an argument to be had that status changes should happen in the book class as it is the book that undergoes the change
        # the book should/could control the member lists based on status

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
        allowed_status = (
            "available",
            "borrowed",
            "reserved",
        )  # tuple, so it is immutable & cannot be changed anywhere
        if status not in allowed_status:
            raise ValueError(f"Status should be one of the following: {allowed_status}")
        return status

    def reserve_by(
        self, member
    ):  # member or member name? Member object makes it easier so lets keep it this way
        if not isinstance(member, Member):
            raise TypeError(f"{member} should be a Member object")
        # if member.reserve_book(self): self.status = "reserved" # change status in the member class
        return member.reserve_book(self)  # delegate to member

        # if self not in member.borrowed_books and self not in member.reserved_books:
        #    self.status = "reserved"
        #    member.reserved_books.append(self)
        # could/should? run member.reserve_book here but then it should return something for else

    def borrow_by(self, member):
        if not isinstance(member, Member):
            raise TypeError(f"{member} should be a Member object")
        return member.borrow_book(self)  # delegate to member

        # if self not in member.borrowed_books:
        #    self.status = "borrowed"
        #    member.borrowed_books.append(self)
        # again, could/should run member.borrow_book()

    def return_by_member(self, member):
        return member.return_book(self.title)


member = Member("Alice", "M001")
book = Book("Python Guide", "978-0134853989")

member.reserve_book(book)
member.borrow_book(book)  # Should work since it's reserved
member.return_book("Python Guide")
print(f"Final book status: {book.status}")  # Should be "available"
