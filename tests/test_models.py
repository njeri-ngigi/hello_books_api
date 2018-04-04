'''test_models.py'''
import unittest
from werkzeug.security import check_password_hash
from hello_books_api import models

#class to test models
class TestModels(unittest.TestCase):
    '''class to test models created'''
    def setUp(self):
        self.my_book = models.Books()
        self.my_user = models.Users()

    def test_put_book(self):
        '''test that put_book adds book to dictionary ALL_BOOKS'''
        result = self.my_book.put("Harry Potter", "JK Rowling", "1st", 22, "available")
        self.assertEqual("Book added successfully", result["message"])

    def test_get_all_books(self):
        '''tests get_all retrieves all books in the dictionary'''
        result = self.my_book.get_all()
        self.assertEqual(result, models.ALL_BOOKS)

    def test_edit_book(self):
        '''test that edit_book edits'''
        self.my_book.put("Make me laugh", "Louis Lenard", "1st", 20, "available")
        result = self.my_book.edit_book("Harry Potter and the Goblet of Giggles",
                                        "Louis Lenard", "2nd", 20, "available")
        self.assertIn("Details edited successfully", result["message"])

    def test_get_single_book(self):
        '''test that get_single_book returns a book from dictionary ALL_BOOKS'''
        self.my_book.put("How long to live", "Mary Howard",
                         "1st", 19, "available")
        result = self.my_book.get_single_book(19)
        self.assertEqual("Mary Howard", result['author'])

    def test_delete_book(self):
        '''test that delete_book deletes book from ALL_BOOKS'''
        self.my_book.put("Leople", "Master Xi", "1st", 15, "available")
        result = self.my_book.delete(15)
        self.assertEqual(
            {"message": "Book 15 deleted successfully"}, result)

    def test_put_user(self):
        '''test that put_user adds user to dictionary USERS'''
        result = self.my_user.put("Adelle Owino", "a-owino", "ac@ab.com", "imeowit")
        self.assertIn("user registered successfully", result["message"])

    def test_verify_password(self):
        '''test verify password'''
        result = self.my_user.verify_password("a-owino", "imeowit")
        self.assertEqual(result, "True")
    def test_borrow_book(self):
        '''test borrow a book'''
        self.my_book.put("Lady Lord", "Ling liu", "1st", 11, "available")
        result = self.my_user.borrow_book(11)
        self.assertEqual(result, {"message":"Book successfully checked out"})
        result2 = self.my_user.borrow_book(11)
        self.assertEqual(result2, {"message":"Book is currently unavailble"})

    def test_reset_password(self):
        '''test reset password'''
        self.my_user.put("Martha", "martha", "ac@ab.com", "kesho")
        result = self.my_user.reset_password("martha")
        self.assertEqual(False, check_password_hash("kesho", result["new_password"]))
        self.assertEqual(7, len(result["new_password"]))


#make the tests conviniently executable
if __name__ == "__main__":
    unittest.main()
