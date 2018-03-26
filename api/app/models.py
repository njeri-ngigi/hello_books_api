
class Books():
    def __init__(self):
        
        self.books = {}
        
		

    #retrieve all books
    def get_all(self):
        return self.books


    def get_single_book(self, id):
    	return (self.books[id])

    #add a book or modify a book
    def put(self, title, author, id):
        
        book = {title:author}
        self.books[id] = book
		
        return (self.books[id])
    
    #delete a book  
    def delete(self, id):
   
        del self.books[id]
        
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