# -*- coding: utf-8 -*-
"""Capstone_Library Book Management

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AWJ6UARD2DlOD6GxgLM9gaSK9RKdRG0r

Library Book Management
"""

import re
from datetime import datetime
import copy

### DUMMY DATA ###

listing = [
    {
        "Full Name": "Andi Pratama",
        "ID Number": "3276012309870004",
        "book_title": "Rahasia di Balik Layar",
        "author": "Dewi Lestari",
        "book_id": "472918",
        "book_status": "returned",
        "borrow_date": "05-06-2025",
        "return_date": "08-06-2025",
        "return_deadline": "15-06-2025"
    },
    {
        "Full Name": "Siti Marlina",
        "ID Number": "3205046702990007",
        "book_title": "Jejak Langkah Senja",
        "author": "Ahmad Fuadi",
        "book_id": "839205",
        "book_status": "borrowed",
        "borrow_date": "03-06-2025",
        "return_date": "",
        "return_deadline": "13-06-2025"
    },
    {
        "Full Name": "Budi Santoso",
        "ID Number": "3174091508840002",
        "book_title": "Langit Merah di Utara",
        "author": "Tere Liye",
        "book_id": "756431",
        "book_status": "returned",
        "borrow_date": "01-06-2025",
        "return_date": "07-06-2025",
        "return_deadline": "10-06-2025"
    }
]

deleted_history = []

### Input validation

def validate_string(prompt, allow_numbers=False):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        if not allow_numbers and any(char.isdigit() for char in value):
            print("Input should not contain numbers. Please re-enter.")
            continue
        if allow_numbers and any(char.isdigit() for char in value):
            confirm = input(f"Are you sure '{value}' is correct? (y/n): ").strip().lower()
            if confirm != 'y':
                continue
        return value

def validate_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print("Invalid date format! Please use DD-MM-YYYY.")

#### MAIN MENU

def main_menu():
    while True:
        print("\n=== Digital Library Menu ====")
        print("1. View Book Status")
        print("2. Borrow Book")
        print("3. Add New Book")
        print("4. Delete Book")
        print("5. View Deleted Book History")
        print("6. Restore Deleted Book")
        print("7. Search Book Borrowing Status")
        print("8. Calculate Late Return Fines")
        print("9. Exit")

        choice = input("Choose Menu (1-9): ")

        if choice == '1':
            check_book_status(listing)
        elif choice == '2':
            input_borrowing_data()
        elif choice == '3':
            register_new_book(listing)
        elif choice == '4':
            delete_book_by_title(listing)
        elif choice == '5':
            view_deleted_history()
        elif choice == '6':
            restore_deleted_book()
        elif choice == '7':
            search_book_borrowing_status()
        elif choice == '8':
            calculate_late_return_fines(listing)
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid input, please choose 1-9.")

####
#### CRUD
####

## View Book Status
def check_book_status(data_list):
    available_books = []
    borrowed_books = []

    print("\n== Library Menu ===")

    for data in data_list:
        title = data.get("book_title", "Unknown")
        status = data.get("book_status", "").lower()

        if status == "borrowed":
            borrowed_books.append(title)
        elif status == "returned":
            available_books.append(title)

    if borrowed_books:
        print("\nCurrently Borrowed Books:")
        for title in borrowed_books:
            print(f"- {title}")
    else:
        print("No books currently borrowed.")

    if available_books:
        print("\nAvailable Books:")
        for title in available_books:
            print(f"- {title}")
    else:
        print("No available books.")

## Borrow Book Input
def input_borrowing_data():
    print("\n=== Borrow Book ===")
    while True:
        full_name = validate_string("Enter Full Name: ")
        id_number = input("Enter ID Number: ").strip()

        book_title = validate_string("Enter Book Title to Borrow: ", allow_numbers=True)

        # Validate if book exists and available
        book = None
        for b in listing:
            if b['book_title'].lower() == book_title.lower():
                book = b
                break

        if not book:
            print(f"Book '{book_title}' is not available in the system.")
            add_new = input("Would you like to register this book? (y/n): ").strip().lower()
            if add_new == 'y':
                register_new_book(listing)
            continue

        if book['book_status'] == 'borrowed':
            print(f"Book '{book_title}' is currently borrowed by someone else.")
            continue

        borrow_date = validate_date("Enter Borrowing Date (DD-MM-YYYY): ")
        return_deadline = validate_date("Enter Return Deadline (DD-MM-YYYY): ")

        book['Full Name'] = full_name
        book['ID Number'] = id_number
        book['borrow_date'] = borrow_date
        book['return_deadline'] = return_deadline
        book['return_date'] = ""
        book['book_status'] = "borrowed"

        print("\nBorrowing data saved successfully!")
        break

## Add New Book
def register_new_book(book_list):
    print("\n=== Register New Book ===")
    title = validate_string("Enter Book Title: ", allow_numbers=True)
    author = validate_string("Enter Author Name: ")
    new_book_id = str(len(book_list) + len(deleted_history) + 1).zfill(6)

    new_book = {
        "Full Name": "",
        "ID Number": "",
        "book_title": title,
        "author": author,
        "book_id": new_book_id,
        "book_status": "returned",
        "borrow_date": "",
        "return_date": "",
        "return_deadline": ""
    }

    book_list.append(new_book)
    print(f"Book '{title}' added successfully with ID {new_book_id}")

## Delete Book
def delete_book_by_title(book_data):
    print("\n=== Delete Book ===")
    book_title = validate_string("Enter book title to delete: ", allow_numbers=True)

    for i, book in enumerate(book_data):
        if book.get("book_title", "").lower() == book_title.lower():
            confirm = input(f"Are you sure you want to delete '{book['book_title']}'? (y/n): ").lower()
            if confirm == 'y':
                deleted_history.append(copy.deepcopy(book))
                del book_data[i]
                print(f"Book '{book['book_title']}' successfully deleted.")
            else:
                print("Deletion cancelled.")
            return
    print(f"Book '{book_title}' not found.")

## View Deleted Book History
def view_deleted_history():
    print("\n=== Deleted Book History ===")
    if not deleted_history:
        print("No deleted books.")
    else:
        for book in deleted_history:
            print(f"- {book['book_title']} by {book['author']}")

## Restore Deleted Book
def restore_deleted_book():
    print("\n=== Restore Deleted Book ===")
    if not deleted_history:
        print("No book to restore.")
        return

    book_title = validate_string("Enter book title to restore: ", allow_numbers=True)

    for i, book in enumerate(deleted_history):
        if book['book_title'].lower() == book_title.lower():
            listing.append(book)
            del deleted_history[i]
            print(f"Book '{book_title}' successfully restored.")
            return

    print(f"Book '{book_title}' not found in deleted history.")

## Search Borrowing Status
def search_book_borrowing_status():
    print("\n=== Search Borrowing Status ===")
    book_title = validate_string("Enter book title: ", allow_numbers=True)

    for data in listing:
        if data['book_title'].lower() == book_title.lower():
            name = data.get("Full Name", "No borrower")
            return_date = data.get("return_date", "")
            status = data.get("book_status")

            if status == "borrowed":
                print(f"The book '{book_title}' is STILL borrowed by {name}.")
            else:
                print(f"The book '{book_title}' has ALREADY been returned by {name}.")
            return

    print(f"Book '{book_title}' not found in database.")

## Calculate Late Return Fine
def calculate_late_return_fines(book_data):
    print("\n=== Calculate Late Return Fines ===")

    for data in book_data:
        title = data.get("book_title", "Unknown Title")
        return_date = data.get("return_date")
        due_date = data.get("return_deadline")

        if not return_date or not due_date:
            continue

        try:
            return_date_obj = datetime.strptime(return_date, "%d-%m-%Y")
            due_date_obj = datetime.strptime(due_date, "%d-%m-%Y")

            days_late = (return_date_obj - due_date_obj).days

            if days_late > 0:
                fine = days_late * 100000
                print(f"Book '{title}' was returned {days_late} day(s) late. Fine: Rp {fine:,}")
            else:
                print(f"Book '{title}' was returned on time.")
        except ValueError:
            print(f"Invalid date format for book '{title}'.")

main_menu()

"""# New section"""

