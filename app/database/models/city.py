from sqlalchemy import Integer, Column, TIMESTAMP, Index, ForeignKey, VARCHAR

from app.database.base import Base
from app.database.models.base import AbstractModel


class City(Base, AbstractModel):
    __tablename__ = 'city'
    __table_args__ = (
        Index('city_pkey', 'city_id'),
        Index('idx_fk_country_id', 'country_id'),
    )

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey(column="country.country_id", name='fk_city'))

    city = Column(VARCHAR(50))

    last_update = Column(TIMESTAMP)
