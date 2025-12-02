import logging
from library_manager.inventory import LibraryInventory

logging.basicConfig(filename="library.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def menu():
    print("\n====== Library Inventory Manager ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                inventory.add_book(title, author, isbn)
                print("Book added successfully!!\n")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    inventory.save()
                    print("Book issued!!\n")
                else:
                    print("Book not available.\n")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    inventory.save()
                    print("Book returned!!\n")
                else:
                    print("Invalid request.\n")

            elif choice == "4":
                for b in inventory.display_all():
                    print(b)

            elif choice == "5":
                title = input("Enter title to search: ")
                results = inventory.search_by_title(title)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.\n")

            elif choice == "6":
                print("Goodbye!!")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            logging.error(f"Error: {e}")
            print("Something went wrong. Please try again.")

if __name__ == "__main__":
    main()
