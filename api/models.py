
class Books():
    def __init__(self):
        
        self.books = {}
        
		

    #retrieve all books
    def get_all(self):
        return self.books


    def get_single_book(self, book_id):
    	return (self.books[book_id])

    #add a book 
    def put(self, title, author, book_id):
        
        book = {title:author}
        self.books[book_id] = book
		
        return (self.books[book_id])

    #edit a book
    def edit_book(self, title, author, book_id):
        book = {title : author}
        self.books[book_id] = book
        return (self.books[book_id])


    #delete a book  
    def delete(self, book_id):
   
        del self.books[book_id]
        
        return (self.books)

#create an object User with itle and author 
#attributes set which are then added to a dictionary called books
class Users():
    def __init__(self):
        self.username = ""
        self.email = ""
        self.password = ""
        self.users = {}
        
    def put(self, username, email, password):
        self.users[username] = [email, password]
        return ({username : self.users[username]})