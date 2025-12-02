import json
import logging
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, filepath="data/catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load()

    def load(self):
        try:
            if not self.filepath.exists():
                logging.warning("Catalog file not found. Creating new one.")
                self.save()
                return

            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.books = [Book(**entry) for entry in data]

        except Exception as e:
            logging.error(f"Error loading file: {e}")
            self.books = []
            self.save()

    def save(self):
        try:
            with open(self.filepath, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save()
        logging.info(f"Added book: {title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books
