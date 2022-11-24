from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy import Integer, Column, TIMESTAMP, Index, Boolean

from app.database.base import Base
from app.database.models.base import AbstractModel


class Customer(Base, AbstractModel):
    __tablename__ = 'customer'
    __table_args__ = (
        Index('customer_pkey', 'customer_id'),
        Index('idx_fk_address_id', 'address_id'),
        Index('idx_fk_store_id', 'store_id'),
        Index('idx_last_name', 'last_name'),
    )

    customer_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.address_id', name='customer_address_id_fkey'))
    store_id = Column(Integer, ForeignKey('store.store_id', name='customer_store_id_fkey'))

    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    email = Column(VARCHAR(50))
    active = Column(Boolean)
    create_date = Column(TIMESTAMP)
    last_update = Column(TIMESTAMP)
