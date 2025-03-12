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

from fastapi import FastAPI, Body, HTTPException, Path, Query
from typing import Optional, List
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: Optional[str] = None
    category: Optional[str] = None
    rating: Optional[int] = None
    published_year: Optional[int] = None

    def __init__(self, id: int, title: str, author: str, 
                 description: Optional[str] = None, 
                 category: Optional[str] = None, 
                 rating: Optional[int] = None, published_year: Optional[int] = None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.category = category
        self.rating = rating
        self.published_year = published_year

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Not needed on create", default=None)  # Added Field with description and default=None
    title: str = Field(min_length=1, max_length=100)  # Added Field with min_length and max_length
    author: str = Field(min_length=1, max_length=50)  # Added Field with min_length and max_length
    description: Optional[str] = None # Made this optional with default=None
    category: str = Field(min_length=1, max_length=50)  # Added Field with min_length and max_length
    rating: Optional[int] = Field(ge=1, le=5, default=None)  # Added rating field
    published_year: Optional[int] = Field(ge=1900, le=2022, default=None)  # Added published_year field

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Title One",
                "author": "Author One",
                "description": "Amazing work",
                "category": "history",
                "rating" : 5,
                "published_year": 2022
            }
        }
    }

# Create a list of books
BOOKS = [
    BookRequest(id=1, title="Title One", author="Author One", description="Amazing work", category="history", rating=5, published_year=2022),
    BookRequest(id=2, title="Title Two", author="Author Two", category="science", rating=4, published_year=2021),
    BookRequest(id=3, title="Title Three", author="Author Three", category="fiction", rating=3, published_year=2020),
    BookRequest(id=4, title="Title Four", author="Author Four", category="history", rating=2, published_year=2019),
    BookRequest(id=5, title="Title Five", author="Author Five", category="science", rating=1, published_year=2018),
    BookRequest(id=6, title="Title Six", author="Author Six", category="fiction", rating=1, published_year=2017),
    BookRequest(id=7, title="Title Seven", author="Author Seven", description="Great work", category="history", rating=2, published_year=2016),
    BookRequest(id=8, title="Title Eight", author="Author Eight", category="science", rating=3, published_year=2015),
]

@app.get("/get_books", status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_books_by_publish_year(publish_year: int = Query(..., description="The year the book was published", gt=1900, le=2022)):
    books_to_return = []
    for book in BOOKS:
        if book.published_year == publish_year:
            books_to_return.append(book)
    return books_to_return

@app.post("/get_books/create_book", status_code=status.HTTP_201_CREATED) # Use status_code to return the status code in the response
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

def find_book_by_id(book: Book, book_id: int = Path(description="The ID of the book you want to get", gt=0)):
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

@app.get("/get_books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(description="The ID of the book you want to get", gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(..., description="The rating of the book you want to get", gt=0, le=5)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/get_books/update_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest, book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            book.title = book_request.title
            book.author = book_request.author
            book.description = book_request.description
            book.category = book_request.category
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/get_books/delete_book/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int = Path(description="The ID of the book you want to delete", gt=0)):
    for index, book in enumerate(BOOKS): # This is to get the index of the book in the list
    # for i in range(len(BOOKS)):
    #     if BOOKS[i].id == book_id:
    #         deleted_book = BOOKS.pop(i)
    #         return deleted_book
        if book.id == book_id:
            deleted_book = BOOKS.pop(index)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")

# Run the application using uvicorn
# uvicorn books2:app --reload

"""
STATUS CODES:

1. 200 OK: The request was successful. --> Common among all the CRUD operations
2. 201 Created: The request was successful, and a new resource was created. --> Common for POST requests
3. 204 No Content: The request was successful, but there is no content to return. --> Common for PUT requests
4. 400 Bad Request: The request was invalid.
5. 401 Unauthorized: The request requires authentication.
6. 403 Forbidden: The request is forbidden.
7. 404 Not Found: The requested resource was not found.
8. 405 Method Not Allowed: The request method is not allowed.
9. 500 Internal Server Error: The server encountered an error.
10. 503 Service Unavailable: The server is unavailable.

In general:
1xx --> Informational responses (e.g., 100 Continue)
2xx --> Success (e.g., 200 OK)
3xx --> Redirection (e.g., 301 Moved Permanently)
4xx --> Client errors (e.g., 400 Bad Request)
5xx --> Server errors (e.g., 500 Internal Server Error)
"""


"""
HTTP Exception Handling:
1. The HTTPException class is used to raise exceptions with a specific status code.
2. The HTTPException class takes two arguments: status_code and detail.
3. The status_code argument is the status code of the exception.
4. The detail argument is a message that describes the exception.
5. The raise statement is used to raise the exception.
6. The raise statement is followed by the HTTPException class and its arguments.
"""

"""
Path Parameters: Path parameters are used to pass data to the server using the URL path.
1. Path parameters are defined in the URL path.
2. Path parameters are enclosed in curly braces {}.
3. Path parameters can have a data type and constraints.
4. Path parameters are passed as arguments to the function.
5. Path parameters are used to get data from the server.

Query Parameters: Query parameters are used to pass data to the server using the URL query string.
1. Query parameters are defined in the URL query string.
2. Query parameters are separated by the ? character.
3. Query parameters are key-value pairs.
4. Query parameters are passed as arguments to the function.
5. Query parameters are used to filter data from the server.
"""

"""
Request Body: The request body is used to send data to the server.
1. The request body is the data sent to the server.
2. The request body is passed to the function as an argument.
3. The request body is used to create new resources.
4. The request body is used to update existing resources.
5. The request body is used to delete resources.
"""