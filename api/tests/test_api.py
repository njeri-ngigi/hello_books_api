#test_api.py
import unittest, json

from api import app 

#class to respresent books testcase
class TestCreateBooks(unittest.TestCase):
    def setUp(self):
        #create a test client
        self.app = app.app.create_app()
        self.client = self.app.test_client  

        self.book= {"title":"Figure skating for dummies", "author":"Jonas Jonas"}
    
    #test that API can create a book (POST request)
    def test_api_can_create_books(self):
        response = self.client().post('/books', data=self.book)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", response.data)
    
    #test that api can get all books
    def test_api_can_get_all_books(self):
        response = self.client().post('/books', data=self.book)
        self.assertEqual(response.status_code, 200)
        response = self.client().get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", str(response.data))

    #test that api can delete book
    #test that api can modify book
    #test that api can retrieve book by id


   

if __name__ == "__main__":
    unittest.main()
    #test API can get a single book using its id
    #test API can edit/modify an existing book
    #test API can delete an existing book

