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

@app.get("/books/category/{category}")
async def read_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

"""
# The order of the path parameters matters
# Get all books from a specific category and author using path parameters
@app.get("/books/category/horror")
async def read_category():
    return {"data": "Horror"}
# ^ The above path will not work because the path parameters are not in the correct order. 
# @app.get("/books/category/{category}") will not work because the path parameters are not in the correct order.
"""
# %20 is the URL encoding for a space character
# http://0.0.0.0:8000/books/category/science/author/Author%20One -> This is the URL
# science -> This is the category path parameter
# Author One -> This is the author path parameter

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold(): # casefold() is used to make the comparison case-insensitive
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.delete("/books/delete_books/")
async def delete_books_by_category(category: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('category').casefold() == category.casefold():
            BOOKS.pop(i)
            break
            