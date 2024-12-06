from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import department_crud
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse
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
        
@router.post("/", response_model=BaseResponse[DepartmentResponse])
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        inserted_department = department_crud.insert_department(db=db, department=department)
        return BaseResponse.success_response(
            message="Department created successfully",
            data=inserted_department
        )
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.get("/{store_id}", response_model=BaseResponse[List[DepartmentResponse]])
def get_departments_by_store(store_id: int, db: Session = Depends(get_db)):
    try:
        get_departments = department_crud.get_departments_by_store(db=db, store_id=store_id)
        return BaseResponse.success_response(
            message="Departments retrieved successfully",
            data=get_departments
        )
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.get("/{department_id}", response_model=BaseResponse[DepartmentResponse])
def get_department_by_id(department_id: int, db: Session = Depends(get_db)):
    try:
        department = department_crud.get_department_by_id(db=db, department_id=department_id)
        return BaseResponse.success_response(
            message="Department retrieved successfully",
            data=department
        )
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.put("/{department_id}", response_model=BaseResponse[DepartmentResponse])
def update_department(department_id: int, department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        updated_department = department_crud.update_department(db=db, department_id=department_id, updates=department)
        return BaseResponse.success_response(
            message="Department updated successfully",
            data=updated_department
        )
    except Exception as e:
        return BaseResponse.error_response(message=str(e))

@router.delete("/{department_id}", response_model=BaseResponse)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    try:
        deleted_department = department_crud.get_department_by_id(db=db, department_id=department_id)
        return BaseResponse.success_response(
            message="Department deleted successfully",
            data=deleted_department
        )
    except Exception as e:
        return BaseResponse.error_response(message=str(e))