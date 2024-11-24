from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.category_model import Category
from app.schemas.category_schema import CategoryInsert, CategoryResponse

def insert_category(db: Session, category: CategoryInsert) -> CategoryResponse:
    """
    Insert a Category record into the database.

    :param db: SQLAlchemy database session.
    :param category: CategoryInsert DTO to be inserted.
    :return: CategoryResponse object representing the inserted category.
    """
    try:
        # Map DTO to SQLAlchemy Category object
        category_obj = Category(
            category_name=category.category_name,
            department_id=category.department_id
        )

        # Add and commit the category
        db.add(category_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(category_obj)

        # Convert to Pydantic model for returning
        return CategoryResponse.model_validate(category_obj)
    except SQLAlchemyError as e:
        db.rollback() # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert category: {str(e)}") from e

def get_all_categories(db: Session) -> List[CategoryResponse]:
    """
    Retrieve all Category records from the database.

    :param db: SQLAlchemy database session.
    :return: List of CategoryResponse objects.
    """
    categories = db.query(Category).all()
    return [CategoryResponse.model_validate(category) for category in categories]
 
def get_category_by_id(db: Session, category_id: int) -> CategoryResponse:
    """
    Retrieve a single Category record by its ID.

    :param db: SQLAlchemy database session.
    :param category_id: ID of the category to retrieve.
    :return: CategoryResponse object if found.
    :raises: RuntimeError if the category is not found.
    """
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")
    return CategoryResponse.model_validate(category)
 
def update_category(db: Session, category_id: int, updates: CategoryInsert) -> CategoryResponse:
    """
    Update a Category record in the database.

    :param db: SQLAlchemy database session.
    :param category_id: ID of the category to update.
    :param updates: CategoryInsert DTO containing the updated data.
    :return: CategoryResponse object representing the updated category.
    :raises: RuntimeError if the category is not found.
    """
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(category, key, value)
    try:
        db.commit()
        db.refresh(category)
        
        return CategoryResponse.model_validate(category)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update category: {str(e)}") from e
     
def delete_category(db: Session, category_id: int) -> None:
    """
    Delete a Category record from the database.

    :param db: SQLAlchemy database session.
    :param category_id: ID of the category to delete.
    :raises: RuntimeError if the category is not found.
    """
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")
    try:
        db.delete(category)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete category: {str(e)}") from e



