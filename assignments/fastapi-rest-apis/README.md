# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a small REST API with FastAPI and practice how to create routes, validate data, and return consistent JSON responses.

## 📝 Tasks

### 🛠️	Set Up the API Structure

#### Description
Use the starter code to create a FastAPI application for managing a small collection of books. Your API should define a data model, start the application successfully, and expose a welcome route that confirms the service is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance in starter-code.py.
- Define a Book model with at least id, title, author, and year fields.
- Add a GET / route that returns a JSON message such as {"message": "Books API is running"}.
- Start successfully with uvicorn and show the automatic docs at /docs.


### 🛠️	Implement REST Endpoints

#### Description
Expand the API so users can create, view, update, and delete books from an in-memory collection. Make sure each endpoint returns clear JSON data and handles missing records correctly.

#### Requirements
Completed program should:

- Add a GET /books endpoint that returns all books.
- Add a GET /books/{book_id} endpoint that returns one book or an error message when the book does not exist.
- Add a POST /books endpoint that accepts a new book and stores it in memory.
- Add a PUT /books/{book_id} endpoint to update an existing book.
- Add a DELETE /books/{book_id} endpoint to remove a book and confirm the deletion in the response.
