# Your task: Define the Book class
# Test it with: book = Book("1984", "George Orwell")

class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

book = Book("1984", "George Orwell")

print(book.title)
print(book.author)