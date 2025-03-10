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
    id: Optional[int] = Field(description="Not needed on create", default=None)  # Added Field with description and default=None
    title: str = Field(min_length=1, max_length=100)  # Added Field with min_length and max_length
    author: str = Field(min_length=1, max_length=50)  # Added Field with min_length and max_length
    description: Optional[str] = None # Made this optional with default=None
    category: str = Field(min_length=1, max_length=50)  # Added Field with min_length and max_length
    rating: Optional[int] = Field(ge=1, le=5, default=None)  # Added rating field

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Title One",
                "author": "Author One",
                "description": "Amazing work",
                "category": "history",
                "rating" : 5
            }
        }
    }

# Create a list of books
BOOKS = [
    BookRequest(id=1, title="Title One", author="Author One", description="Amazing work", category="history", rating=5),
    BookRequest(id=2, title="Title Two", author="Author Two", category="science", rating=4),
    BookRequest(id=3, title="Title Three", author="Author Three", category="fiction", rating=3),
    BookRequest(id=4, title="Title Four", author="Author Four", category="history", rating=2),
    BookRequest(id=5, title="Title Five", author="Author Five", category="science", rating=1),
    BookRequest(id=6, title="Title Six", author="Author Six", category="fiction", rating=1),
    BookRequest(id=7, title="Title Seven", author="Author Seven", description="Great work", category="history", rating=2),
    BookRequest(id=8, title="Title Eight", author="Author Eight", category="science", rating=3)
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
    # print(type(new_book)) # <class 'books2.Book'> | As we are converting the BookRequest to Book
    BOOKS.append(find_book_by_id(new_book)) # Append the new book to the BOOKS list
    return book_request # Return the created book

def find_book_by_id(book: Book):
    """
    1. The find_book_by_id function takes a Book object as a parameter.
    2. The function iterates through the BOOKS list.
    3. If the book.id matches the id of a book in the BOOKS list, the function returns the book.
    4. If the book.id does not match the id of any book in the BOOKS list, the function raises an HTTPException with a 404 status code.
    """
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1 # Increment the id by 1 for the new book
    else:
        book.id = 1
    return book

    # We could alternatively use the below code to find the book by id
    # book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

@app.get("/get_books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/get_books/update_book/{book_id}")
async def update_book(book_id: int, book_request: BookRequest):
    for book in BOOKS:
        if book.id == book_id:
            book.title = book_request.title
            book.author = book_request.author
            book.description = book_request.description
            book.category = book_request.category
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/get_books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            deleted_book = BOOKS.pop(index)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")

# Run the application using uvicorn
# uvicorn books2:app --reload
