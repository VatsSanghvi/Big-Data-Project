from typing import List
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.store_model import Store, StorePrice
from app.schemas.store_schema import StoreInsert, StoreResponse

def insert_store(db: Session, store: StoreInsert) -> StoreResponse:
    """
    Insert a Store record into the database.

    :param db: SQLAlchemy database session.
    :param store: StoreInsert DTO to be inserted.
    :return: StoreResponse object representing the inserted store.
    """
    try:
        # Map DTO to SQLAlchemy Store object
        store_obj = Store(
            store_name=store.store_name,
            location=store.location,
            fk_owner_id=store.fk_owner_id,
            fk_manager_id=store.fk_manager_id
        )

        # Add and commit the store
        db.add(store_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(store_obj)

        # Convert to Pydantic model for returning
        return StoreResponse.model_validate(store_obj)
    except SQLAlchemyError as e:
        db.rollback() # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert store: {str(e)}") from e

def get_stores_by_owner(owner_id: int, db: Session) -> List[StoreResponse]:
    """
    Retrieve all Store records from the database.

    :param db: SQLAlchemy database session.
    :return: List of StoreResponse objects.
    """
    stores = db.query(Store).filter(Store.fk_owner_id == owner_id).all()
    return [StoreResponse.model_validate(store) for store in stores]

def get_store_by_id(db: Session, store_id: int) -> StoreResponse:
    """
    Retrieve a single Store record by its ID.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to retrieve.
    :return: StoreResponse object if found.
    :raises: RuntimeError if the store is not found.
    """
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    return StoreResponse.model_validate(store)

def update_store(db: Session, store_id: int, updates: StoreInsert) -> StoreResponse:
    """
    Update a Store record in the database.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to update.
    :param updates: StoreInsert DTO containing the updated data.
    :return: StoreResponse object representing the updated store.
    :raises: RuntimeError if the store is not found.
    """
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(store, key, value)
    
    try:
        db.commit()
        db.refresh(store)
        return StoreResponse.model_validate(store)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update store: {str(e)}") from e

def delete_store(db: Session, store_id: int):
    """
    Delete a Store record from the database.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to delete.
    :raises: RuntimeError if the store is not found.
    """
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    try:
        db.delete(store)
        db.commit()

        return {"message": f"Store {store.store_name} deleted successfully."}
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete store: {str(e)}") from e

def get_store_prices(
        db: Session,
        product_id: int,
        store_ids: List[int],
        current_time: datetime = datetime.now()
):
    return db.query(StorePrice).filter(
        StorePrice.product_id == product_id,
        StorePrice.store_id.in_(store_ids),
        StorePrice.price_valid_from <= current_time,
        StorePrice.price_valid_until >= current_time
    ).all()

