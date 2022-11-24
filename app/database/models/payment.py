from sqlalchemy import ForeignKey, Numeric
from sqlalchemy import Integer, Column, TIMESTAMP, Index

from app.database.base import Base
from app.database.models.base import AbstractModel


class Payment(Base, AbstractModel):
    __tablename__ = 'payment'
    __table_args__ = (
        Index('payment_pkey', 'payment_id'),
        Index('idx_fk_customer_id', 'customer_id'),
        Index('idx_fk_rental_id', 'rental_id'),
        Index('idx_fk_staff_id', 'staff_id'),
    )

    payment_id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id', name='payment_staff_id_fkey'))
    rental_id = Column(Integer, ForeignKey('rental.rental_id', name='payment_rental_id_fkey'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id', name='payment_customer_id_fkey'))
    amount = Column(Numeric)

    payment_date = Column(TIMESTAMP)
