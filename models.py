'''models.py containing models for the API'''
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash

ALL_BOOKS = {}

class Books():
    '''class to represent book model'''
    def __init__(self):
        self.book = {}

    def get_all(self):
        '''return all books from ALL_BOOKS dictionary'''
        return ALL_BOOKS

    def get_single_book(self, book_id):
        '''get single book from ALL_BOOKS using id'''
        if book_id in ALL_BOOKS:
            return ALL_BOOKS[book_id]

        return {"message":"Book not found"}

    def put(self, title, author, edition, book_id, status):
        '''add a book to ALL_BOOKS'''
        if book_id in ALL_BOOKS:
            return {"message":"Book id entered already exists"}

        self.book["title"] = title
        self.book["author"] = author
        self.book["edition"] = edition
        self.book["status"] = status

        ALL_BOOKS[book_id] = self.book
        return {"message":"Book added successfully"}

    #edit a book
    def edit_book(self, title, author, edition, book_id, status):
        '''edit a book by its id'''
        if book_id in ALL_BOOKS:
            self.book["title"] = title
            self.book["author"] = author
            self.book["edition"] = edition
            self.book["status"] = status

            ALL_BOOKS[book_id] = self.book
            return {"message": "Details edited successfully"}
        return {"message":"Book you are trying to edit doesn't exist"}

    def delete(self, book_id):
        '''delete a book by its id'''
        if book_id in ALL_BOOKS:
            del ALL_BOOKS[book_id]
            return {"message":"Book {} deleted successfully".format(book_id)}

        return {"message":"Book you are trying to delete doesn't exist"}

USERS = {}

class Users():
    '''class to represent users model'''
    def __init__(self):
        self.user = {}

    def put(self, name, username, email, password):
        '''add a user to USERS'''
        if username in USERS:
            return {"message":"Username already exists"}
        
        self.user["name"] = name
        self.user["email"] = email
        pw_hash = generate_password_hash(password)
        self.user["password"] = pw_hash

        USERS[username] = self.user
        return {"message":"user registered successfully"}

    def verify_password(self, username, password):
        '''verify password'''
        if username in USERS:
            result = check_password_hash(USERS[username]["password"], password)
            if result is True:
                return "True"
            return {"message": "Password incorrect"}
        return {"message": "Incorrect username"}
    
    def borrow_book(self, book_id):
        '''borrow a book by book_id'''
        if book_id in ALL_BOOKS:
            if ALL_BOOKS[book_id]["status"] == "available":
                ALL_BOOKS[book_id]["status"]="unavailable"
                return {"message":"Book successfully checked out"}
            return {"message":"Book is currently unavailble"}
        return {"message":"Book not found"}
    
    def reset_password(self, username):
        '''reset user password'''
        if username in USERS:
            new_password = ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
            pw_hash = generate_password_hash(new_password)
            USERS[username]["password"] = pw_hash

            return {"new_password":new_password}

        return {"message":"Incorrect username"}
