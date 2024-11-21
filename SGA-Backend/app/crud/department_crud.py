from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.department_model import Department
from app.schemas.department_schema import DepartmentInsert, DepartmentResponse

def insert_department(db: Session, department: DepartmentInsert) -> DepartmentResponse:
    try:
        department_obj = Department(
            department_name=department.department_name,
            store_id=department.store_id
        )
        db.add(department_obj)
        db.commit()
        db.refresh(department_obj)
        return DepartmentResponse.model_validate(department_obj)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to insert department: {str(e)}") from e
    
def get_all_departments(db: Session) -> List[DepartmentResponse]:
    departments = db.query(Department).all()
    return [DepartmentResponse.model_validate(department) for department in departments]

def get_department_by_id(db: Session, department_id: int) -> DepartmentResponse:
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")
    return DepartmentResponse.model_validate(department)

def update_department(db: Session, department_id: int, updates: DepartmentInsert) -> DepartmentResponse:
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(department, key, value)
    try:
        db.commit()
        db.refresh(department)
        return DepartmentResponse.model_validate(department)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update department: {str(e)}") from e

def delete_department(db: Session, department_id: int) -> None:
    department = db.query(Department).filter(Department.department_id == department_id).first()
    if not department:
        raise RuntimeError(f"Department with ID {department_id} not found.")
    try:
        db.delete(department)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete department: {str(e)}") from e
