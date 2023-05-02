from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    id:int
    full_name:str
    description:str
    value:float
    year:int
    month:int
    day:int


class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    full_name:str
    description:str
    value:float

class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True