
all_books = {}
def get_all_books_for_test_model():
    return all_books

class Books():
    def __init__(self):
        
        self.book = {}

    #retrieve all all_books
    def get_all(self):
        return all_books


    def get_single_book(self, book_id):
    	return (all_books[book_id])

    #add a book 
    def put(self, title, author, edition, copies, book_id):
        
        self.book["title"] = title
        self.book["author"] = author
        self.book["edition"] = edition
        self.book["copies"] = copies

        all_books[book_id] = self.book
		
        return (all_books[book_id])

    #edit a book
    def edit_book(self, title, author, edition, copies, book_id):
        self.book["title"] = title
        self.book["author"] = author
        self.book["edition"] = edition
        self.book["copies"] = copies

        all_books[book_id] = self.book
        return (all_books[book_id])


    #delete a book  
    def delete(self, book_id):
   
        del all_books[book_id]
        
        return (all_books)

b = Books()
b2 = Books()
b3 = Books()
b4 = Books()
b.put("Tiny Stone", "Martha Mackenzie", "1st", 35 ,1)
b2.put("Fly away birdie", "Marietta Gonzalez", "1st", 4 ,2)
b3.put("Go home, Susan", "Barry White", "1st", 21 ,3)
b4.put("Dunia haina huruma", "Kung'u Kahiga", "1st", 12 ,4)









#create an object User with itle and author 
#attributes set which are then added to a dictionary called all_books
class Users():
    def __init__(self):
        self.username = ""
        self.email = ""
        self.password = ""
        self.users = {}
        
    def put(self, username, email, password):
        self.users[username] = [email, password]
        return ({username : self.users[username]})