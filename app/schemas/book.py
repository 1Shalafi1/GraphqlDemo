import datetime
import decimal

from pydantic import BaseModel


class BookBase(BaseModel):
    email: str
    title: str
    authors: str
    publishers: str
    
    release: str
    
    isbn: str
    publication_date: str

    price: decimal.Decimal


class BookCreate(BookBase):
    pass


class Book(BookBase):
    pass

    class Config:
        orm_mode = True
