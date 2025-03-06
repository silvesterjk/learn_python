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
* Optional variables need a =None example: id: Optional[int] = None
"""

from fastapi import FastAPI, Body, HTTPException
from typing import Optional, List

app = FastAPI()

# Create a list of books
BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "history"},
    {"title": "Title Two", "author": "Author Two", "category": "fiction"},
    {"title": "Title Three", "author": "Author Three", "category": "science"},
    {"title": "Title Four", "author": "Author Four", "category": "biography"},
    {"title": "Title Five", "author": "Author Five", "category": "history"},
    {"title": "Title Six", "author": "Author Six", "category": "fiction"},
    {"title": "Title Seven", "author": "Author Seven", "category": "science"}
]

@app.get("/get_books")
async def get_all_books():
    return BOOKS