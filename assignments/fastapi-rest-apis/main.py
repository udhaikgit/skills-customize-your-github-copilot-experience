from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int = Field(ge=0)


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "publication_year": 1937},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "publication_year": 1962},
}

# Add the GET, POST, PUT, and DELETE endpoints described in the assignment.