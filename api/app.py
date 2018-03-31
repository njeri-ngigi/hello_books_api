'''app.py'''
import re
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash
from models import Books, Users

APP = Flask(__name__)
#APP.config["TESTING"] = True

MY_BOOK = Books()

@APP.route('/api/v1/books', methods=['GET', 'POST'])
def books():
    '''endpoint to add book and get all books'''
    if request.method == 'POST':
        #add a book method="POST"
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        copies = data.get('copies')
        book_id = data.get('book_id')
        response = jsonify(MY_BOOK.put(title, author, edition, copies, book_id))
        response.status_code = 200

        return response

    #get a book method="GET"
    else:
        get_books = MY_BOOK.get_all()
        response = jsonify(get_books)
        response.status_code = 200

        return response

@APP.route('/api/v1/books/<int:book_id>', methods=['PUT', 'GET', 'DELETE'])
def book_book_id(book_id):
    '''endpoint to edit, modify and delete a book by id'''
    if request.method == 'GET':
    #get a book by its id
        get_book = MY_BOOK.get_single_book(book_id)
        response = jsonify(get_book)
        response.status_code = 200

        return response

    elif request.method == 'PUT':
    #modify or edit a book method
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        copies = data.get('copies')
        response = jsonify(MY_BOOK.edit_book(title, author, edition, copies, book_id))
        response.status_code = 200

        return response

    else:
        #delete a book, method=DELETE
        response = jsonify(MY_BOOK.delete(book_id))
        response.status_code = 200

        return response

MY_USER = Users()
APP.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(APP)

@APP.route('/api/v1/users/books/<int:book_id>', methods=['POST'])
def users_books(book_id):
    '''endpoint to borrow a book'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth = MY_USER.verify_password(username, password)

    if auth == "True":
        response = jsonify(MY_USER.borrow_book(book_id))
        response.status_code = 200
        return response
    if auth == "False":
        return {"Message": "Authorization failed"}

@APP.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''endpoint to register a user'''
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

   
    if len(password) < 4:
        return jsonify({"message":"password is too short"})
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)
    if match == None:
        return jsonify({"message":"Enter a valid email address"})
    pw_hash = generate_password_hash(password)
    response = jsonify(MY_USER.put(name, username, email, pw_hash))
    response.status_code = 200
    return response
'''
@APP.route('/auth/login', methods=['POST'])
def login():
    pass

@APP.route('/auth/logout', methods=['POST'])
def logout():
    pass

@APP.route('/auth/reset-password', methods=['POST'])
def reset_password():
    pass
'''

#method to run app.py
if __name__ == '__main__':
    APP.run(debug=True)
    
