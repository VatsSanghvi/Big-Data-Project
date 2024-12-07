from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import category_crud
from app.schemas.category_schema import CategoryInsert, CategoryResponse
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

@router.post("/", response_model=BaseResponse[CategoryResponse])
def create_category(category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        inserted_category = category_crud.insert_category(db=db, category=category)
        return BaseResponse.success_response(
            message="Category created successfully.",
            data=inserted_category
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/{department_id}", response_model=BaseResponse[List[CategoryResponse]])
def get_categories_by_department(department_id: int, db: Session = Depends(get_db)):
    try:
        categories_by_department = category_crud.get_categories_by_department(db=db, department_id=department_id)
        return BaseResponse.success_response(
            message="Categories retrieved successfully.",
            data=categories_by_department
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/", response_model=BaseResponse[List[CategoryResponse]])
def get_categories(db: Session = Depends(get_db)):
    try:
        all_categories = category_crud.get_categories(db=db)
        return BaseResponse.success_response(
            message="Categories retrieved successfully.",
            data=all_categories
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/{category_id}", response_model=BaseResponse[CategoryResponse])
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    try:
        category = category_crud.get_category_by_id(db=db, category_id=category_id)
        return BaseResponse.success_response(
            message="Category retrieved successfully.",
            data=category
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.put("/{category_id}", response_model=BaseResponse[CategoryResponse])
def update_category(category_id: int, category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        updated_category = category_crud.update_category(db=db, category_id=category_id, updates=category)
        return BaseResponse.success_response(
            message="Category updated successfully.",
            data=updated_category
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.delete("/{category_id}", response_model=BaseResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        deleted_category = category_crud.delete_category(db=db, category_id=category_id)
        return BaseResponse.success_response(
            message=deleted_category
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )
