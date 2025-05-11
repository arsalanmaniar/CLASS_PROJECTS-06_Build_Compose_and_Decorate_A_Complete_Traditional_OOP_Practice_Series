class Book:
    total_books = 0  # Class variable to track total number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increase count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Total books:", Book.total_books)  # Output: Total books: 2
