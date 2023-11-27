from fastapi import Body, FastAPI
from pydantic import BaseModel
app=FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]



@app.get("/books", tags=["book1"])
async def read_all_books():
    return BOOKS

#

@app.get("/books/{book_title}", tags=["book1"])
async def read_all_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
        
@app.get("/books/")      
async def read_category_by_book(category:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.get("/books/{book_author}/", tags=["book1"])
async def read_book_author_category_by_book(book_author:str,category:str):
    book_to_return=[]
    for book in BOOKS:
        if (book.get('author').casefold()==book_author.casefold() and
        book.get('category').casefold()==category.casefold()):
            book_to_return.append(book)
    return book_to_return


@app.post("/books/create_book", tags=["book1"])
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    
@app.put("/books/update_book", tags=["book1"])
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book
            
@app.delete("books/delete_book/{book_title}", tags=["book1"])
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
           BOOKS.pop(i)
           break
       
       
@app.get("/books/byauthor/", tags=["book1"])
async def read_books_by_author(book_author:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold():
            book_to_return.append(book)
    return book_to_return
       
class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    description:str
    rating:int


BOOKS1=[
    Book(1,'computer science','charles','it is a very nice book',5),
    Book(2,'science','robert','it is a  nice book',5),
    Book(3,'physics','newton','it is a awesome book',4),
    Book(4,'hp 1','author 1','good book',3),
    Book(5,'hp 2','author 2','good book',2),
    Book(6,'hp 3','author 3','good book',1)
]


@app.get("/book")
async def read_all_books():
    return BOOKS1

@app.post("/create_book")
async def create_book(book_request=BookRequest):
    new_book=Book(**book_request.dict())
    print(type(new_book))
    BOOKS1.append(new_book)