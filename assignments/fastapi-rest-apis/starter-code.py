from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=2, title="Automate the Boring Stuff with Python", author="Al Sweigart", year=2019),
]


@app.get("/")
def read_root():
    return {"message": "Books API is running"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return {"deleted": deleted_book.id}
    raise HTTPException(status_code=404, detail="Book not found")