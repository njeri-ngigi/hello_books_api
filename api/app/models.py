
class Books():
    def __init__(self):
        self.title = ""
        self.author = ""
        self.books = {}
		


    def get(self):
        return self.books

    def put(self, title, author):
        self.title = title
        self.author = author
        self.books[self.title] = self.author
		
        return ({title:author})
        
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