from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Column, TIMESTAMP, Index

from app.database.base import Base
from app.database.models.base import AbstractModel


class Store(Base, AbstractModel):
    __tablename__ = 'store'
    __table_args__ = (
        Index('store_pkey', 'store_id'),
        Index('idx_unq_manager_staff_id', 'manager_staff_id'),
    )

    store_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.address_id', name='store_address_id_fkey'))
    manager_staff_id = Column(Integer, ForeignKey('staff.staff_id', name='store_manager_staff_id_fkey'))

    last_update = Column(TIMESTAMP)
