import csv

FILENAME = "books.csv"
UNREAD_STATUS = 'u'
COMPLETED_STATUS = 'c'

def main():
    print("Books to Read 1.0 by [Your Name]")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.")

    choice = ''
    while choice != 'Q':
        print("Menu:")
        print("D - Display books")
        print("A - Add a new book")
        print("C - Complete a book")
        print("Q - Quit")

        choice = get_menu_choice()
        if choice == 'D':
            display_books(books)
        elif choice == 'A':
            add_new_book(books)
        elif choice == 'C':
            complete_book(books)
        elif choice != 'Q':
            print("Invalid menu choice")

    save_books(FILENAME, books)
    print(f"{len(books)} books saved to {FILENAME}")
    print('"So many books, so little time. Frank Zappa"')

def get_non_empty_string(prompt):
    input_string = ""
    while input_string == "":
        input_string = input(prompt).strip()
        if input_string == "":
            print("Input can not be blank")
    return input_string

def positive_integer(prompt, minimum=0):
    while True:
        try:
            user_input = input(prompt)
            if user_input.strip() == "":
                print("Invalid input - please enter a valid number")
                continue
            number = int(user_input)

            if number < minimum:
                if minimum == 0:
                    print("Number must be >= 0")
                else:
                    print("Number must be > 0")
            else:
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")

def get_menu_choice():
    return get_non_empty_string(">>> ").upper()

def load_books(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split(',')
                if len(row) == 4:
                    try:
                        row[2] = int(row[2].strip())
                        books.append(row)
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return books

def save_books(filename, books):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

def display_books(books):
    if not books:
        print("No books in the list.")
        return

    sorted_books = sorted(books, key=lambda book: (book[1], book[0]))
    max_title_width = max(len(book[0]) for book in sorted_books)
    max_author_width = max(len(book[1]) for book in sorted_books)

    unread_count = 0
    total_unread_pages = 0

    for i, book in enumerate(sorted_books, 1):
        title, author, pages, status = book[0], book[1], book[2], book[3]

        if status == UNREAD_STATUS:
            is_unread_marker = "*"
            unread_count += 1
            total_unread_pages += pages
        else:
            is_unread_marker = " "

        print(
            f"{is_unread_marker}{i: >1}. {title:<{max_title_width}} by "
            f"{author:<{max_author_width}} {pages: >4} pages"
        )

    if unread_count == 0:
        if len(books) > 0 and all(book[3] == COMPLETED_STATUS for book in books):
            print("No books left to read. Why not add a new book?")
        else:
            print("No unread books - well done!")
    else:
        print(f"You still need to read {total_unread_pages} pages in {unread_count} books.")

def add_new_book(books):
    title = get_non_empty_string("Title: ")
    author = get_non_empty_string("Author: ")
    pages = positive_integer("Number of Pages: ")
    new_book = [title, author, pages, UNREAD_STATUS]
    books.append(new_book)
    print(f"{title} by {author} ({pages} pages) added.")

def complete_book(books):
    if not any(book[3] == UNREAD_STATUS for book in books):
        print("No unread books - well done!")
        return
    display_books(books)
    print("Enter number of book to mark as completed")
    sorted_books = sorted(books, key=lambda book: (book[1], book[0]))
    while True:
        book_index = positive_integer(">>> ", minimum=1)
        if 1 <= book_index <= len(sorted_books):
            selected_book = sorted_books[book_index - 1]

            if selected_book[3] == COMPLETED_STATUS:
                print("That book is already completed")
                continue

            for book_original in books:
                if book_original[0] == selected_book[0] and \
                        book_original[1] == selected_book[1] and \
                        book_original[2] == selected_book[2]:
                    book_original[3] = COMPLETED_STATUS
                    print(f"{book_original[0]} by {book_original[1]} completed!")
                    return
        else:
            print("Invalid book number")

if __name__ == '__main__':
    main()