class BookNotFoundError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError(f"Book '{title}' not found in the library")
        self.books.remove(title)

    def list_books(self):
        return self.books

# Тесты
import unittest

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        library.add_book("Book1")
        self.assertIn("Book1", library.list_books())

    def test_remove_book(self):
        library = Library()
        library.add_book("Book1")
        library.remove_book("Book1")
        self.assertNotIn("Book1", library.list_books())

    def test_remove_book_not_found(self):
        library = Library()
        with self.assertRaises(BookNotFoundError):
            library.remove_book("Book1")

    def test_list_books(self):
        library = Library()
        library.add_book("Book1")
        library.add_book("Book2")
        library.remove_book("Book1")
        self.assertEqual(library.list_books(), ["Book2"])

    def test_list_books_empty(self):
        library = Library()
        self.assertEqual(library.list_books(), [])

if __name__ == "__main__":
    unittest.main()
