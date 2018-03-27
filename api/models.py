from flask import jsonify

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









#create an object User with name, username, email, phone and password
#attributes set which are then added to a dictionary called all_books
users = {}
class Users():
    def __init__(self):
        
        self.user = {}
        
    def show_all_users(self):
        return users

    def put(self, name, username, email, phone, password):
        
        self.user["name"] = name
        self.user["email"] = email
        self.user["phone"] = phone
        self.user["password"] = password



        users[username] = self.user
        return ({username : users[username]})

    def verify_password(self, username, password):
        answer = (username in users)

        if answer==True:
            if ((users[username]["password"]) == password):
                return ({"message":"Successfully logged in"})
                
            else:
                return ({"message":"Password is incorrect"})
                

        else:

            return ({"message":"username not found"})
        

    def borrow_book(self, book_id):
        answer = book_id in all_books
        if (answer == True):
            all_books[book_id]["copies"] -= 1
            if (all_books[book_id]["copies"] == 0):
                del all_books[book_id]
            return ({"message":"Book successfully checked out"})
        else:
            return ({"message":"Book not found"})

u = Users()
u.put("Njeri Ngigi", "njeri-ngigi", "abc@d.com", "07XX", "1234")
