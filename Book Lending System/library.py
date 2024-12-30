'''
Console-based book lending system for a small library or a personal
book collection. This app allows users to browse available books,
borrow a book, return a book, and view all borrowed books.
'''


class BookLendingSystem:
    def __init__(self):
        self.available_books = {
            1: "The Great Gatsby",
            2: "To Kill a Mockingbird",
            3: "1984",
            4: "Pride and Prejudice"
        }
        self.borrowed_books = {}

    def display_menu(self):
        print("\nWelcome to the Book Lending System!")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Borrowed books")
        print("5. Exit")

    def view_available_books(self):
        self.available_books = dict(sorted(self.available_books.items()))
        if not self.available_books:
            print("\nThere are no available books")
        else:
            print("\n--- Available Books ---")
            for i, book in self.available_books.items():
                print(f"{i}. {book}")

    def borrow_book(self):
        if not self.available_books:
            print("\nThere are no available books")
        else:
            while True:
                self.view_available_books()
                try:
                    choice = int(input("\nEnter the book number to borrow: "))
                    if choice in self.available_books.keys():
                        name = input("Enter your name: ")
                        book = self.available_books.pop(choice)
                        self.borrowed_books[choice] = (book, name)
                        print(
                            f'You have borrowed "{book}". Please return it on time.')
                        break
                    else:
                        print("\nEnter available book number")
                except ValueError:
                    print("\nEnter available book number")

    def return_book(self):
        if not self.borrowed_books:
            print("\nThere are no borrowed books")
        else:
            while True:
                self.view_borrowed_books()
                try:
                    choice = int(input("\nEnter the book number to return: "))
                    if choice in self.borrowed_books.keys():
                        book, name = self.borrowed_books.pop(choice)
                        self.available_books[choice] = book
                        print(f'Thank you, {name}, for returning "{book}".')
                        break
                    else:
                        print("\nEnter available book number")
                except ValueError:
                    print("\nEnter available book number")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("\nThere are no borrowed books")
        else:
            self.borrowed_books = dict(sorted(self.borrowed_books.items()))
            print("\n--- Borrowed Books ---")
            for i, borrow in self.borrowed_books.items():
                print(f"{i}. {borrow[0]}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoose an option: ").strip()
            if choice == "1":
                self.view_available_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                break
            else:
                print("Enter available option (1-5)")


system = BookLendingSystem()
system.run()
