#encoding:utf-8

from db import DB



class User (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Author (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Publisher (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Book (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class User_book (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Book_author (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Book_publisher (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

class Article (DB):
    def __init__ (self, table_name):
        DB.__init__(self, table_name)

        


user = User('user')

author = Author('author')

publisher = Publisher('publisher')

book = Book('book')

user_book = User_book('user_book')

book_author = Book_author('book_author')

book_publisher = Book_publisher('book_publisher')

article = Article('article')



if __name__=="__main__":
    pass