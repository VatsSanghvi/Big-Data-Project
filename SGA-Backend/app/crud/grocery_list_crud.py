from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.grocery_list_model import GroceryList, GroceryItem
from app.schemas.grocery_list_schema import GroceryListResponse, GroceryItemCreate, GroceryItemResponse
from typing import List

def insert_grocery_list(db: Session, grocery_list: GroceryListResponse):
    """
    Insert a new grocery list to the database.
    :param db: SQLAlchemy database session.
    :param grocery_list: GroceryList object to be inserted.
    :return: Inserted grocery list.
    """
    try:
        # Map DTO to SQLAlchemy GroceryList object
        grocery_list_obj = GroceryList(
            name=grocery_list.name,
            user_id=grocery_list.user_id
        )

        # Add and commit the grocery list
        db.add(grocery_list_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(grocery_list_obj)

        # Convert to Pydantic model for returning
        return GroceryListResponse.model_validate(grocery_list_obj)
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert grocery list: {str(e)}") from e

def get_grocery_list(db: Session, list_id: int, user_id: int) -> List[GroceryListResponse]:
    """
    Retrieve a grocery list by its identifier and user.

    :param db: SQLAlchemy database session.
    :param list_id: Identifier of the grocery list.
    :param user_id: Identifier of the user.
    :return:
    """
    grocery_list = db.query(GroceryList).filter(GroceryList.id == list_id, GroceryList.user_id == user_id)
    if not grocery_list:
        raise RuntimeError(f"Grocery list with ID {list_id} not found.")
    return [GroceryListResponse.model_validate(grocery_list_items) for grocery_list_items in grocery_list]

def delete_grocery_list(db: Session, list_id: int):
    """
    Delete a grocery list by its identifier.

    :param db: SQLAlchemy database session.
    :param list_id: Identifier of the grocery list.
    :return: True if the grocery list was deleted successfully.
    """
    grocery_list = db.query(GroceryList).filter(GroceryList.id == list_id).first()
    if not grocery_list:
        raise RuntimeError(f"Grocery list with ID {list_id} not found.")
    try:
        db.delete(grocery_list)
        db.commit()

        return {"message": f"Grocery list {grocery_list.name} deleted successfully."}
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete grocery list: {str(e)}") from e

def insert_item_to_grocery_list(db: Session, item: GroceryItemCreate):
    """
    Insert a new item to the grocery list.
    :param db: SQLAlchemy database session.
    :param item: GroceryItem object to be inserted.
    :return: Inserted item.
    """
    try:
        # Map DTO to SQLAlchemy GroceryItem object
        item_obj = GroceryItem(
            name=item.name,
            category=item.category,
            grocery_list_id=item.grocery_list_id
        )

        # Add and commit the category
        db.add(item_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(item_obj)

        # Convert to Pydantic model for returning
        return GroceryItemResponse.model_validate(item_obj)
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert item: {str(e)}") from e

def get_grocery_item_by_id(db: Session, item_id: int):
    """
    Retrieve a grocery item by its identifier.
    :param db: SQLAlchemy database session.
    :param item_id: Identifier of the grocery item.
    :return: GroceryItem object if found.
    :raises: RuntimeError if the item is not found.
    """
    item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
    if not item:
        raise RuntimeError(f"Item with ID {item_id} not found.")
    return GroceryItemResponse.model_validate(item)

def update_grocery_list_item(db: Session, item_id: int, updates: GroceryItemCreate):
    """
    Update a grocery list item.
    :param db: db: SQLAlchemy database session.
    :param item_id: ID of the item to update.
    :param updates: GroceryItemCreate DTO containing the updated data.
    :return: GroceryItemResponse object representing the updated item.
    :raises: RuntimeError if the item is not found.
    """
    item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
    if not item:
        raise RuntimeError(f"Item with ID {item_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    try:
        db.commit()
        db.refresh(item)

        return GroceryItemResponse.model_validate(item)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update item: {str(e)}") from e


def delete_grocery_list_item(db: Session, item_id: int):
    """
    Delete a grocery list item by its identifier.
    :param db: SQLAlchemy database session.
    :param item_id: ID of the item to delete.
    :return: RuntimeError if the item is not found.
    """
    item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
    if not item:
        raise RuntimeError(f"Item with ID {item_id} not found.")
    try:
        db.delete(item)
        db.commit()

        return {"message": f"Item {item.name} deleted successfully."}
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete item: {str(e)}") from e
