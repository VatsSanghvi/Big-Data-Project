from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import product_crud
from app.schemas.product_schema import ProductInsert, ProductResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductResponse)
def insert_product(product: ProductInsert, db: Session = Depends(get_db)):
    try:
        created_product = product_crud.insert_product(db=db, product=product)
        return created_product

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    try:
        return product_crud.get_all_products(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return product_crud.get_product_by_id(db=db, product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductInsert, db: Session = Depends(get_db)):
    try:
        return product_crud.update_product(db=db, product_id=product_id, updates=product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        return product_crud.delete_product(db=db, product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))