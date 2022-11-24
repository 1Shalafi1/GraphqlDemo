import json
from typing import Optional, List

from fastapi import HTTPException
from sqlalchemy import Integer, Column, String, TIMESTAMP, Index
from sqlalchemy.orm import Session as DbSession, relationship

from app.database.base import Base
from app.database.models.__relations_tables import film_actor
from app.database.models.base import AbstractModel
from app.database.models.film import Film
from app.schema.film import FilmInput


class Actor(Base, AbstractModel):
    __tablename__ = 'actor'
    __table_args__ = (
        Index('actor_pkey', "actor_id"),
        Index('idx_actor_last_name', "last_name"),
    )

    actor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    last_update = Column(TIMESTAMP)

    films = relationship('Film', secondary=film_actor, lazy='subquery', back_populates='actors')

    @classmethod
    def add_actor_films(cls, db: DbSession, actor_id, films_data: Optional[List[FilmInput]] = None,
                        films_ids: List[int] = None):

        if not (films_ids or films_data):
            raise HTTPException(status_code=400, detail='New films object or films ids are required')

        films_data = [] if films_data is None else films_data
        films_ids = [] if films_ids is None else films_ids

        db_object = cls.get_by_id(db, actor_id)
        if not db_object:
            raise HTTPException(status_code=404, detail='Actor not found')

        errors = []
        films = []

        for film in films_data:
            try:
                films.append(Film.create(db, film))
            except Exception as err:
                errors.append({'object': film, 'details': str(err)})

        if errors:
            raise HTTPException(status_code=400, detail=json.dumps(errors))

        if films_ids:
            films.extend(Film.get_list_by_id(db, films_ids))

        db_object.films = films
        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object
