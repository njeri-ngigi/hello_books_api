#test_models.py
import unittest
from api import app

#class to test models
class TestModels(unittest.TestCase):
    def setUp(self):
        self.my_book = app.models.Books()
        self.my_user = app.models.Users()
        self.my_book.books={1 : {"Hello world":"Leah Beau"}}
        
    def test_put_book(self):
        self.my_book.put("Harry Potter", "JK Rowling", 2)
        self.assertIn("Harry Potter", self.my_book.books[2])
    
    def test_get_book(self):
        result = self.my_book.get_all()
        self.assertEqual(self.my_book.books, result)

    def test_edit_book(self):
        self.my_book.put("Harry Potter", "JK Rowling", 2)
        self.assertIn("Harry Potter", self.my_book.books[2])

        result = self.my_book.edit_book("Harry Potter and the Goblet of Giggles", "JK Rowling", 2)
        self.assertIn("Harry Potter and the Goblet of Giggles", self.my_book.books[2])

    def test_get_single_book(self):
        self.my_book.put("Harry Potter", "JK Rowling", 2)
        self.assertIn("Harry Potter", self.my_book.books[2])
        result = self.my_book.get_single_book(2)
        self.assertEqual(result, {"Harry Potter" : "JK Rowling"})
        
    def test_delete_book(self):
        self.my_book.books[2]={"Harry Potter" : "JK Rowling"}
        result = self.my_book.delete(2)
          
        self.assertEqual(self.my_book.books, result)

    def test_put_user(self):
    	result = self.my_user.put("njeri-ngigi", "abc@a.com", "imeowit")
    	self.assertIn("njeri-ngigi", self.my_user.users)
    	self.assertEqual(result["njeri-ngigi"], self.my_user.users["njeri-ngigi"])

#make the tests conviniently executable
if __name__ == "__main__":
	unittest.main()


