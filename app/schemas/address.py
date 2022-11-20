import datetime

from pydantic import BaseModel


class AddressBase(BaseModel):
    country: str
    city: str
    postal_code: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    street: str

    class Config:
        orm_mode = True
