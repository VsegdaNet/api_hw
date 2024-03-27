from sqlalchemy import Column, String, Integer
from db import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    hash_password = Column(String, nullable=False)


