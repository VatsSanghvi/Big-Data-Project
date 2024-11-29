from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import category_crud
from app.schemas.category_schema import CategoryInsert, CategoryResponse
from app.database import SessionLocal
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        return category_crud.insert_category(db=db, category=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/all", response_model=List[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    try:
        return category_crud.get_all_categories(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return category_crud.get_category_by_id(db=db, category_id=category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        return category_crud.update_category(db=db, category_id=category_id, updates=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        return category_crud.delete_category(db=db, category_id=category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))