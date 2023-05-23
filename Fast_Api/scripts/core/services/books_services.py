from fastapi import APIRouter
from schemas.book_models import Book, Email
from scripts.core.handlers.books_handler import create_book, welcome, read_book, update_book, delete_book, pipe_agg
from scripts.core.handlers.email_handler import send_email

app = APIRouter()


# Add a new book
@app.post("/book")
def func(book: Book):
    return create_book(book)


# welcome message
@app.get("/")
def func():
    return welcome()


# Endpoint to get all books
@app.get("/books_all")
def func():
    return read_book()


# Endpoint to update a book

@app.put("/books/{title}")
def func(title: str, course: Book):
    return update_book(title, course)


# Endpoint to delete a book


@app.delete("/books/{title}")
def func(title: str):
    return delete_book(title)


# Endpoint to send email
@app.post("/send_email")
def fun(email: Email):
    total_amount = pipe_agg()
    return send_email(str(total_amount), email)


# Endpoint to get Total Price
@app.get("/total_price")
def fun():
    return pipe_agg()
