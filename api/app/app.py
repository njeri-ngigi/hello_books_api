#app.py
'''import Flask module from flask package.
Flask creates instances of web application'''


from flask import request, jsonify, abort
#request for handling request
from flask import Flask
from models import Books, Users
import json

    
app = Flask(__name__, instance_relative_config=True)

book = Books()

@app.route('/books', methods=['POST', 'GET'])
def put_and_get_books():
#add a book method="POST"
    if request.method == 'POST':
        title = request.data.get('title')
        author = request.data.get('author')
        response = book.put(title, author)				
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

    


