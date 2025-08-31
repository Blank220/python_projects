class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    
    def list_books(self):
        return [f'{book.title} by {book.author}'for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
library = Library('Manila Bulletin')

book1 = Book('The Best of Me', 'Nicholas Sparks')
book2 = Book('48 Laws', 'Robert Greene')
book3 = Book('Jujutsu Kaisen', 'Gege Akutami')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for i,book in enumerate(library.list_books(),start=1):
    print(f'{i}. {book}')

