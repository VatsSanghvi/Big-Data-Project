from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import store_crud, user_crud
from app.schemas.store_schema import StoreCreate, AssignManager, StoreResponse, ProductPriceComparison
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
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    try:
        owner = user_crud.get_user_by_id(db=db, user_id=store.fk_owner_id)
        if not owner:
            raise HTTPException(status_code=400, detail="Owner not found")
        if owner.role != "admin":
            raise HTTPException(status_code=400, detail="Unauthorized to create store")

        return store_crud.insert_store(db=db, store=store)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{owner_id}", response_model=List[StoreResponse])
def get_all_stores(owner_id: int, db: Session = Depends(get_db)):
    try:
        owner = user_crud.get_user_by_id(db=db, user_id=owner_id)
        if not owner:
            raise HTTPException(status_code=400, detail="Owner not found")
        if owner.role == "customer":
            return []
        return store_crud.get_stores_by_owner(owner_id=owner_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/assign-owner/{store_id}", response_model=StoreResponse)
def update_store(store_id: int, updates: AssignManager, db: Session = Depends(get_db)):
    try:
        store = store_crud.update_store(db=db, store_id=store_id, updates=updates)
        if updates.email:
            user = user_crud.get_user_by_email(db=db, email=updates.email)

            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            if user.role == "customer":
                raise HTTPException(status_code=400, detail="Customer cannot be assigned as store owner")

            update_user_role = user_crud.update_user_role(db=db, user_id=user.user_id, role=user.role)
            if not update_user_role:
                raise HTTPException(status_code=400, detail="Failed to update user role")

            store = store_crud.assign_manager(db=db, store_id=store.store_id, user_id=user.user_id)

        return store
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{store_id}/{owner_id}")
def delete_store(store_id: int, owner_id: int, db: Session = Depends(get_db)):
    try:
        owner = user_crud.get_user_by_id(db=db, user_id=owner_id)
        if not owner:
            raise HTTPException(status_code=400, detail="Owner not found")
        if owner.role != "admin":
            raise HTTPException(status_code=400, detail="Unauthorized to delete store")

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
