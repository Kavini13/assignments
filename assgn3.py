from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
database = client.interns_b2_23

Books = database.exciting_books


# Define a Pydantic model for the book
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    price: int
    published_date: int
    publisher: str


# Define an array to store the books

books = []


# Add a new book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book


# Endpoint to get  all books
@app.get("/books", response_model=List[Book])
def read_books():
    return books


# Endpoint to get a specific book by ID
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books:
        if book_id == book.id:
            return book


@app.put("/books/{books_id}")
def update_book(book_id: int, book: Book):
    for index, stored_book in enumerate(books):
        if book_id == stored_book.id:
            books[index] = book
            return {"message": "Book deleted Successfully"}
        else:
            print("Book not found")


# Endpoint to delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, stored_book in enumerate(books):
        if book_id == stored_book.id:
            books.pop(index)
            return {"message": "Book deleted Successfully"}
        else:
            print("Book not found!error")
