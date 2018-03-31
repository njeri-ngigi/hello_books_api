'''test_models.py'''
import unittest
from api import models

#class to test models
class TestModels(unittest.TestCase):
    '''class to test models created'''
    def setUp(self):
        self.my_book = models.Books()
        self.my_user = models.Users()

    def test_put_book(self):
        '''test that put_book adds book to dictionary ALL_BOOKS'''
        result = self.my_book.put("Harry Potter", "JK Rowling", "1st", 22)
        self.assertIn("Harry Potter", result['title'])

    def test_get_all_books(self):
        '''tests get_all retrieves all books in the dictionary'''
        result = self.my_book.get_all()
        self.assertEqual(result, models.ALL_BOOKS)

    def test_edit_book(self):
        '''test that edit_book edits'''
        self.my_book.put("Make me laugh", "Louis Lenard", "1st", 20)
        result = self.my_book.edit_book("Harry Potter and the Goblet of Giggles",
                                        "Louis Lenard", "2nd", 20)
        self.assertIn("Harry Potter and the Goblet of Giggles", result["title"])

    def test_get_single_book(self):
        '''test that get_single_book returns a book from dictionary ALL_BOOKS'''
        self.my_book.put("How long to live", "Mary Howard", "1st", 19)
        result = self.my_book.get_single_book(19)
        self.assertEqual("Mary Howard", result['author'])

    def test_delete_book(self):
        '''test that delete_book deletes book from ALL_BOOKS'''
        self.my_book.put("Leople", "Master Xi", "1st", 15)
        result = self.my_book.delete(15)
        self.assertEqual(
            {"message": "Book 15 deleted successfully"}, result)

    def test_put_user(self):
        '''test that put_user adds user to dictionary USERS'''
        result = self.my_user.put("Adelle Owino", "a-owino", "ac@ab.com", "imeowit")
        self.assertIn("a-owino", result)

    def test_verify_password(self):
        '''test verify password'''
        result = self.my_user.verify_password("a-owino", "imeowit")
        self.assertEqual(result, "True")
    def test_borrow_book(self):
        '''test borrow a book'''
        result = self.my_user.borrow_book(1)
        self.assertEqual(result, {"message":"Book successfully checked out"})

#make the tests conviniently executable
if __name__ == "__main__":
    unittest.main()
