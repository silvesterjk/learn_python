"""
1. Data Validation
2. Exception Handling
3. Status Codes
4. Swagger configurations
5. Request Objects
"""


"""
HTTP Request Methods: Comparision between CRUD and HTTP Request Methods
1. GET: To request data from the server. This is similar to the Read operation in CRUD.
2. POST: To submit data to the server. This is similar to the Create operation in CRUD.
3. PUT: To update data on the server. This is similar to the Update operation in CRUD.
4. DELETE: To delete data from the server. This is similar to the Delete operation in CRUD.
"""

"""
Pydantic 1 vs Pydantic 2
Pydantic 2 has made some changes to the library. The three biggest are:
* .dict() function is now renamed to .model_dump()
* schema_extra function within a Config class is now renamed to json_schema_extra
* Optional variables need a = None --> For example: id: Optional[int] = None
"""

from fastapi import FastAPI, Body, HTTPException
from typing import Optional, List
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: Optional[str] = None
    category: Optional[str] = None

    def __init__(self, id: int, title: str, author: str, description: Optional[str] = None, category: Optional[str] = None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.category = category


class BookRequest(BaseModel):
    id: int
    title: str 
    author: str
    description: Optional[str] = None
    category: Optional[str] = None  # Made this optional with default=None

# Create a list of books
BOOKS = [
    BookRequest(id=1, title="Title One", author="Author One", description="Amazing work", category="history"),
    BookRequest(id=2, title="Title Two", author="Author Two", category="science"),
    BookRequest(id=3, title="Title Three", author="Author Three", category="fiction"),
    BookRequest(id=4, title="Title Four", author="Author Four", category="history"),
    BookRequest(id=5, title="Title Five", author="Author Five", category="science"),
    BookRequest(id=6, title="Title Six", author="Author Six", category="fiction"),
    BookRequest(id=7, title="Title Seven", author="Author Seven", description="Great work", category="history")
]

@app.get("/get_books")
async def get_all_books():
    return BOOKS

@app.post("/get_books/create_book")
async def create_book(book_request: BookRequest):  # Use type hint for proper validation
    """
    1. The create_book function is decorated with the @app.post() decorator.
    2. The function takes a single parameter, book_request, which is of type BookRequest.
    3. The function returns a BookRequest object.
    4. The function creates a new Book object using the BookRequest object.
    5. The new Book object is appended to the BOOKS list.
    6. The function returns the created book.
    7. The reason to use Book class instead of BookRequest class is to have a separate class for the request and response objects.
    8. For example, the BookRequest class can have additional fields that are not present in the Book class.
    9. The Book class can have additional fields that are not present in the BookRequest class.
    """
    # print(type(book_request)) # <class 'books2.BookRequest'>
    new_book = Book(**book_request.model_dump())
    print(type(new_book)) # <class 'books2.Book'> | As we are converting the BookRequest to Book
    BOOKS.append(book_request)
    return book_request # Return the created book

@app.get("/get_books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")