'''Console-based library management system'''


class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def mark_as_borrowed(self):
        if self.is_available:
            self.is_available = False
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently not available.')

    def mark_as_returned(self):
        if not self.is_available:
            self.is_available = True
            print(f'You have returned "{self.title}"')
        else:
            print(f'Sorry, "{self.title}" is already returned.')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        if not title:
            print('Title can not be empty.')
            return
        self.books.append(Book(title))
        print(f'"{title}" has been added to the library.')

    def borrow_book(self):
        title = input('Enter the title of the book to borrow: ')
        if not title:
            print('Title can not be empty.')
            return
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                book.mark_as_borrowed()
        if not found:
            print(f'"{title}" not found in the library.')

    def return_book(self):
        title = input('Enter the title of the book to return: ')
        if not title:
            print('Title can not be empty.')
            return
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                book.mark_as_returned()
        if not found:
            print(f'"{title}" not found in the library.')

    def view_books(self):
        available = False
        for book in self.books:
            if book.is_available:
                available = True
                print(f'- {book.title}')
        if not available:
            print('No books available right now.')

    def run(self):
        while True:
            print(
                "\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                if self.books:
                    self.borrow_book()
                else:
                    print('The library is empty.')
            elif choice == '3':
                if self.books:
                    self.return_book()
                else:
                    print('The library is empty.')
            elif choice == '4':
                if self.books:
                    self.view_books()
                else:
                    print('The library is empty.')
            elif choice == '5':
                print('\nExiting...\n')
                break
            else:
                print('Enter valid choice (1-5).')


if __name__ == "__main__":
    library = Library()
    library.run()
