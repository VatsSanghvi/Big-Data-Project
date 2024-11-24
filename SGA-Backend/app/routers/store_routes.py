from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import store_crud
from app.schemas.store_schema import StoreCreate, StoresResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   
@router.post("/", response_model=StoresResponse)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    try:
        return store_crud.insert_store(db=db, store=store)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=StoresResponse)
def get_all_stores(db: Session = Depends(get_db)):
    try:
        return store_crud.get_all_stores(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{store_id}", response_model=StoresResponse)
def get_store_by_id(store_id: int, db: Session = Depends(get_db)):
    try:
        return store_crud.get_store_by_id(db=db, store_id=store_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{store_id}", response_model=StoresResponse)
def update_store(store_id: int, store: StoreCreate, db: Session = Depends(get_db)):
    try:
        return store_crud.update_store(db=db, store_id=store_id, updates=store)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{store_id}", response_model=StoresResponse)
def delete_store(store_id: int, db: Session = Depends(get_db)):
    try:
        return store_crud.delete_store(db=db, store_id=store_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))