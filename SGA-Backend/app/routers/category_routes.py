from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import category_crud
from app.schemas.category_schema import CategoryInsert, CategoriesResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoriesResponse)
def create_category(category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        return category_crud.insert_category(db=db, category=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=CategoriesResponse)
def get_all_categories(db: Session = Depends(get_db)):
    try:
        return category_crud.get_all_categories(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{category_id}", response_model=CategoriesResponse)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return category_crud.get_category_by_id(db=db, category_id=category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{category_id}", response_model=CategoriesResponse)
def update_category(category_id: int, category: CategoryInsert, db: Session = Depends(get_db)):
    try:
        return category_crud.update_category(db=db, category_id=category_id, updates=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{category_id}", response_model=CategoriesResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        return category_crud.delete_category(db=db, category_id=category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))