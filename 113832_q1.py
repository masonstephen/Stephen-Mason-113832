class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Sorry, '{book.title}' is currently borrowed by another member.")
        elif book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"'{book.title}' has been borrowed.")
        else:
            print(f"Could not borrow '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"'{book.title}' has been returned.")
        else:
            print(f"'{book.title}' is not in your list of borrowed books.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books borrowed.")

# Initial Data
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee")
]

members = [
    LibraryMember("Alice", 1),
    LibraryMember("Bob", 2),
    LibraryMember("Charlie", 3)
]

# Functions
def find_member_by_name(name):
    for member in members:
        if member.name.lower() == name.lower():
            return member
    return None

def register_new_member(name):
    new_member_id = len(members) + 1
    new_member = LibraryMember(name, new_member_id)
    members.append(new_member)
    print(f"New member registered! Welcome, {name}. Your Member ID is {new_member_id}.")
    return new_member

def main():
    print("Welcome to the Library Management System")
    while True:
        name = input("Enter your name to access your account: ").strip()
        member = find_member_by_name(name)
        
        if member:
            print(f"\nHello, {member.name}! Accessing your account...")
        else:
            print("Member not found.")
            register_choice = input("Would you like to register as a new member? (yes/no): ").strip().lower()
            if register_choice == 'yes':
                member = register_new_member(name)
            else:
                print("Returning to the main menu...\n")
                continue
        
        while member:
            print("\nMember Menu")
            print("1. Borrow a Book")
            print("2. Return a Book")
            print("3. List Borrowed Books")
            print("4. Logout")
            
            choice = input("Choose an option (1-4): ").strip()
            
            if choice == '1':
                print("\nAvailable Books:")
                available_books = [book for book in books]
                for idx, book in enumerate(available_books, start=1):
                    status = "Available" if not book.is_borrowed else "Borrowed"
                    print(f"{idx}. {book.title} by {book.author} - {status}")
                
                book_choice = int(input("Enter the number of the book you want to borrow: ").strip())
                if 1 <= book_choice <= len(available_books):
                    selected_book = available_books[book_choice - 1]
                    member.borrow_book(selected_book)
                else:
                    print("Invalid choice.")

            elif choice == '2':
                print("\nYour Borrowed Books:")
                if member.borrowed_books:
                    for idx, book in enumerate(member.borrowed_books, start=1):
                        print(f"{idx}. {book.title} by {book.author}")
                    book_choice = int(input("Enter the number of the book you want to return: ").strip())
                    if 1 <= book_choice <= len(member.borrowed_books):
                        selected_book = member.borrowed_books[book_choice - 1]
                        member.return_book(selected_book)
                    else:
                        print("Invalid choice.")
                else:
                    print("You have no borrowed books to return.")

            elif choice == '3':
                print("\nListing Your Borrowed Books:")
                member.list_borrowed_books()

            elif choice == '4':
                print("Logging out...\n")
                break

            else:
                print("Invalid choice. Please select a valid option.")

# Run the library management system
main()
