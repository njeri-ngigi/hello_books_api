
class Books():
    def __init__(self):
        
        self.books = {}
		

    #retrieve all books
    def get_all(self):
        return self.books


    def get_single_book(self, title):
    	return ({title : self.books[title]})

    #add a book or modify a book
    def put(self, title, author):
        
        self.books[title] = author
		
        return ({title:author})
    
    #delete a book  
    def delete(self, title):
   
        del self.books[title]
        
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