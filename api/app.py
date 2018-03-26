#app.py
from flask import Flask, request, jsonify

from models import Books, Users  

app = Flask(__name__, instance_relative_config=True)
app.config["TESTING"] = True

book = Books()


@app.route('/books', methods=['POST', 'GET'])
def put_and_get_books():
    #add a book method="POST"
    if request.method == 'POST':
        title = str(request.form.get('title'))
        author = str(request.form.get('author'))
        book_id = str(request.form.get('book_id'))

        #book = Books()
        book.put(title, author, book_id)
        response = jsonify({"book_id" : book_id, "title" : title, "author" : author})                
        response.status_code = 200

        return response
        
    #get a book method="GET"    
    else:
        all_books = book.get_all()

        results = []
            
        for i in all_books:
                
            for j in all_books[i]:
                obj = {"title" : j,
                "author" : all_books[i][j]
                    }                                   
                    #append obj to results
                results.append(obj)

        response = jsonify(results)
        response.status_code = 200

        return response

    
@app.route('/books/<book_id>', methods=['PUT', 'GET', 'DELETE'])
def book_modification(book_id):                
        
    if request.method == 'GET':
    #get a book by its id        

            
            
        try:
            my_book = book.get_single_book(book_id)
            results = []

            for i in my_book:
                obj={
                    'title' : i,
                    'author' : my_book[i]
                    }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

        except KeyError:
            response = jsonify({'message': 'item not found'})
            response.status_code = 404
            return response
         


    elif request.method =='PUT':
    #modify or edit a book
        title = str(request.form.get('title',''))
        author = str(request.form.get('author', ''))
           
        book.edit_book(title,author, book_id)
        response = jsonify({"book_id": book_id, "title" : title, "author" : author})                
        response.status_code = 200

        return response

    else:
    #delete a book, method=DELETE            
        book.delete(book_id)
        msg = ("book {} deleted successfully".format(book_id))
        response = jsonify({"message": msg})
        response.status_code = 200
        return(response)

if __name__ == '__main__':
    app.run(debug=True)           
            
        
    



'''

    @app.route('/users/books/<book_id>')
    def borrow_book():


    @app.route('/auth/register')
  
    @app.route('/auth/login')

    @app.route('/auth/logout')

    @app.route('/auth/reset-password')'''




