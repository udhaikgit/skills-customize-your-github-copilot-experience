# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API in Python with FastAPI, using HTTP methods, Pydantic models, and clear responses to manage a collection of books.

## 📝 Tasks

### 🛠️ List and Retrieve Books

#### Description
Use the provided starter code to create endpoints for listing all books and retrieving one book by its ID. Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the development server with `uvicorn main:app --reload`.

#### Requirements
Completed program should:

- Return the collection of books from `GET /books`
- Return one book from `GET /books/{book_id}`
- Return HTTP 404 when the requested book ID does not exist
- Open `/docs` in a browser to inspect and try the endpoints


### 🛠️ Create and Update Books

#### Description
Add endpoints that accept book data and use a Pydantic model to validate each request. Use the book ID to identify which record to update.

#### Requirements
Completed program should:

- Use the provided `BookCreate` Pydantic model to validate a title, author, and non-negative publication year
- Create a book with `POST /books` and return the created book
- Update a book with `PUT /books/{book_id}`
- Return HTTP 404 when an update targets a book that does not exist


### 🛠️ Delete Books and Check Responses

#### Description
Complete the collection API by adding a delete endpoint. Try valid and invalid requests in `/docs` and check that each response uses an appropriate HTTP status code.

#### Requirements
Completed program should:

- Delete a book with `DELETE /books/{book_id}`
- Return HTTP 404 when a delete targets a book that does not exist
- Return a clear success response after deleting a book
- Confirm that the list and retrieve endpoints reflect created, updated, and deleted books