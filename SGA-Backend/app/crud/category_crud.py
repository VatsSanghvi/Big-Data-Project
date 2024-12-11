from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.store_model import Store
from app.models.department_model import Department
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
            fk_department_id=category.fk_department_id
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

def get_categories_by_department(db: Session, department_id: int) -> List[CategoryResponse]:
    """
    Retrieve all Category records from the database.

    :param db: SQLAlchemy database session.
    :return: List of CategoryResponse objects.
    """
    categories = db.query(Category).filter(Category.fk_department_id == department_id).all()
    if not categories:
        raise RuntimeError(f"No categories found")
    return [CategoryResponse.model_validate(category) for category in categories]

def get_categories_by_owner(owner_id: int, db: Session) -> List[CategoryResponse]:
    """
    Retrieve all Category records from the database.

    :param db: SQLAlchemy database session.
    :return: List of CategoryResponse objects.
    """
    categories = []
    stores = db.query(Store).filter(Store.fk_owner_id == owner_id).all()
    for store in stores:
        departments_by_store = db.query(Department).filter(Department.fk_store_id == store.store_id).all()
        for department in departments_by_store:
            categories_by_department = db.query(Category).filter(Category.fk_department_id == department.department_id).all()
            categories.extend(categories_by_department)

    if not categories:
        raise RuntimeError("No categories found")
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
        raise RuntimeError(f"Category not found.")
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
     
def delete_category(db: Session, category_id: int):
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

        return f"Category {category.category_name} deleted successfully."
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete category: {str(e)}") from e



