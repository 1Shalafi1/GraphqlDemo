from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session as DbSession, Load


class AbstractModel:
    """
    Abstract class for our models which standard implementation
    """
    @classmethod
    def __get_id_field(cls):
        primary_key = inspect(cls).primary_key[0]
        return primary_key


    @classmethod
    def get_filtered(cls, db: DbSession, skip=0, limit=10, **filters):
        query = db.query(cls).filter_by(**filters).offset(skip).limit(limit)
        return query.all()

    @classmethod
    def create(cls, db: DbSession, data):
        new_obj = cls(
            **data.dict(),
            last_update=datetime.utcnow(),
        )
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)

        return new_obj

    @classmethod
    def get_list(cls, db: DbSession, limit: int = 10, skip: int = 0):
        return db.query(cls).offset(skip).limit(limit).all()

    @classmethod
    def get_list_by_id(cls, db: DbSession, ids: List[int]):
        return db.query(cls).filter(cls.__get_id_field().in_(ids))

    @classmethod
    def get_by_id(cls, db: DbSession, _id: int):
        return db.query(cls).filter(cls.__get_id_field() == _id).first()

    @classmethod
    def update(cls, db: DbSession, _id: int, data):
        db_object = cls.get_by_id(db=db, _id=_id)
        if not db_object:
            raise HTTPException(status_code=404, detail='Address not found')

        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_object, key, value)
        db_object.last_update = datetime.utcnow()
        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object