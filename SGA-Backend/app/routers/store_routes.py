from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import store_crud, user_crud
from app.schemas.store_schema import StoreInsertUpdate, StoreResponse, ProductPriceComparison
from app.database import SessionLocal
from typing import List
from datetime import datetime

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StoreResponse)
def create_store(store: StoreInsertUpdate, db: Session = Depends(get_db)):
    try:
        return store_crud.insert_store(db=db, store=store)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{owner_id}", response_model=List[StoreResponse])
def get_all_stores(owner_id: int, db: Session = Depends(get_db)):
    try:
        return store_crud.get_stores_by_owner(owner_id=owner_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{store_id}", response_model=StoreResponse)
def get_store_by_id(store_id: int, db: Session = Depends(get_db)):
    try:
        return store_crud.get_store_by_id(db=db, store_id=store_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{store_id}", response_model=StoreResponse)
def update_store(store_id: int, store: StoreInsertUpdate, db: Session = Depends(get_db)):
    try:
        store = store_crud.update_store(db=db, store_id=store_id, updates=store)
        if store.email:
            user = user_crud.get_user_by_email(db=db, email=store.email)
            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            role = "manager"

            update_user_role = user_crud.update_user_role(db=db, user_id=user.user_id, role=role)
            if not update_user_role:
                raise HTTPException(status_code=400, detail="Failed to update user role")

        return store
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{store_id}")
def delete_store(store_id: int, db: Session = Depends(get_db)):
    try:
        return store_crud.delete_store(db=db, store_id=store_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/compare-prices/{product_id}", response_model=ProductPriceComparison)
async def compare_prices(
        product_id: int,
        store_ids: List[int],
        db: Session = Depends(get_db)
):
    # Get current prices
    store_prices = store_crud.get_store_prices(
        db,
        product_id,
        store_ids,
        datetime.now()
    )

    return {
        "product_id": product_id,
        "product_name": store_prices[0].product.name if store_prices else None,
        "store_prices": store_prices
    }
