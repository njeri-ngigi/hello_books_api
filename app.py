'''app.py'''
import re
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
import models

app = Flask(__name__)
app.config["TESTING"] = True

MY_BOOK = models.Books()

@app.errorhandler(400)
def bad_request(error):
    '''error handler for Bad request'''
    return jsonify(dict(error='Bad request')), 400
@app.errorhandler(404)
def page_not_found(error):
    '''error handler for 404'''
    return jsonify(dict(error='Page not found')), 404

@app.errorhandler(405)
def unauthorized(error):
    '''error handler for 405'''
    return jsonify(dict(error='Unauthorized method')), 405

@app.errorhandler(500)
def server_error(error):
    '''error handler for 404'''
    return jsonify(dict(error='Internal server error')), 500

#sent_data = request.get_json(force=True)
@app.route('/')
def hello():
    return jsonify({"msg":"Hello world"})
@app.route('/api/v1/books', methods=['GET', 'POST'])
def books():
    '''endpoint to add book and get all books'''
    if request.method == 'POST':
    #add a book method="POST"
        data = request.get_json()
        if not data:
            return jsonify({"message": "Fields cannot be empty"})
            
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        book_id = data.get('book_id')
        status = data.get('status')

        if status == "available" or status == "unavailable":
            response = jsonify(MY_BOOK.put(title, author, edition, book_id, status))
            response.status_code = 200

            return response

        return jsonify({"message" : "Status has to be either available or unavailable"})
    #get a book method="GET"
    get_books = MY_BOOK.get_all()
    response = jsonify(get_books)
    response.status_code = 200

    return response

@app.route('/api/v1/books/<int:book_id>', methods=['PUT', 'GET', 'DELETE'])
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
        edit_book = models.ALL_BOOKS[book_id]
        data = request.get_json()
        if not data:
            return jsonify({"message": "Fields cannot be empty"})
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        status = data.get('status')
        if title is None:
            title = edit_book["title"]
        if author is None:
            author = edit_book["author"]
        if edition is None:
            edition = edit_book["edition"]
        if status is None:
            status = edit_book["status"]

        response = jsonify(MY_BOOK.edit_book(title, author, edition, book_id, status))
        response.status_code = 200

        return response
  
    #delete a book, method=DELETE
    response = jsonify(MY_BOOK.delete(book_id))
    response.status_code = 200

    return response

#check if jwt token is in blacklist
app.config['JWT_SECRET_KEY'] = 'my-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

BLACKLIST = set()

@jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    '''check if jti(unique identifier) is in black list'''
    jti = decrypted_token['jti']
    return jti in BLACKLIST

MY_USER = models.Users()

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''endpoint to register a user'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})
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
    response.status_code = 201
    return response

@app.route('/api/v1/users/books/<int:book_id>', methods=['POST'])
@jwt_required
def users_books(book_id):
    '''user can borrow a book if logged in'''
    response = jsonify(MY_USER.borrow_book(book_id))
    response.status_code = 200
    return response

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    '''login user by verifying password and creating an access token'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})
    username = data.get('username')
    password = data.get('password')
    auth = MY_USER.verify_password(username, password)

    if auth == "True":
        access_token = create_access_token(identity=username)
        return jsonify(dict(token = access_token, message = "Login successful"))

    response = jsonify(auth)
    response.status_code = 401
    return response

@app.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout():
    '''logout user by revoking password'''
    json_token_identifier = get_raw_jwt()['jti']
    BLACKLIST.add(json_token_identifier)
    return jsonify({"message": "Successfully logged out"}), 200

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    '''reset user password'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})
    username = data.get("username")

    response = jsonify(MY_USER.reset_password(username))
    response.status_code = 200
    return response

#method to run app.py
if __name__ == '__main__':
    app.run(debug=True)
