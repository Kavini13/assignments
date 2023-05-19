from pydantic import BaseModel


class Book(BaseModel):
    book_id: int
    title: str
    author: str
    description: str
    quantity: int
    price: int


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
