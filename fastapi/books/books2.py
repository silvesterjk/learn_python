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
from pydantic import BaseModel

app = FastAPI()

class BookRequest(BaseModel):
    id: int
    title: str 
    author: str
    description: Optional[str] = None
    category: str

    # Constructor
    def __init__(self, id, title, author, description=None, category=None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.category = category

# Create a list of books
BOOKS = [
    BookRequest(id=1, title="Title One", author="Author One", description="Amazing work",category="history"),
    BookRequest(id=2, title="Title Two", author="Author Two", category="science"),
    BookRequest(id=3, title="Title Three", author="Author Three", category="fiction"),
    BookRequest(id=4, title="Title Four", author="Author Four", category="history"),
    BookRequest(id=5, title="Title Five", author="Author Five", category="science"),
    BookRequest(id=6, title="Title Six", author="Author Six", category="fiction"),
    BookRequest(7, "Title Seven", "Author Seven", "Great work", "history")
]

@app.get("/get_books")
async def get_all_books():
    return BOOKS

@app.post("/get_books/create_book")
async def create_book(book_request = Body()): # Instead of Book = Body(...) we could also use Body() with a type hint
    BOOKS.append(book_request)
    return book_request

@app.post("/add_books")
async def add_books():
    ...