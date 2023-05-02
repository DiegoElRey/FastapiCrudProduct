from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.crud import  create_product, get_product, get_products, delete_user, update_product
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from app.schemas.user import UserCreate

router = APIRouter()

# @router.post("/producto", status_code=status.HTTP_201_CREATED)
# def create_product(product: ProductCreate):
#     print(product)
#     return product

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(product: ProductCreate, db: Session = Depends(get_db)):
    print(product)
    db_product = get_product(db, product.id)
    if db_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already registered",
        )
    return create_product(db=db, product=product)


@router.get("/{product_id}")
async def read_product(product_id: int, db: Session = Depends(get_db)):
    try:
        db_product = get_product(db, product_id=product_id)
        if db_product is None:
            return JSONResponse(content={"message": "User not found"},
                                 status_code=status.HTTP_404_NOT_FOUND)
        return db_product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )

@router.get("/")
async def read_products(db: Session = Depends(get_db)):
    try:
        db_product = get_products(db)
        if db_product is None:
            return JSONResponse(content={"message": "User not found"},
                                 status_code=status.HTTP_404_NOT_FOUND)
        return db_product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )

@router.put("/{id_product}")
async def actualizar_producto(id_product:int, product_update:ProductUpdate, db: Session = Depends(get_db)):
    try:
        db_product = get_product(db, id_product)
        if db_product is None:
            return JSONResponse(content={"message": "Product not found"},
                                 status_code=status.HTTP_404_NOT_FOUND)
        return update_product(db=db, product_update=product_update)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )

@router.delete("/{id_product}")
async def borrar_producto(id_product:int, db: Session = Depends(get_db)):
    try:
        db_product = get_product(db, id_product)
        if db_product is None:
            return JSONResponse(content={"message": "Product not found"},
                                 status_code=status.HTTP_404_NOT_FOUND)
        return delete_user(db=db, product=db_product)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )
