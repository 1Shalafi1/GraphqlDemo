import datetime

from pydantic import BaseModel


class PublisherBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    self_publishing: bool


class PublisherCreate(PublisherBase):
    pass


class Publisher(PublisherBase):
    pass

    class Config:
        orm_mode = True