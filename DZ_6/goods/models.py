from sqlalchemy import Column, String, Integer, DECIMAL
from db import Base

class Goods(Base):
    __tablename__ = "Goods"
    id = Column(Integer, primary_key=True)
    name_goods = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(DECIMAL)