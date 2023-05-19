from schemas.book_models import Book
from scripts.core.db.mongodb import lib


def create_book(book: Book):
    lib.insert_one(book.dict())
    return {"message": "book created"}


def welcome():
    return {"Welcome to book store"}


def read_book():
    exciting_books = (lib.find())
    new_exciting_books = []
    for harry_potter in exciting_books:
        del harry_potter["_id"]
        new_exciting_books.append(harry_potter)
    return new_exciting_books


def update_book(title: str, course: Book):
    lib.update_one({"title": title}, {"$set": course.dict()})
    return {"message": "Book updated Successfully"}


def delete_book(title: str):
    lib.delete_one({"title": title})
    return {"message": "Book deleted successfully"}


def pipe_agg():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'Total_Price': {
                    '$sum': '$price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]

    data = lib.aggregate(pipeline)
    data = list(data)
    print(data)
    return{"Total_Price": data[0]['Total_Price']}
