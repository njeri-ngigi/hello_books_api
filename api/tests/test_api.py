import os
import unittest
import json
import app, flask


#class to respresent books testcase
class TestCreateBooks(unittest.TestCase):
    def setUp(self):
        #create a test client
        
        self.app = app.app.test_client()
        self.user = Users()
         
             
        self.book= {"title":"Figure skating for dummies", "author":"Jonas Jonas"}
    
    #test that API can create a book (POST request)
    def test_api_can_create_books(self):
        response = self.app.post('/books', data=self.book)
        self.assertEqual(response.status_code, 200)
        self.assertIn({"title":"Figure skating for dummies"}, response.data)

class TestGetAllBooks(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    #test that api can get all books
    def test_api_can_get_all_books(self):
        response = self.app.post('/books', data=self.book)
        self.assertEqual(response.status_code, 200)
        res = self.app.get('/books')
        self.assertEqual(res.status_code, 200)
        self.assertIn({"title":"Figure skating for dummies"}, str(res.data))


if __name__ == "__main__":
    unittest.main()
    #test API can get a single book using its id
    #test API can edit/modify an existing book
    #test API can delete an existing book

