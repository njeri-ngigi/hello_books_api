#test_models.py
import unittest
from api import my_app

#class to test models
class TestModels(unittest.TestCase):
    def setUp(self):
        self.my_book = my_app.Books()
        self.my_user = my_app.Users()
        
        
    def test_put_book(self):
        result = self.my_book.put("Harry Potter", "JK Rowling", "1st", 4, 2)
        self.assertIn("Harry Potter", result['title'])
    
    def test_get_book(self):
        result = self.my_book.put("Hello world", "Leah Beau", "3rd", 3, 1)
        result = self.my_book.get_all()        
        self.assertTrue(result)

    def test_edit_book(self):
        result = self.my_book.edit_book("Harry Potter and the Goblet of Giggles", "JK Rowling", "2nd", 2, 2)
        self.assertIn("Harry Potter and the Goblet of Giggles", result["title"])

    def test_get_single_book(self):
        result = self.my_book.get_single_book(2)
        self.assertEqual("JK Rowling", result['author'])
        
    def test_delete_book(self):
        result = self.my_book.put("Play hard", "Eustace", "1st", 4, 3)
        self.assertIn("Play hard", result['title'])

        result = self.my_book.delete(3)
          
        self.assertNotIn(3, result)

    def test_put_user(self):
    	result = self.my_user.put("Adelle Owino","a-owino", "ac@ab.com", "0767","imeowit")
    	result2 = self.my_user.show_all_users()
        self.assertIn("a-owino", result2)

    def test_verify_password(self):
        result = self.my_user.verify_password("a-owino", "imeowit")
        
        self.assertEqual(result,{"message": "Successfully logged in"})

    def test_borrow_book(self):
        result = self.my_user.borrow_book(1)
        self.assertEqual(result, {"message":"Book successfully checked out"})
    	

#make the tests conviniently executable
if __name__ == "__main__":
	unittest.main()


