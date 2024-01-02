import mysql.connector
from mysql.connector import Error
import datetime

# Function to establish a MySQL connection
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            database='library_management',
            user='root',
            password='root'
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to add a book to the library
def add_book(conn, ISBN, title, author, quantity):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        existing_book = cursor.fetchone()

        if existing_book:
            new_quantity = existing_book[3] + quantity
            cursor.execute("UPDATE books SET Quantity = %s WHERE ISBN = %s", (new_quantity, ISBN))
            print(f"Updated quantity of book with ISBN {ISBN}.")
        else:
            cursor.execute("INSERT INTO books (ISBN, Title, Author, Quantity) VALUES (%s, %s, %s, %s)",
                           (ISBN, title, author, quantity))
            print(f"Book with ISBN {ISBN} added to the library.")

        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to remove a book from the library
def remove_book(conn, ISBN):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        book = cursor.fetchone()

        if book:
            cursor.execute("SELECT * FROM book_issues WHERE ISBN = %s", (ISBN,))
            issued_book = cursor.fetchone()
            if issued_book:
                print("Cannot remove the book as it is issued to a student.")
            else:
                cursor.execute("DELETE FROM books WHERE ISBN = %s", (ISBN,))
                print(f"Book with ISBN {ISBN} removed from the library.")
            conn.commit()
        else:
            print(f"Book with ISBN {ISBN} not found in the library.")

        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to search for a book by ISBN
def search_book_by_ISBN(conn, ISBN):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        book = cursor.fetchone()

        if book:
            print("Book found:")
            print(f"ISBN: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Quantity: {book[3]}")
        else:
            print("Book not found.")

        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to count the total number of books in the library
def count_total_books(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Quantity) FROM books")
        total_books = cursor.fetchone()[0]

        if total_books:
            print(f"Total number of books in the library: {total_books}")
        else:
            print("The library is empty.")

        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to count available books by title
def count_available_books_by_title(conn, title):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Quantity) FROM books WHERE Title = %s", (title,))
        available_books = cursor.fetchone()[0]

        if available_books:
            print(f"Total available copies of '{title}': {available_books}")
        else:
            print(f"No available copies of '{title}' found in the library.")

        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to issue a book to a student
def issue_book(conn, student_id, ISBN):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        book = cursor.fetchone()

        if book:
            cursor.execute("SELECT * FROM book_issues WHERE ISBN = %s", (ISBN,))
            issued_book = cursor.fetchone()

            if issued_book:
                print("The book is already issued to another student.")
            else:
                issue_date = datetime.date.today()
                due_date = issue_date + datetime.timedelta(days=7)
                cursor.execute("INSERT INTO book_issues (Student_ID, ISBN, Issue_Date, Due_Date) "
                               "VALUES (%s, %s, %s, %s)", (student_id, ISBN, issue_date, due_date))
                print(f"Book with ISBN {ISBN} issued to student {student_id}. Due date: {due_date}")

        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to return a book
def return_book(conn, student_id, ISBN):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        book = cursor.fetchone()

        if book:
            cursor.execute("SELECT * FROM book_issues WHERE ISBN = %s", (ISBN,))
            issued_book = cursor.fetchone()

            if issued_book:
                if issued_book[1] == student_id:
                    return_date = datetime.date.today()
                    due_date = issued_book[4]
                    days_issued = (return_date - due_date).days

                    if days_issued <= 0:
                        print(f"Book with ISBN {ISBN} returned on time.")
                    else:
                        late_fee = days_issued * 5  # Assuming a late fee of $5 per day
                        print(f"Book with ISBN {ISBN} returned late. Late fee: ${late_fee}")

                    cursor.execute("DELETE FROM book_issues WHERE ISBN = %s", (ISBN,))
                    print(f"Book with ISBN {ISBN} returned.")
                else:
                    print("This book is issued to another student.")
            else:
                print("Book with ISBN {ISBN} is not currently issued.")
        else:
            print(f"Book with ISBN {ISBN} not found in the library.")

        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

# Function to check admin authentication
def admin_authenticate():
    admin_username = "admin"
    admin_password = "password"
    entered_username = input("Enter admin username: ")
    entered_password = input("Enter admin password: ")
    return entered_username == admin_username and entered_password == admin_password

# Function to update book information (Admin Only)
def update_book_info(conn, ISBN, new_quantity):
    try:
        if admin_authenticate():
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET Quantity = %s WHERE ISBN = %s", (new_quantity, ISBN))
            print(f"Book with ISBN {ISBN} quantity updated to {new_quantity}.")
            conn.commit()
            cursor.close()
        else:
            print("Admin authentication failed. You are not authorized to update books.")
    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    db_connection = connect_to_db()
    if db_connection:
        while True:
            print("\nLibrary Management System")
            print("1. Add a Book")
            print("2. Remove a Book")
            print("3. Search for a Book by ISBN")
            print("4. Count Total Books")
            print("5. Count Available Books by Title")
            print("6. Issue a Book to a Student")
            print("7. Return a Book")
            print("8. Update Book Quantity (Admin Only)")
            print("9. Exit")
            
            choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

            if choice == '1':
                ISBN = input("Enter the ISBN of the book: ")
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                quantity = int(input("Enter the quantity of the book: "))
                add_book(db_connection, ISBN, title, author, quantity)
            elif choice == '2':
                ISBN = input("Enter the ISBN of the book to remove: ")
                remove_book(db_connection, ISBN)
            elif choice == '3':
                ISBN = input("Enter the ISBN of the book to search: ")
                search_book_by_ISBN(db_connection, ISBN)
            elif choice == '4':
                count_total_books(db_connection)
            elif choice == '5':
                title = input("Enter the title of the book to count available copies: ")
                count_available_books_by_title(db_connection, title)
            elif choice == '6':
                student_id = int(input("Enter the student ID: "))
                ISBN = input("Enter the ISBN of the book to issue: ")
                issue_book(db_connection, student_id, ISBN)
            elif choice == '7':
                student_id = int(input("Enter the student ID: "))
                ISBN = input("Enter the ISBN of the book to return: ")
                return_book(db_connection, student_id, ISBN)
            elif choice == '8':
                ISBN = input("Enter the ISBN of the book to update quantity: ")
                new_quantity = int(input("Enter the new quantity: "))
                update_book_info(db_connection, ISBN, new_quantity)
            elif choice == '9':
                print("Exiting the library management system.")
                break
            else:
                print("Invalid choice. Please choose a valid option (1/2/3/4/5/6/7/8/9).")

        db_connection.close()
