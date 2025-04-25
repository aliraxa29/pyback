from sqlalchemy import Column, Integer, String
from pyback.db import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    item_name = Column(String(145), nullable=False)
    item_description = Column(String(145), nullable=False)
