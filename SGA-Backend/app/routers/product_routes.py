from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import product_crud
from app.schemas.product_schema import ProductCreateRequest, ProductResponse
from app.database import SessionLocal
from app.utils.base_response import BaseResponse

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BaseResponse[ProductResponse])
def insert_product(product: ProductCreateRequest, db: Session = Depends(get_db)):
    try:
        created_product = product_crud.insert_product(db=db, product=product)
        return BaseResponse.success_response(data=created_product, message="Product created successfully")

    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.get("/owner/{owner_id}", response_model=BaseResponse[list[ProductResponse]])
def get_products_by_owner(owner_id: int, db: Session = Depends(get_db)):
    try:
        get_products = product_crud.get_products_by_owner(db=db, owner_id=owner_id)
        return BaseResponse.success_response(data=get_products, message="Products retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.get("/", response_model=BaseResponse[list[ProductResponse]])
def get_all_products(db: Session = Depends(get_db)):
    try:
        get_products = product_crud.get_all_products(db=db)
        return BaseResponse.success_response(data=get_products, message="Products retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.put("/{product_id}", response_model=BaseResponse[ProductResponse])
def update_product(product_id: int, product: ProductCreateRequest, db: Session = Depends(get_db)):
    try:
        updated_product = product_crud.update_product(db=db, product_id=product_id, updates=product)
        return BaseResponse.success_response(data=updated_product, message="Product updated successfully")
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.delete("/{product_id}", response_model=BaseResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        deleted_product = product_crud.delete_product(db=db, product_id=product_id)
        return BaseResponse.success_response(data=deleted_product, message="Product deleted successfully")
    except Exception as e:
        return BaseResponse.error_response(message=str(e))