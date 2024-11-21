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
        category_obj = Category(
            category_name=category.category_name,
            department_id=category.department_id
        )
        
        db.add(category_obj)
        db.commit()
        db.refresh(category_obj)
        
        return CategoryResponse.model_validate(category_obj)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to insert category: {str(e)}") from e

def get_all_categories(db: Session) -> List[CategoryResponse]:
    categories = db.query(Category).all()
    return [CategoryResponse.model_validate(category) for category in categories]
 
def get_category_by_id(db: Session, category_id: int) -> CategoryResponse:
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")
    return CategoryResponse.model_validate(category)
 
def update_category(db: Session, category_id: int, updates: CategoryInsert) -> CategoryResponse:
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")
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
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        raise RuntimeError(f"Category with ID {category_id} not found.")
    try:
        db.delete(category)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete category: {str(e)}") from e



