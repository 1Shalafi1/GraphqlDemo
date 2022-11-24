from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy import Integer, Column, TIMESTAMP, Index, LargeBinary, Boolean

from app.database.base import Base
from app.database.models.base import AbstractModel


class Staff(Base, AbstractModel):
    __tablename__ = 'staff'
    __table_args__ = (
        Index('staff_pkey', 'staff_id'),
    )

    staff_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.address_id', name='staff_address_id_fkey'))
    store_id = Column(Integer)

    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    username = Column(VARCHAR(16))
    password = Column(VARCHAR(45))
    active = Column(Boolean)
    picture = Column(LargeBinary)
    last_update = Column(TIMESTAMP)
