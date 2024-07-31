import unittest
from library import Library

class TestBook(unittest.TestCase):


    def setUp(self) -> None:
        self.library = Library()

    def test_add_book(self):

        self.assertTrue(self.library.add_book(
            title="Последний герой",
            author="Александр Кабаков",
            year="2024",
            status="1"
        ))

        self.assertTrue(self.library.add_book(
            title="Мастер и Маргарита",
            author="Михаил Булгаков",
            year="2012",
            status="1"
        ))

        self.assertFalse(self.library.add_book(
            title="Последний герой",
            author="Александр Кабаков",
            year="2023",
            status="5"
        ))

        self.assertFalse(self.library.add_book(
            title="",
            author="Александр Кабаков",
            year="",
            status=""
        ))

        self.assertFalse(self.library.add_book(
            title="Нравственные письма к Луцилию",
            author="Сенека",
            year="2025",
            status="1" 
        ))

        self.assertFalse(self.library.add_book(
            title="asdfasd",
            author="Александр Кабаков",
            year="1234",
            status="l"
        ))

    def test_del_book(self):
        self.assertFalse(self.library.delete_book(-1))
        self.assertFalse(self.library.delete_book(0))

    def test_search_book(self):

        self.assertTrue(self.library.search_book(
            title="Последний герой",
            author="",
            year="",
        ))

        self.assertFalse(self.library.search_book(
            title="",
        ))

        self.assertTrue(self.library.search_book(
            year="2012",
        ))

    def test_change_status(self):

        self.assertFalse(self.library.change_books_status(
            id=0, new_value=1
        ))

        self.assertFalse(self.library.change_books_status(
            id=-1, new_value=1
        ))

        self.assertFalse(self.library.change_books_status(
            id=2, new_value=10
        ))


if __name__ == "__main__":
    unittest.main()