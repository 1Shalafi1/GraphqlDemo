from sqlalchemy import Integer, Column, TIMESTAMP, Index, Text

from app.database.base import Base
from app.database.models.base import AbstractModel


class Language(Base, AbstractModel):
    __tablename__ = 'language'
    __table_args__ = (
        Index('language_pkey', 'language_id'),
    )

    language_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(Text)
    last_update = Column(TIMESTAMP)
