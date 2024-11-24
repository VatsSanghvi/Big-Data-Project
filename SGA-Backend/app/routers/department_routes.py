from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import department_crud
from app.schemas.department_schema import DepartmentCreate, DepartmentsResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model=DepartmentsResponse)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return department_crud.insert_department(db=db, department=department)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=DepartmentsResponse)
def get_all_departments(db: Session = Depends(get_db)):
    try:
        return department_crud.get_all_departments(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{department_id}", response_model=DepartmentsResponse)
def get_department_by_id(department_id: int, db: Session = Depends(get_db)):
    try:
        return department_crud.get_department_by_id(db=db, department_id=department_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{department_id}", response_model=DepartmentsResponse)
def update_department(department_id: int, department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return department_crud.update_department(db=db, department_id=department_id, updates=department)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{department_id}", response_model=DepartmentsResponse)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    try:
        return department_crud.delete_department(db=db, department_id=department_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))