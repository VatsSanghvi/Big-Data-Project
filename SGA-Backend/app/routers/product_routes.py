from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import product_crud
from app.schemas.product_schema import ProductInsert, ProductsResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=ProductsResponse)
def insert_product(product: ProductInsert, db: Session = Depends(get_db)):
    try:
        created_product = product_crud.insert_product(db=db, product=product)
        return ProductsResponse(
            ok=True,
            msg=f"{created_product.product_name} created successfully",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))