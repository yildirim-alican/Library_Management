from prettytable import PrettyTable

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        self.book_id = self.get_next_book_id()

    def __del__(self):
        self.file.close()

    def get_next_book_id(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if book_lines:
            last_line = book_lines[-1]
            last_book_id = int(last_line.split(',')[0])
            return last_book_id + 1
        else:
            return 1

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        if not book_lines:
            print("No books found.")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Title", "Author", "Release Year", "Pages", "Category"]

            for line in book_lines:
                if line.count(',') == 5:
                    book_id, title, author, release_year, num_pages, category = line.split(',')
                    table.add_row([book_id, title, author, release_year, num_pages, category])
                else:
                    print(f"Invalid format in line: {line}")

            print(table)

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        category = input("Enter the category of the book: ")

        book_info = f"{self.book_id},{title},{author},{release_year},{num_pages},{category}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")
        self.book_id += 1

    def remove_book(self):
        title_to_remove = None

        remove_option = input("Enter 1 to remove by title or 2 to remove by book ID: ")

        if remove_option == '1':
            title_to_remove = input("Enter the title of the book to remove: ")
            identifier = title_to_remove
        elif remove_option == '2':
            identifier = input("Enter the book ID to remove: ")
        else:
            print("Invalid option. Please enter 1 or 2.")
            return

        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        for i, line in enumerate(book_lines):
            if line.count(',') == 5:
                book_id, title, author, release_year, num_pages, category = line.split(',')
                if title_to_remove == title or identifier == book_id:
                    del book_lines[i]
                    break
            else:
                print(f"Invalid format in line: {line}")

        self.file.truncate(0)
        for line in book_lines:
            self.file.write(line + '\n')

        print(f"Book '{identifier}' removed successfully.")

    def modify_book(self):
        self.list_books()

        book_id_to_modify = input("Enter the ID of the book you want to modify: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        for i, line in enumerate(book_lines):
            if line.count(',') == 5:
                book_id, title, author, release_year, num_pages, category = line.split(',')
                if book_id_to_modify == book_id:
                    new_title = input(f"Enter the new title for the book (old: {title}): ")
                    new_author = input(f"Enter the new author for the book (old: {author}): ")
                    new_release_year = input(f"Enter the new release year for the book (old: {release_year}): ")
                    new_num_pages = input(f"Enter the new number of pages for the book (old: {num_pages}): ")
                    new_category = input(f"Enter the new category for the book (old: {category}): ")

                    updated_line = f"{book_id},{new_title},{new_author},{new_release_year},{new_num_pages},{new_category}"
                    book_lines[i] = updated_line
                    break
        else:
            print(f"Book with ID '{book_id_to_modify}' not found.")

        updated_content = '\n'.join(book_lines)

        self.file.seek(0)
        self.file.truncate(0)
        self.file.write(updated_content)

        print(f"Book with ID '{book_id_to_modify}' modified successfully.")

def main():
    lib = Library()

    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")

        menu_table = PrettyTable()
        menu_table.field_names = ["Option", "Description"]
        menu_table.add_row(["1", "List Books"])
        menu_table.add_row(["2", "Add Book"])
        menu_table.add_row(["3", "Remove Book"])
        menu_table.add_row(["4", "Modify Book"])
        menu_table.add_row(["5", "Exit"])

        print(menu_table)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            lib.modify_book()
        elif choice == '5':
            print("Exiting the program. See You!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
