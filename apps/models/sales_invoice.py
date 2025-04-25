from sqlalchemy import Column, Integer, String
from pyback.db import Base

class SalesInvoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    name = Column(String(145), nullable=False)