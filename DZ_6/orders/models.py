from sqlalchemy import Column, String, Integer,  Date, ForeignKey
from db import Base

class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    order_date = Column(Date)
    status = Column(String)