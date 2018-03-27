#my_api_test.py

#test_api.py
import unittest
from flask import jsonify, json

from api import app

#class to respresent create an get books testcase
class TestCreateAndGetAllBooks(unittest.TestCase):
    def setUp(self):
        #create a test client
        self.client = app.app.test_client  

        self.testbook= {"book_id":1, "title":"Figure skating for dummies", "author":"Jonas Jonas", "edition":"3rd", "copies":20}
    
    #test that API can create a book (POST request)
    def test_api_can_create_books(self):
        response = self.client().post('/books', data=self.testbook)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", response.data)
    
    #test that api can get all books
    def test_api_can_get_all_books(self):
        response = self.client().post('/books', data=self.testbook)
        self.assertEqual(response.status_code, 200)

        response = self.client().get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", str(response.data))

#class to represent test for modification of books by id
class TestModifyBookById(unittest.TestCase):
    def setUp(self):
        #create a test client
        
        self.client = app.app.test_client
        self.testbook= {"book_id":5, "title":"Figure skating for dummies", "author":"Jonas Jonas", "edition":"3rd", "copies":20}


    #test that api can retrieve book by id
    def test_api_can_get_book_by_id(self):
        rv = self.client().post('/books', data=self.testbook)
        self.assertEqual(rv.status_code, 200)
        

       
        result = self.client().get('/books/5')
        
        print (result)
        self.assertEqual(result.status_code, 200)
        
        self.assertIn("Figure skating for dummies", str(result.data))

    #test that api can modify book
    def test_book_can_be_edited(self):
        rv = self.client().post('/books', data={"book_id":2, "title":"The fault in our stars", "author":"Not John Green", "edition":"7th", "copies":30})
        self.assertEqual(rv.status_code, 200)

        rv = self.client().put('/books/2', data={"title":"The fault in our stars", "author":"John Greene", "eidition":"7th", "copies": 29})
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/books/2')
        self.assertIn("John Greene", str(results.data))

    #test that api can delete book  
    def test_delete_book(self):
        rv = self.client().post('/books', data={"book_id":3, "title": "Queer cats, An African Tale", "author" : "Chimamano Nakote"})
        self.assertEqual(rv.status_code, 200)

        res = self.client().delete('/books/3')
        self.assertEqual(res.status_code, 200)
        #test to check whether deleted item exists
        result = self.client().get('/books/3')
        self.assertEqual(result.status_code, 404)

    


   

if __name__ == "__main__":
    unittest.main()
    #test API can get a single book using its id
    #test API can edit/modify an existing book
    #test API can delete an existing book

