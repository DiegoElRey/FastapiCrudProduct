from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id_product == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(full_name=product.full_name, description=product.description, value=product.value, year=product.year, month=product.month, day=product.day)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: ProductCreate, product_update: ProductUpdate):
    print("holaaaaaaaaaaa")
    product.full_name = product_update.full_name
    product.description = product_update.description
    product.value = product_update.value
    db.commit()
    db.refresh(product)
    return product

def delete_user(db: Session, product:Product):
    try:
        db.delete(product)
        db.commit()
        return "Product deleted"
    except Exception as e:
        return "product not found"