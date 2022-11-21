from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session as DbSession


class AbstractModel:
    """
    Abstract class for our models which standard implementation
    """
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
    def get_list(cls, db: DbSession, limit: int = 10, skip: int = 0, **filters):
        return db.query(cls).offset(skip).limit(limit).all()

    @classmethod
    def get_single(cls, db: DbSession, **filters):
        # I HAVE TO ADD DYNAMIC FILTERING

        clauses = []
        for k, v in filters.items():
            clauses.append((getattr(cls, k), '==', v))
        ####
        from pprint import pprint
        import pydevd_pycharm
        pydevd_pycharm.settrace('192.168.0.136', port=2137, stdoutToServer=True, stderrToServer=True)
        ####
        return db.query(cls).filter(clauses).first()

    @classmethod
    def update(cls, db: DbSession, obj_id: int, data):
        db_object = cls.get_by_id(db=db, obj_id=obj_id)
        if not db_object:
            raise HTTPException(status_code=404, detail=f'{cls.__name__} not found')

        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_object, key, value)
        db_object.last_update = datetime.utcnow()
        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object
