'''test_api.py'''
import unittest
from api import app

#class to respresent create an get books testcase
class TestCreateAndGetAllBooks(unittest.TestCase):
    '''class to tests app.py'''
    def setUp(self):
        '''create a test client'''
        self.client = app.APP.test_client
        self.testbook = {"book_id":1, "title":"Figure skating",
                         "author":"Jonas", "edition":"3rd", "copies":20}
                           
    def test_api_can_create_books(self):
        '''test that API can create a book (POST request)'''
        response = self.client().post('/api/v1/books', data=self.testbook)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", response.data)
    
    def test_api_can_get_all_books(self):
        '''test that api can get all books'''
        response = self.client().post('/api/v1/books', data=self.testbook)
        self.assertEqual(response.status_code, 200)

        response = self.client().get('/api/v1/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Figure skating for dummies", str(response.data))

class TestModifyBookById(unittest.TestCase):
    '''class to represent test for modification of books by id'''
    def setUp(self):
        '''create a test client'''
        self.client = app.APP.test_client
        self.testbook = {"book_id":5, "title":"Figure skating",
                         "author":"Jonas", "edition":"3rd", "copies":20}

    def test_api_can_get_book_by_id(self):
        '''test that api can retrieve book by id'''
        result = self.client().get('/api/v1/books/2')
        self.assertEqual(result.status_code, 200)
        self.assertIn("Fly away birdie", str(result.data))

    def test_book_can_be_edited(self):
        '''test that api can modify book'''
        res = self.client().post('/api/v1/books', data={"book_id": 2,
                                                        "title": "The fault in our stars",
                                                        "author": "Not John Green",
                                                        "edition": "7th", "copies": 30})
        self.assertEqual(res.status_code, 200)

        res = self.client().put('/api/v1/books/2', data={"title":"The fault in our stars",
                                                         "author":"John Greene",
                                                         "eidition":"7th", "copies": 29})
        self.assertEqual(res.status_code, 200)
        results = self.client().get('/api/v1/books/2')
        self.assertIn("John Greene", str(results.data))

    def test_delete_book(self):
        '''test that api can delete book'''
        res = self.client().post('/api/v1/books', data={"book_id":3,
                                                        "title": "Queer cats, An African Tale",
                                                        "author" : "Chimamano Nakote"})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete('/api/v1/books/3')
        self.assertEqual(res.status_code, 200)
        #test to check whether deleted item exists
        result = self.client().get('/api/v1/books/3')
        self.assertEqual(result.status_code, 404)

class TestUserBorrowBook(unittest.TestCase):
    '''class to represent user tests'''
    def setUp(self):
        self.client = app.APP.test_client
        self.user = {"username": "njeri-ngigi", "password":"1234"}

    '''def test_borrow_book(self):

        rv=self.client().post('/api/v1/users/books/3', data=self.user)
        print(rv.data)
        self.assertEqual(rv.status_code, 200)'''

if __name__ == "__main__":
    unittest.main()
