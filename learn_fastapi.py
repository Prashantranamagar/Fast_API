from fastapi import FastAPI
app = FastAPI()

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
        "author": "Maya Bloom",
        "category": "Poetry",
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