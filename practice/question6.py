class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }

        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nBooks in Library:")

        for book in self.books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print()

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("\nBook Found!")
                print("Title:", book["title"])
                print()
                print("Author:", book["author"])
                return

        print("Book not found.")


library = Library()

library.add_book("Python Programming", "sahal")
library.add_book("Data Science", "shalah")
library.add_book("java script", "samil")

library.display_books()

library.search_book("data science")