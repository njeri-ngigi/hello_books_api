'''app.py'''
import re
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from api.models import Books, Users



APP = Flask(__name__)
APP.config["TESTING"] = True

MY_BOOK = Books()

#sent_data = request.get_json(force=True)

@APP.route('/api/v1/books', methods=['GET', 'POST'])
def books():
    '''endpoint to add book and get all books'''
    if request.method == 'POST':
    #add a book method="POST"
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        book_id = data.get('book_id')
        response = jsonify(MY_BOOK.put(title, author, edition, book_id))
        response.status_code = 200

        return response

    #get a book method="GET"
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
        response = jsonify(MY_BOOK.edit_book(title, author, edition, book_id))
        response.status_code = 200

        return response

    
    #delete a book, method=DELETE
    response = jsonify(MY_BOOK.delete(book_id))
    response.status_code = 200

    return response


#check if jwt token is in blacklist
APP.config['JWT_SECRET_KEY'] = 'my-key'
APP.config['JWT_BLACKLIST_ENABLED'] = True
APP.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(APP)

BLACKLIST = set()


@jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    '''check if jti(unique identifier) is in black list'''
    jti = decrypted_token['jti']
    return jti in BLACKLIST

MY_USER = Users()

@APP.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''endpoint to register a user'''
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if len(password) < 4:
        return jsonify({"message": "password is too short"})
    if confirm_password != password:
        return jsonify({"message": "Passwords don't match"})
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match is None:
        return jsonify({"message": "Enter a valid email address"})
    response = jsonify(MY_USER.put(name, username, email, password))
    response.status_code = 200
    return response


@APP.route('/api/v1/users/books/<int:book_id>', methods=['POST'])
@jwt_required
def users_books(book_id):
    '''user can borrow a book if logged in'''
    response = jsonify(MY_USER.borrow_book(book_id))
    response.status_code = 200
    return response


@APP.route('/api/v1/auth/login', methods=['POST'])
def login():
    '''login user by verifying password and creating an access token'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth = MY_USER.verify_password(username, password)

    if auth == "True":
        access_token = create_access_token(identity=username)
        return access_token

    response = jsonify(auth)
    response.status_code = 401
    return response


@APP.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout():
    '''logout user by revoking password'''
    jti = get_raw_jwt()['jti']
    BLACKLIST.add(jti)
    return jsonify({"message": "Successfully logged out"})


@APP.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    '''reset user password'''
    data = request.get_json()
    username = data.get("username")

    response = jsonify(MY_USER.reset_password(username))
    response.status_code = 200
    return response


#method to run app.py
if __name__ == '__main__':
    APP.run(debug=True)
