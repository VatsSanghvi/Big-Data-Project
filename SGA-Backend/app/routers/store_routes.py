from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.crud import store_crud, user_crud
from app.schemas.store_schema import StoreCreateRequest, StoreUpdateRequest, StoreResponse, PriceComparisonRequest, FlyerResponse
from app.database import SessionLocal
from app.utils.base_response import BaseResponse
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BaseResponse[StoreResponse])
def create_store(store: StoreCreateRequest, db: Session = Depends(get_db)):
    try:
        owner = user_crud.get_user_by_id(db=db, user_id=store.fk_owner_id)
        if not owner:
            return BaseResponse.error_response(message="Owner not found")

        if owner.role != "admin":
            return BaseResponse.error_response("Unauthorized to create store")

        if store.manager_email:
            manager = user_crud.get_user_by_email(db=db, email=store.manager_email)
            if not manager:
                return BaseResponse.error_response("Manager not found")

            update_user_role = user_crud.update_user_role(db=db, user_id=manager.user_id, role="manager")
            if not update_user_role:
                return BaseResponse.error_response("Failed to update user role")

            new_store = store_crud.insert_store(db=db, store=store)
            assigned_store = store_crud.update_manager(db=db, store_id=new_store.store_id, user_id=manager.user_id)
            return assigned_store

        inserted_store = store_crud.insert_store(db=db, store=store)
        return BaseResponse.success_response(data=inserted_store, message="Store created successfully")

    except Exception as e:
        return BaseResponse.error_response(str(e))

@router.get("/{owner_id}", response_model=BaseResponse[List[StoreResponse]])
def get_stores_by_owner(owner_id: int, db: Session = Depends(get_db)):
    try:
        owner = user_crud.get_user_by_id(db=db, user_id=owner_id)
        if not owner:
            return BaseResponse.error_response("Owner not found")
        if owner.role == "customer":
            return BaseResponse.error_response("Unauthorized to view stores")
        stores = store_crud.get_stores_by_owner(owner_id=owner_id, db=db)
        if not stores:
            return BaseResponse.error_response("No stores found")
        return BaseResponse.success_response(data=stores, message="Stores retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(str(e))

@router.put("/{store_id}", response_model=BaseResponse[StoreResponse])
def update_store(store_id: int, updates: StoreUpdateRequest, db: Session = Depends(get_db)):
    try:
        store = store_crud.get_store_by_id(db=db, store_id=store_id)
        if not store:
            return BaseResponse.error_response("Store not found")

        if updates.manager_email:
            user = user_crud.get_user_by_email(db=db, email=updates.manager_email)

            if not user:
                return BaseResponse.error_response("User not found")

            update_user_role = user_crud.update_user_role(db=db, user_id=user.user_id, role="manager")
            if not update_user_role:
                return BaseResponse.error_response("Failed to update user role")

            update_manager = store_crud.update_manager(db=db, store_id=store_id, user_id=update_user_role.user_id)
            if not update_manager:
                return BaseResponse.error_response("Failed to update store manager")

            updated_store = store_crud.update_store(db=db, store_id=store_id, updates=updates)
            return BaseResponse.success_response(message="Store updated successfully", data=updated_store)

        elif store.manager:
            update_user_role = user_crud.update_user_role(db=db, user_id=store.manager.user_id,role="customer")
            if not update_user_role:
                return BaseResponse.error_response("Failed to update user role")

            update_manager = store_crud.update_manager(db=db, store_id=store_id)
            if not update_manager:
                return BaseResponse.error_response("Failed to update store manager")

            updated_store = store_crud.update_store(db=db, store_id=store_id, updates=updates)
            return BaseResponse.success_response(message="Store updated successfully", data=updated_store)
        else:
            updated_store = store_crud.update_store(db=db, store_id=store_id, updates=updates)
            return BaseResponse.success_response(message="Store updated successfully", data=updated_store)

    except Exception as e:
        return BaseResponse.error_response(str(e))

@router.delete("/{store_id}", response_model=BaseResponse)
def delete_store(store_id: int, db: Session = Depends(get_db)):
    try:
        store = store_crud.get_store_by_id(db=db, store_id=store_id)
        if not store:
            return BaseResponse.error_response("Store not found")
        if store.manager:
            update_user_role = user_crud.update_user_role(db=db, user_id=store.manager.user_id, role="customer")
            if not update_user_role:
                return BaseResponse.error_response("Failed to update user role")

        deleted_store = store_crud.delete_store(db=db, store_id=store_id)
        return BaseResponse.success_response(message="Store deleted successfully", data=deleted_store)
    except Exception as e:
        return BaseResponse.error_response(str(e))

@router.get("/compare-prices/{product_id}", response_model=BaseResponse[PriceComparisonRequest])
async def compare_prices(
        product_id: int,
        store_ids: str = Query(...),
        db: Session = Depends(get_db)
):
    try:
        store_ids_list = [int(_) for _ in store_ids.split(",")]
        if not store_ids_list:
            return BaseResponse.error_response(
                message="No valid store IDs provided"
            )
        store_prices = store_crud.get_store_prices(db, product_id, store_ids_list)

        # Create comparison response
        comparison = PriceComparisonRequest(
            product_id=product_id,
            product_name=store_prices[0].product.product_name if store_prices else None,
            store_prices=[
                PriceComparisonRequest.model_validate(price)
                for price in store_prices
            ]
        )

        return BaseResponse.success_response(
            data=comparison,
            message=f"Successfully retrieved prices from {len(store_prices)} stores"
        )
    except Exception as e:
        return BaseResponse.error_response(str(e))

@router.get("/flyer/{store_id}", response_model=BaseResponse[FlyerResponse])
async def get_store_flyer(
    store_id: int,
    db: Session = Depends(get_db),
):
    try:
        flyer = store_crud.get_store_flyer(db, store_id)
        if not flyer:
            return BaseResponse.error_response(message="Flyer not found")
        return BaseResponse.success_response(data=flyer, message="Flyer retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(str(e))
