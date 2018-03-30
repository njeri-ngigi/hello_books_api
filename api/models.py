'''models.py containing models for the API'''

ALL_BOOKS = {}

class Books():
    '''create class to represent book model'''
    def __init__(self):
        self.book = {}

    def get_all(self):
        '''return all books from ALL_BOOKS dictionary'''
        return ALL_BOOKS

    def get_single_book(self, book_id):
        '''get single book from ALL_BOOKS using id'''
        if book_id in ALL_BOOKS:

            return ALL_BOOKS[book_id]

        else:
            return {"message":"Book not found"}
 
    def put(self, title, author, edition, copies, book_id):
        '''add a book to ALL_BOOKS'''
        if book_id in ALL_BOOKS:
            return {"message":"Book id entered already exists"}

        else:
            self.book["title"] = title
            self.book["author"] = author
            self.book["edition"] = edition
            self.book["copies"] = copies

            ALL_BOOKS[book_id] = self.book
            return ALL_BOOKS[book_id]

    #edit a book
    def edit_book(self, title, author, edition, copies, book_id):
        '''edit a book by its id'''
        if book_id in ALL_BOOKS:
            self.book["title"] = title
            self.book["author"] = author
            self.book["edition"] = edition
            self.book["copies"] = copies

            ALL_BOOKS[book_id] = self.book
            return ALL_BOOKS[book_id]
        else:
            return {"message":"Book you are trying to edit doesn't exist"}

    def delete(self, book_id):
        '''delete a book by its id'''
        if book_id in ALL_BOOKS:
            del ALL_BOOKS[book_id]
            return {"message":"Book {} deleted successfully".format(book_id)}

        else:
            return {"message":"Book you are trying to delete doesn't exist"}

B = Books()
B2 = Books()
B3 = Books()
B4 = Books()
B.put("Tiny Stone", "Martha Mackenzie", "1st", 35, 1)
B2.put("Fly away birdie", "Marietta Gonzalez", "1st", 4, 2)
B3.put("Go home, Susan", "Barry White", "1st", 21, 3)
B4.put("Dunia haina huruma", "Kung'u Kahiga", "1st", 12, 4)


USERS = {}

class Users():
    '''class to represent users model'''
    def __init__(self):
        self.user = {}

    def show_all_users(self):
        '''retrieve all users from USERS'''
        return USERS

    def put(self, name, username, email, phone, password):
        '''add a user to USERS'''
        self.user["name"] = name
        self.user["email"] = email
        self.user["phone"] = phone
        self.user["password"] = password

        USERS[username] = self.user
        return {username : USERS[username]}

    def verify_password(self, username, password):
        '''verify password'''
        if username in USERS:
            if (USERS[username]["password"]) == password:
                return True
            else:
                return False
        else:
            return "False"
    
    def borrow_book(self, book_id):
        '''borrow a book by book_id'''
        if book_id in ALL_BOOKS:
            return {"message":"Book successfully checked out"}
        else:
            return {"message":"Book not found"}

U = Users()
U.put("Njeri Ngigi", "njeri-ngigi", "abc@d.com", "07XX", "1234")
