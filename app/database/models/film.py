from sqlalchemy import ForeignKey, VARCHAR, Text, Numeric, String, ARRAY
from sqlalchemy import Integer, Column, TIMESTAMP, Index
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.models.__relations_tables import film_actor, film_category
from app.database.models.base import AbstractModel


class Film(Base, AbstractModel):
    __tablename__ = 'film'
    __table_args__ = (
        Index('film_pkey', 'film_id'),
        Index('film_fulltext_idx', 'fulltext'),
        Index('idx_fk_language_id', 'language_id'),
        Index('idx_title', 'title'),
    )

    film_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    language_id = Column(Integer, ForeignKey('language.language_id', name='film_language_id_fkey'))

    title = Column(VARCHAR(255))
    description = Column(Text)
    release_year = Column(TIMESTAMP)
    rental_duration = Column(Integer)
    rental_rate = Column(Numeric)
    length = Column(Integer)
    replacement_cost = Column(Numeric)
    rating = Column(Text)
    special_features = Column(ARRAY(String))
    fulltext = Column(String)

    last_update = Column(TIMESTAMP)

    actors = relationship('Actor', secondary=film_actor, lazy='subquery', back_populates="films")
    categories = relationship('Category', secondary=film_category, lazy='subquery')
