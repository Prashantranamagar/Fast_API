from fastapi import FastAPI
app = FastAPI()  # Create an instance of FastAPI

DUMMY_BOOKS = [
    {
        "title": "Whispers of the Dusk",
        "author": "Elena Rivers",
        "category": "Fantasy",
        "year": 2018,
        "isbn": "978-1-4028-9462-1"
    },
    {
        "title": "Quantum Abyss",
        "author": "Dr. Mark Holloway",
        "category": "Science Fiction",
        "year": 2020,
        "isbn": "978-0-316-03415-2"
    },
    {
        "title": "The Mindful Warrior",
        "author": "Aisha Tanaka",
        "category": "Self-Help",
        "year": 2022,
        "isbn": "978-1-250-12036-3"
    },
    {
        "title": "Beneath the Cypress",
        "author": "Thomas G. Everett",
        "category": "Historical Fiction",
        "year": 2016,
        "isbn": "978-0-345-42321-7"
    },
    {
        "title": "Pixels and Paradoxes",
        "author": "Liam K. Chen",
        "category": "Technology",
        "year": 2021,
        "isbn": "978-1-9848-2945-0"
    },
    {
        "title": "Lost in Kathmandu",
        "author": "Ravi Thapa",
        "category": "Adventure",
        "year": 2019,
        "isbn": "978-1-4197-5206-5"
    },
    {
        "title": "Gardens of Serenity",
        "author": "Ravi Thapa",
        "category": "Adventure",
        "year": 2015,
        "isbn": "978-1-4516-2606-9"
    },
    {
        "title": "Echoes of Empire",
        "author": "Julian Marsh",
        "category": "Thriller",
        "year": 2023,
        "isbn": "978-0-679-40322-1"
    },
    {
        "title": "Binary Souls",
        "author": "Nina Patel",
        "category": "Cyberpunk",
        "year": 2020,
        "isbn": "978-0-7432-7356-0"
    },
    {
        "title": "The Artisan’s Notebook",
        "author": "Carlos Mendoza",
        "category": "Biography",
        "year": 2017,
        "isbn": "978-0-0611-2534-3"
    }
]



@app.get("/books")
async def books():
    return DUMMY_BOOKS

@app.get("/books/my_book")
async def dyanamic_books(): 
    return {"my_book":"My new book"}

@app.get("/books/{dynamic_param}")
async def dyanamic_books(dynamic_param: str):
    return {"dyanamic_books":dynamic_param}

# @app.get("/books/my_book")
# async def dyanamic_books(): 
#     """ 
#     this execute the dynamic_books function because the 
#     path matches and the function work in chronological order
#     for this to work the function must be placed before the default books function
#     """
#     return {"my_book":"My new book"}

#############################################
#### PATH PARAMETERS
# Dynamic path parameters allow you to create endpoints that can accept variable inputs.
#  Spaces in a request parameter is defined as %20 in the URL.
############################################

@app.get("/books/search-books/{dynamic_param}")
async def dyanamic_books(dynamic_param: str):
    """
    Dynamic endpoint that returns a book based on the provided parameter.
    """
    for books in DUMMY_BOOKS:
        # if dynamic_param.casefold() == books["title"].casefold():
        if dynamic_param.casefold() in books["title"].casefold():
            return books
    return {"message": "Book not found"}


#############################################
#### QUERY PARAMETERS ####
# Query parameters are request parameter that are attached after a ?
# Query parameter have name = value pairs
# Example 172.0.0.1:8000/books/?category=math
############################################

@app.get("/query-books/")
async def query_books(category: str = None, author: str = None):
    """
    Returns books filtered by category and/or author.
    If no parameters are provided, returns all books.
    """
    if category:
        filtered_books = [book for book in DUMMY_BOOKS if book["category"].casefold() == category.casefold()]
        if not filtered_books:
            return {"message": "No books found in this category"}
        return filtered_books

    if author:
        filtered_books = [book for book in DUMMY_BOOKS if book["author"].casefold() == author.casefold()]
        if not filtered_books:
            return {"message": "No books found by this author"}
        return filtered_books

    return DUMMY_BOOKS


@app.get("/paramsandquery/{author}/")
async def paramandquery(author: str, category: str):
    book_list = []
    for book in DUMMY_BOOKS:
        if author.casefold() == book["author"].casefold() and \
        category.casefold() == book["category"].casefold():
            book_list.append(book)
    return book_list
        
@app.post("/books/")
async def create_book(book: dict):
    print(book)
    # print(DUMMY_BOOKS)
    DUMMY_BOOKS.append(book)
    print(DUMMY_BOOKS)
    

@app.put("/book/updatebook/")
async def update_book(book: dict):
    # for index , value in enumerate(DUMMY_BOOKS):
    #     if value["title"].casefold() == book["title"].casefold():
    #         DUMMY_BOOKS[index] = book
    #         return {"message": "Book updated successfully"}
    for i in range(len(DUMMY_BOOKS)):
        # if DUMMY_BOOKS[i]["title"].casefold() == book["title"].casefold(): 
        if DUMMY_BOOKS[i].get("title").casefold() == book["title"].casefold():

            DUMMY_BOOKS[i] = book
            return {"message": "Book updated successfully"}
        

@app.delete("/book/deletebook/")
async def delete_book(book):
    for index, value in enumerate(DUMMY_BOOKS):
        if value["title"].casefold() == book.casefold():
            del DUMMY_BOOKS[index]
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}



"""
Pydantics
library that is used for data modeling and data parsing and have effecient error handaling.
commanly used with FastAPI to validate rIn FastAPI, Path is used to validate and document path parameters — the variables you include in your URL route like /users/{user_id}.equest bodies and query parameters.

We will be implementing
Creates different request model for data validation
Field data validation on each variable.

Field is used with Pydantic models to add metadata, validations, defaults, and Swagger documentation for each field in the model.

In FastAPI, Path is used to validate and document path parameters — the variables you include in your URL route like /users/{user_id}.

In FastAPI, Query() is used to explicitly declare and validate query parameters — the values sent in the URL after the ? symbol.

Status codes
1XX --> Request Processing
2XX --> Request Successfully complete  200 --> OK, 201 --> Created, 204 --> No Content
3XX --> Redirection?Futher action must be complete
4XX --> Client Error 400 --> Bad Request, 401 --> Unauthorized, 403 --> Forbidden, 404 --> Not Found, 422 --> Unprocessable Entity
5XX --> Server Error 500 --> Internal Server Error, 502 --> Bad Gateway, 503 --> Service Unavailable

In FastAPI, an HTTPException is used to manually return an HTTP error response when something goes wrong 
— like unauthorized access, not found, or bad input.

Explicit Status code response
In FastAPI, you can explicitly define the HTTP status code that a route should return using:
The status_code parameter in route decorators
Response objects like JSONResponse or Response
"""