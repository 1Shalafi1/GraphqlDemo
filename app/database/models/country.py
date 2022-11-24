from sqlalchemy import Integer, Column, TIMESTAMP, Index, VARCHAR

from app.database.base import Base
from app.database.models.base import AbstractModel


class Country(Base, AbstractModel):
    __tablename__ = 'country'
    __table_args__ = (
        Index('country_pkey', 'country_id'),
    )

    country_id = Column(Integer, primary_key=True, autoincrement=True)

    country = Column(VARCHAR(20))

    last_update = Column(TIMESTAMP)
