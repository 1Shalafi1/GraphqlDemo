from typing import List

from pydantic import BaseModel

from app.schemas.address import Address
from app.schemas.book import Book
from app.schemas.user import User


class LibraryBase(BaseModel):
    name: str
    address: Address
    capacity: int


class LibraryCreate(LibraryBase):
    pass


class Library(LibraryBase):
    books: List[Book]
    workers: List[User]

    class Config:
        orm_mode = True
