import unittest

from app import models 

#class to test models
class TestModels(unittest.TestCase):
    def setUp(self):
        self.my_book = models.Books()
        self.my_user = models.Users()
        self.my_book.books={"Hello world":"Leah Beau"}
        
    def test_put_book(self):
        self.my_book.put("Harry Potter", "JK Rowling")
        self.assertIn("Harry Potter", self.my_book.books)
    
    def test_get_book(self):
        result = self.my_book.get_all()
        self.assertEqual(self.my_book.books, result)

    def test_get_single_book(self):
        result = self.my_book.get_single_book("Hello world")
        self.assertEqual(result, {"Hello world" :self.my_book.books["Hello world"]})
        
    def test_delete_book(self):
        self.my_book.books["Harry Potter"]="JK Rowling"
        result = self.my_book.delete("Harry Potter")
          
        self.assertNotIn("Harry Potter", result)

    def test_put_user(self):
    	result = self.my_user.put("njeri-ngigi", "abc@a.com", "imeowit")
    	self.assertIn("njeri-ngigi", self.my_user.users)
    	self.assertEqual(result["njeri-ngigi"], self.my_user.users["njeri-ngigi"])

#make the tests conviniently executable
if __name__ == "__main__":
	unittest.main()


