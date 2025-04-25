from sqlalchemy import Column, Integer, String
from pyback.db import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String(145), nullable=False)