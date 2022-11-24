from datetime import datetime

from sqlalchemy import Integer, Column, TIMESTAMP, Index, VARCHAR
from sqlalchemy.orm import Session as DbSession, relationship

from app.database.base import Base
from app.database.models.__relations_tables import film_category
from app.database.models.base import AbstractModel
from app.schema.category import CategoryInput, CategoryOutput


class Category(Base, AbstractModel):
    __tablename__ = 'category'
    __table_args__ = (
        Index('category_pkey', 'category_id'),
    )
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(25))
    last_update = Column(TIMESTAMP)
    films = relationship('Film', secondary=film_category, lazy='dynamic', back_populates="categories")

    @classmethod
    def create(cls, db: DbSession, data: CategoryInput) -> CategoryOutput:
        new_obj = cls(
            **data.dict(),
            last_update=datetime.utcnow(),
        )
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)

        return new_obj
