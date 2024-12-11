from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.store_model import Store, StorePrice, Flyer
from app.models.product_model import Product
from app.schemas.store_schema import StoreCreateRequest, StoreUpdateRequest, StoreResponse

def insert_store(db: Session, store: StoreCreateRequest):
    """
    Insert a Store record into the database.

    :param db: SQLAlchemy database session.
    :param store: StoreCreate DTO to be inserted.
    :return: StoreResponse object representing the inserted store.
    """
    try:
        # Map DTO to SQLAlchemy Store object
        store_obj = Store(
            store_name=store.store_name,
            location=store.location,
            fk_owner_id=store.fk_owner_id,
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

def get_stores_by_owner(owner_id: int, db: Session):
    """
    Retrieve all Store records from the database.

    :param db: SQLAlchemy database session.
    :return: List of StoreResponse objects.
    """
    stores = db.query(Store).filter(Store.fk_owner_id == owner_id).all()
    if not stores:
        raise RuntimeError("No stores found")
    return [StoreResponse.model_validate(store) for store in stores]

def get_stores(db: Session):
    """
    Retrieve all Store records from the database.

    :param db: SQLAlchemy database session.
    :return: List of StoreResponse objects.
    """
    stores = db.query(Store).all()
    if not stores:
        raise RuntimeError("No stores found")
    return [StoreResponse.model_validate(store) for store in stores]

def get_store_by_id(db: Session, store_id: int) -> StoreResponse:
    """
    Retrieve a Store record from the database.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to retrieve.
    :return: StoreResponse object representing the store.
    :raises: RuntimeError if the store is not found.
    """
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")
    return StoreResponse.model_validate(store)

def update_store(db: Session, store_id: int, updates: StoreUpdateRequest) -> StoreResponse:
    """
    Update a Store record in the database.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to update.
    :param updates: StoreCreate DTO containing the updated data.
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

def update_manager(db: Session, store_id: int, user_id: Optional[int] = None) -> StoreResponse:
    """
    Add a user as a manager for a store.

    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to add the manager to.
    :param user_id: ID of the user to add as a manager.
    :return: StoreResponse object representing the updated store.
    :raises: RuntimeError if the store is not found.
    """
    store = db.query(Store).filter(Store.store_id == store_id).first()
    if not store:
        raise RuntimeError(f"Store with ID {store_id} not found.")

    if user_id:
        store.fk_manager_id = user_id
    else:
        store.fk_manager_id = None

    try:
        db.commit()
        db.refresh(store)
        return StoreResponse.model_validate(store)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to add manager to store: {str(e)}") from e

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

        return f"Store {store.store_name} deleted successfully."
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete store: {str(e)}") from e

def get_store_prices(db: Session, product_id: int, store_ids: List[int]):
    """
    Get the prices of a product at a list of stores at a given time.
    :param db: SQLAlchemy database session.
    :param product_id: ID of the product to get prices for.
    :param store_ids: List of store IDs to get prices from.
    :return: List of StorePrice objects.
    """
    # First verify product exists
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise ValueError(f"Product with ID {product_id} not found")

    # Verify stores exist
    existing_stores = db.query(Store.store_id).filter(Store.store_id.in_(store_ids)).all()
    existing_store_ids = [store.store_id for store in existing_stores]

    if not existing_store_ids:
        raise ValueError("None of the provided store IDs exist")

    if len(existing_store_ids) != len(store_ids):
        invalid_stores = set(store_ids) - set(existing_store_ids)
        raise ValueError(f"Some store IDs are invalid: {invalid_stores}")

    # Get prices
    store_prices = (
        db.query(StorePrice)
        .filter(
            StorePrice.product_id == product_id,
            StorePrice.store_id.in_(store_ids)
        )
        .all()
    )

    if not store_prices:
        raise ValueError(f"No prices found for product {product_id} in the specified stores")

    return store_prices


def get_store_flyer(db: Session, store_price_id: int):
    """
    Get the flyer for a store.
    :param db: SQLAlchemy database session.
    :param store_id: ID of the store to get the flyer for.
    :return: Flyer object for the store.
    """

    # First verify store price exists
    store_price = db.query(StorePrice).filter(StorePrice.id == store_price_id).first()
    if not store_price:
        raise ValueError("Store price not found")

    store_flyer = db.query(Flyer).join(StorePrice).filter(store_price.id == store_price_id).first()
    if not store_flyer:
        raise RuntimeError("No flyer found")
    return store_flyer

