import datetime

# Initialize an empty library dictionary
library = {}

# Initialize an empty dictionary to track issued books
issued_books = {}

# Initialize an empty dictionary to track student-book associations
student_books = {}

# Define admin authentication credentials
admin_username = "admin"
admin_password = "password"

# Function to add a book to the library
def add_book(title, author, ISBN, quantity):
    if ISBN in library:
        library[ISBN]["Quantity"] += quantity
    else:
        library[ISBN] = {"Title": title, "Author": author, "Quantity": quantity}

# Function to remove a book from the library
def remove_book(ISBN):
    if ISBN in library:
        if ISBN in issued_books:
            print("Cannot remove the book as it is issued to a student.")
        else:
            del library[ISBN]
            print(f"Book with ISBN {ISBN} removed from the library.")
    else:
        print(f"Book with ISBN {ISBN} not found in the library.")

# Function to search for a book by ISBN
def search_book_by_ISBN(ISBN):
    if ISBN in library:
        return library[ISBN]
    else:
        return None

# Function to count the total number of books in the library
def count_total_books():
    return sum(item["Quantity"] for item in library.values())

# Function to count available books by title
def count_available_books_by_title(title):
    count = 0
    for ISBN, book in library.items():
        if book["Title"].lower() == title.lower() and ISBN not in issued_books:
            count += book["Quantity"]
    return count

# Function to issue a book to a student
def issue_book(student_id, ISBN):
    if ISBN in library:
        if ISBN in issued_books:
            print(f"The book (ISBN {ISBN}) is already issued to another student.")
        else:
            issued_books[ISBN] = {"Student ID": student_id, "Issue Date": datetime.date.today()}
            student_books[student_id] = student_books.get(student_id, []) + [ISBN]
            print(f"Book with ISBN {ISBN} issued to student {student_id}.")
    else:
        print(f"Book with ISBN {ISBN} not found in the library.")

# Function to return a book
def return_book(student_id, ISBN):
    if ISBN in issued_books:
        if issued_books[ISBN]["Student ID"] == student_id:
            issue_date = issued_books[ISBN]["Issue Date"]
            return_date = datetime.date.today()
            days_issued = (return_date - issue_date).days

            if days_issued <= 7:
                print(f"Book with ISBN {ISBN} returned on time.")
            else:
                late_fee = (days_issued - 7) * 5  # Assuming a late fee of $5 per day
                print(f"Book with ISBN {ISBN} returned late. Late fee: ${late_fee}")
            
            del issued_books[ISBN]
            student_books[student_id].remove(ISBN)
        else:
            print(f"This book (ISBN {ISBN}) is issued to another student.")
    else:
        print(f"Book with ISBN {ISBN} is not currently issued.")

# Function to search for books issued to a student
def search_student_books(student_id):
    if student_id in student_books:
        return student_books[student_id]
    else:
        return []

# Admin authentication function
def admin_authenticate():
    admin_username_input = input("Enter admin username: ")
    admin_password_input = input("Enter admin password: ")
    return admin_username_input == admin_username and admin_password_input == admin_password

# Main menu for library management
while True:
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book by ISBN")
    print("4. Count Total Books")
    print("5. Count Available Books by Title")
    print("6. Issue a Book")
    print("7. Return a Book")
    print("8. Search Student's Issued Books")
    print("9. Update Books (Admin Only)")
    print("10. show all available books")
    print("11. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

    if choice == '1':
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        ISBN = input("Enter the ISBN of the book: ")
        try:
            quantity = int(input("Enter the quantity of the book: "))
            if title==''or author=='' or ISBN=='':
                print("Try again and enter all details")
            else:
                add_book(title, author, ISBN, quantity)
                print("Book(s) added successfully.")
        except ValueError:
            print("Try again and enter all details.")
        
        
    elif choice == '2':
        ISBN = input("Enter the ISBN of the book to remove: ")
        remove_book(ISBN)
    elif choice == '3':
        ISBN = input("Enter the ISBN of the book to search: ")
        book = search_book_by_ISBN(ISBN)
        if book:
            print("Book found:")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Quantity: {book['Quantity']}")
        else:
            print("Book not found.")
    elif choice == '4':
        total_books = count_total_books()
        print(f"Total number of books in the library: {total_books}")
    elif choice == '5':
        title = input("Enter the title of the book to count available copies: ")
        available_books = count_available_books_by_title(title)
        print(f"Total available copies of '{title}': {available_books}")
    elif choice == '6':
        student_id = input("Enter the student ID: ")
        ISBN = input("Enter the ISBN of the book to issue: ")
        issue_book(student_id, ISBN)
    elif choice == '7':
        student_id = input("Enter the student ID: ")
        ISBN = input("Enter the ISBN of the book to return: ")
        return_book(student_id, ISBN)
    elif choice == '8':
        student_id = input("Enter the student ID to search for issued books: ")
        issued_books_list = search_student_books(student_id)
        if issued_books_list:
            print(f"Books issued to student {student_id}:")
            for ISBN in issued_books_list:
                book_info = library[ISBN]
                print(f"ISBN: {ISBN}")
                print(f"Title: {book_info['Title']}")
                print(f"Author: {book_info['Author']}")
                print("--------------------")
        else:
            print(f"No books issued to student {student_id}.")
    elif choice == '9':
        if admin_authenticate():
            ISBN = input("Enter the ISBN of the book to update: ")
            quantity = int(input("Enter the new quantity: "))
            if ISBN in library:
                library[ISBN]["Quantity"] = quantity
                print(f"Book quantity updated successfully.")
            else:
                print(f"Book with ISBN {ISBN} not found in the library.")
        else:
            print("Admin authentication failed. You are not authorized to update books.")
    
    elif choice == '10':
        print("Available Books")
        print(library)
    elif choice == '11':
        print("Exiting the library management system.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5/6/7/8/9/10).")
