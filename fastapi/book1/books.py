from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/api-get")
async def first_api():
    return {"data": "Next API"}

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Seven', 'author': 'Author Three', 'category': 'history'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

"""PATH PARAMETERS"""
# Get a specific book using path parameters
# The path parameter is the book title
# The path parameter is passed to the function as an argument
# The function returns the book with the title that matches the path parameter

# http://0.0.0.0:8000/ -> This is the base URL
# books -> This is the path
# Title One -> This is the path parameter (book title)

# Dynamic path parameters
# Get all books from a specific category using path parameters

@app.get("/books")
async def read_book():
    return BOOKS

@app.get("/parama_books/{dynamic_parameter}")
async def parama_read_books(dynamic_parameter: str):
    return {'books_to_return': dynamic_parameter}

# ___________________________________________________

# The order of the path parameters matters
# Get all books from a specific category and author using path parameters

@app.get("/books/category/{category}")
async def read_category(category: str):
    """
    1. The path parameter is the category
    2. The path parameter is passed to the function as an argument
    3. The function returns all the books with the category that matches the path parameter
    4. The function returns a list of books with the category that matches the path parameter
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/category/horror")
async def read_category():
    return {"data": "Horror"}
# ^ The above path will not work because the path parameters are not in the correct order. 
# @app.get("/books/category/{category}") will not work because the path parameters are not in the correct order.

# %20 is the URL encoding for a space character
# http://0.0.0.0:8000/books/category/science/author/Author%20One -> This is the URL
# science -> This is the category path parameter
# Author One -> This is the author path parameter

# Get all books from a specific category and author using path parameters
@app.get("/books/category/{category}/author/{author}")
async def read_category_author(category: str, author: str):
    """
    1. The path parameters are the category and the author
    2. The path parameters are passed to the function as arguments
    3. The function returns all the books with the category and author that match the path parameters
    4. The function returns a list of books with the category and author that match the path parameters
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return