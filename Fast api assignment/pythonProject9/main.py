from fastapi import FastAPI

from scripts.core.services.books_services import app as book
import uvicorn

app = FastAPI()
app.include_router(book)


if __name__ == "main__":
    uvicorn.run("main:app")
