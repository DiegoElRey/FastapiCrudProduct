from sqlalchemy import Boolean, Column, Integer, String, Float, MetaData
from app.database import Base

metadata=MetaData()
class Product(Base):
    __tablename__ = "productos"
    id_product = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(200), index=True)
    description = Column(String, index=True)
    value = Column(Float, index=True)
    year = Column(Integer, index=True)
    month = Column(Integer, index=True)
    day = Column(Integer, index=True)

