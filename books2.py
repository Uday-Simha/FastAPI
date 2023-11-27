from typing import Optional
from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from starlette import status
app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date:int
    
    
    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date
        
class BookRequest(BaseModel):
    id:Optional[int]=None
    title:str=Field(min_length=3)
    author:str=Field(min_lenth=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
    published_date:int=Field(gt=1999,lt=2031)
    
    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date':2029
            }
        }

    
    


BOOK=[
    Book(1,'computer science','charles','it is a very nice book',5,2003),
    Book(2,'science','robert','it is a  nice book',5,2005),
    Book(3,'physics','newton','it is a awesome book',4,2000),
    Book(4,'hp 1','author 1','good book',3,2008),
    Book(5,'hp 2','author 2','good book',4,2020),
    Book(6,'hp 3','author 3','good book',1,2022)
]


@app.get("/book", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOK

@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id:int=Path(gt=0)):
    for book in BOOK:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404,detail='items not found')
        
        
@app.get("/book/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating:int=Query(gt=0,lt=6)):
    book_to_return=[]
    for book in BOOK:
        if book.rating==book_rating:
            book_to_return.append(book)
    return book_to_return

@app.get("/book/publish/", status_code=status.HTTP_200_OK)
async def read_book_published_date(published_date:int=Query(gt=1999,lt=2031)):
    book_to_return=[]
    for book in BOOK:
        if book.published_date==published_date:
            book_to_return.append(book)
    return book_to_return


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.dict())
    print(type(new_book))
    BOOK.append(find_book_id(new_book))
    
def find_book_id(book:Book):
    '''if(len(BOOK)>0):
        book.id=BOOK[-1].id+1
    else:
        book.id=1'''
    book.id=1 if len(BOOK)==0 else BOOK[-1].id+1
    return book

@app.put("/book/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed=False
    for i in range (len(BOOK)):
        if BOOK[i].id==book.id:
            BOOK[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail='item not found')
            
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int=Path(gt=0)):
    book_changed=False
    for i in range (len(BOOK)):
        if BOOK[i].id==book_id:
            BOOK.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code=404,detail='item not found')
        
