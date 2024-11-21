from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.store_model import Store
from app.schemas.store_schema import StoreInsert, StoreResponse

def insert_store(db: Session, store: StoreInsert) -> StoreResponse:
    try:
        store_obj = Store(
            store_name=store.store_name,
            manager_id=store.manager_id
        )
        db.add(store_obj)
        db.commit()
        db.refresh(store_obj)
        return StoreResponse.model_validate(store_obj)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to insert store: {str(e)}") from e

def get_all_stores(db: Session) -> List[StoreResponse]:
    stores = db.query(Store).all()
    return [StoreResponse.model_validate(store) for store in stores]

def get_store_by_id(db: Session, store_id: int) -> StoreResponse:
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    return StoreResponse.model_validate(store)

def update_store(db: Session, store_id: int, updates: StoreInsert) -> StoreResponse:
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(store, key, value)
    try:
        db.commit()
        db.refresh(store)
        return StoreResponse.model_validate(store)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update store: {str(e)}") from e

def delete_store(db: Session, store_id: int) -> None:
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    try:
        db.delete(store)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete store: {str(e)}") from e

