'''app.py'''
import re
from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
import models

app = Flask(__name__)
app.config["TESTING"] = True
app.url_map.strict_slashes = False

MY_BOOK = models.Books()
MY_USER = models.Users()

app.config['JWT_SECRET_KEY'] = 'my-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)
BLACKLIST = set()

'''Error handlers'''
@app.errorhandler(400)
def bad_request(error):
    '''error handler for Bad request'''
    return jsonify(dict(error = 'Bad request')), 400
@app.errorhandler(404)
def page_not_found(error):
    '''error handler for 404'''
    return jsonify(dict(error = 'Page not found')), 404

@app.errorhandler(405)
def unauthorized(error):
    '''error handler for 405'''
    return jsonify(dict(error = 'Method not allowed')), 405

@app.errorhandler(500)
def server_error(error):
    '''error handler for 404'''
    return jsonify(dict(error = 'Internal server error')), 500

@app.route('/')
def home():
    '''method to render documentation'''
    return render_template('documentation.html')

'''user actions'''
@jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    '''check if jti(unique identifier) is in black list'''
    json_token_identifier = decrypted_token['jti']
    return json_token_identifier in BLACKLIST

@app.route('/api/v1/auth/register', methods = ['POST'])
def register():
    '''endpoint to register a user'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})
    username = (data.get('username')).strip(' ')
    name = (data.get('name')).strip(' ')
    email = (data.get('email')).strip(' ')
    password = (data.get('password')).strip(' ')
    confirm_password = (data.get('confirm_password')).strip(' ')

    if username is None or not username:
        return jsonify({"message": "Enter username"})
    if name is None or not name:
        return jsonify({"message":"Enter name"})
    
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

@app.route('/api/v1/users/books/<int:book_id>', methods = ['POST'])
@jwt_required
def users_books(book_id):
    '''user can borrow a book if logged in'''
    response = jsonify(MY_USER.borrow_book(book_id))
    response.status_code = 200
    return response

@app.route('/api/v1/auth/login', methods = ['POST'])
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

@app.route('/api/v1/auth/logout', methods = ['POST'])
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


'''Book endpoints'''
@app.route('/api/v1/books', methods = ['GET', 'POST'])
def books():
    '''endpoint to add book and get all books'''
    if request.method == 'POST':
        #add a book method="POST"
        data = request.get_json()
        if not data:
            return jsonify({"message": "Fields cannot be empty"})

        title = (data.get('title')).strip(' ')
        author = (data.get('author')).strip(' ')
        edition = (data.get('edition')).strip(' ')
        book_id = data.get('book_id')
        status = (data.get('status')).strip(' ')

        if title is None or not title:
            return jsonify({"message":"Enter title"})
        if author is None or not author:
            return jsonify({"message":"Enter author"})
        if edition is None or not edition:
            return jsonify({"message":"Enter edition"})
        if book_id is None or not book_id or not isinstance(book_id, int):
            return jsonify({"message":"Enter valid book_id"})
        if status is None or not status:
            return jsonify({"message":"Enter status"})

        if status == "available" or status == "unavailable":
            response = jsonify(MY_BOOK.put(
                title, author, edition, book_id, status))
            response.status_code = 200

            return response

        return jsonify({"message": "Status has to be either available or unavailable"})
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
        try:
            edit_book = models.ALL_BOOKS[book_id]

            data = request.get_json()
            if not data:
                return jsonify({"message": "All fields cannot be empty enter a field to change"})

            title = data.get('title')
            author = data.get('author')
            edition = data.get('edition')
            status = data.get('status')
                
            if not title:
                title = edit_book["title"]
            if not title.strip():
                    return {"message":"Enter valid data"}
            if not author:
                author = edit_book["author"]
            if not edition:
                edition = edit_book["edition"]
            if not status:
                status = edit_book["status"]

            response = jsonify(MY_BOOK.edit_book(
                title, author, edition, book_id, status))
            response.status_code = 200

            return response
        except KeyError:
            return jsonify({"message":"Book you are trying to edit doesn't exist"})

    #delete a book, method=DELETE
    response = jsonify(MY_BOOK.delete(book_id))
    response.status_code = 200

    return response
#method to run app.py
if __name__ == '__main__':
    app.run(debug=True)
