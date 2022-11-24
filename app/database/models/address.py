from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy import Integer, Column, TIMESTAMP, Index

from app.database.base import Base
from app.database.models.base import AbstractModel


class Address(Base, AbstractModel):
    __tablename__ = 'address'
    __table_args__ = (
        Index('address_pkey', 'address_id'),
        Index('idx_fk_city_id', 'city_id'),
    )

    address_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.city_id', name='fk_address_city'))

    address = Column(VARCHAR(50))
    address2 = Column(VARCHAR(50))
    district = Column(VARCHAR(20))
    postal_code = Column(VARCHAR(10))
    phone = Column(VARCHAR(20))
    last_update = Column(TIMESTAMP)
