import unittest
import models 
#from app import app

class TestModel(unittest.TestCase):
    def setUp(self):
        self.my_book = models.Books()
        self.my_user = models.Users()
        
    def test_put_book(self):
        result = self.my_book.put("Harry Potter", "JK Rowling")
        self.assertIn("Harry Potter", self.my_book.books)
    
    def test_get_book(self):
    	self.my_book.books["hello world"]="Leah Beau"
        result = self.my_book.get()
        self.assertEqual(self.my_book.books, result)

    def test_delete_book(self):
    	self.my_book.books["hello world"]="Leah Beau"
    	self.my_book.books["Harry Potter"]="JK Rowling"
        result = self.my_book.delete("Harry Potter")
          
        self.assertNotIn("Harry Potter", result)

    

    def test_put_user(self):
    	result = self.my_user.put("njeri-ngigi", "abc@a.com", "imeowit")
    	self.assertIn("njeri-ngigi", self.my_user.users)
    	self.assertEqual(result["njeri-ngigi"], self.my_user.users["njeri-ngigi"])
    	


