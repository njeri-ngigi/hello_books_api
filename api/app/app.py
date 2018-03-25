#app.py
from flask import Flask, request, jsonify, abort
from models import Books, Users
import json

def create_app():   
    app = Flask(__name__, instance_relative_config=True)
    app.config["TESTING"] = True

    book = Books()

    @app.route('/books', methods=['POST', 'GET'])
    def put_and_get_books():
        #add a book method="POST"
        if request.method == 'POST':
            title = str(request.form.get('title'))
            author = str(request.form.get('author'))

            #book = Books()
            book.put(title, author)
            response = jsonify({"title" : title, "author" : author})                
            response.status_code = 200

            return response
        
        #get a book method="GET"    
        else:
            all_books = book.get_all()

            results = []
            for i in all_books:
                obj = {
                    'title' : i,
                   'author' : all_books[i]
                    }
                #append obj to results
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200

            return response

    return app
'''
    @app.route('/books/<book_id>', methods=['PUT', 'GET', 'DELETE'])
    def modify_books():
        if request.method == 'PUT':

        else if request.method =='GET':

        else:

    @app.route('/users/books/<book_id>')
    def borrow_book():


    @app.route('/auth/register')
  
    @app.route('/auth/login')

    @app.route('/auth/logout')

    @app.route('/auth/reset-password')  '''


