#my_app.py

#app.py
from flask import Flask, request, jsonify, json, abort

from models import Books, Users

app = Flask(__name__, instance_relative_config=True)
app.config["TESTING"] = True

my_book = Books()

@app.route('/books', methods=['POST', 'GET'])
def put_and_get_books():
    #add a book method="POST"
    if request.method == 'POST':
        title = str(request.form.get('title',''))
        author = str(request.form.get('author',''))
        edition = str(request.form.get('edition'))
        copies = str(request.form.get('copies'))
        book_id = str(request.form.get('book_id'))

        
        response = jsonify(my_book.put(title, author, edition, copies, book_id))               
        response.status_code = 200

        return response
        
    #get a book method="GET"    
    else:
        get_books = my_book.get_all()
        response = jsonify(get_books) 
        response.status_code = 200

        return response

    
@app.route('/books/<int:book_id>', methods=['PUT', 'GET', 'DELETE'])
def book_modification(book_id):                
        
    if request.method == 'GET':
    #get a book by its id        
            
        try:
            get_book = my_book.get_single_book(book_id)
                                
            response = jsonify(get_book)
            response.status_code = 200
            return response

        except KeyError:
            response = jsonify({'message': 'item not found'})
            response.status_code = 404
            return response
         


    elif request.method =='PUT':
    #modify or edit a book
        title = str(request.form.get('title'))
        author = str(request.form.get('author'))
        edition = str(request.form.get('edition'))
        copies = str(request.form.get('copies'))
           
        response = jsonify(my_book.edit_book(title,author,edition,copies,book_id))
        response.status_code = 200

        return response

    else:
    #delete a book, method=DELETE            
        my_book.delete(book_id)
        msg = ("book {} deleted successfully".format(book_id))
        response = jsonify({"message": msg})
        response.status_code = 200
        return(response)


my_user = Users()



@app.route('/users/books/<int:book_id>', methods=['POST'])
def requires_auth(book_id):
    username = str(request.form.get('username'))
    password = str(request.form.get('password'))

    auth = my_user.verify_password(username, password)

    if auth==True:
        response = jsonify(my_user.borrow_book(book_id))
        response.status_code(200)
        return response

    else:
        return ({"Message": "Authorization failed"})



'''@requires_auth(view_func="requires_auth")   
def borrow_a_book(book_id):
    
    
    '''


'''
@app.route('auth/register', methods=['POST'])
def create_user():

@app.route('auth/login', methods=['POST'])
def login_user():

@app.route('auth/logout', methods=['POST'])
def logout_user():

@app.route('auth/reset-password', methods=['POST'])
def reset_password():'''



if __name__ == '__main__':
    app.run(debug=True)           
            
        
    





