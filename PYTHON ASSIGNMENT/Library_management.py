# Made by:Ayush
# Roll number:2501410018
# Course Btech Cse Cybersecurity



class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"

    def mark_issued(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book has been issued.")
        else:
            print("Book is already issued.")

    def mark_returned(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book has been returned.")
        else:
            print("Book is already available.")

    def details(self):
        return f"[{self.isbn}] {self.title} - {self.author} ({self.status})"


class Library:
    def __init__(self):
        self.collection = []

    def register_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.collection.append(book)
        print("Book registered successfully.")

    def find_title(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_isbn(self, isbn):
        for book in self.collection:
            if book.isbn == isbn:
                return book
        return None

    def show_books(self):
        if not self.collection:
            print("Library is empty.")
        else:
            for book in self.collection:
                print(book.details())


def run_library():
    lib = Library()

    while True:
        print("\n======= Library Menu =======")
        print("1. Register a Book")
        print("2. Issue a Book")
        print("3. Return a Book")
        print("4. Show All Books")
        print("5. Search a Book")
        print("6. Quit")

        option = input("Choose an option: ")

        if option == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            isbn = input("Enter ISBN: ")
            lib.register_book(title, author, isbn)

        elif option == "2":
            isbn = input("Enter ISBN to Issue: ")
            book = lib.find_isbn(isbn)
            if book:
                book.mark_issued()
            else:
                print("Book not found.")

        elif option == "3":
            isbn = input("Enter ISBN to Return: ")
            book = lib.find_isbn(isbn)
            if book:
                book.mark_returned()
            else:
                print("Book not found.")

        elif option == "4":
            lib.show_books()

        elif option == "5":
            title = input("Enter title to search: ")
            book = lib.find_title(title)
            if book:
                print(book.details())
            else:
                print("Book not found.")

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


run_library()
