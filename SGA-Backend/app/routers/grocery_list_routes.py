from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import grocery_list_crud as crud
from app.schemas.grocery_list_schema import GroceryItem
from app.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/")
async def insert_item_to_grocery_list(
    item: GroceryItem,
    db: Session = Depends(get_db),
):
    if not crud.insert_item_to_grocery_list(db, item):
        raise HTTPException(status_code=403, detail="Error inserting item")
    return {"message": "Item inserted successfully"}

@router.get("/{list_id}/items", response_model=List[GroceryItem])
async def get_grocery_list_items(
    user_id: int,
    list_id: int,
    db: Session = Depends(get_db)
):
    # Verify user has access to this list
    if not crud.get_grocery_list(db, list_id, user_id):
        raise HTTPException(status_code=403, detail="Not authorized to access this list")
    return crud.get_grocery_list(db, list_id, user_id)

@router.delete("/{list_id}")
async def delete_grocery_list(
    list_id: int,
    db: Session = Depends(get_db)
):
    if not crud.delete_grocery_list(db, list_id):
        raise HTTPException(status_code=403, detail="Only the list owner can delete it")
    crud.delete_grocery_list(db, list_id)
    return {"message": "Grocery list deleted successfully"}

@router.get("/{item_id}")
async def get_grocery_item_by_id(
    item_id: int,
    db: Session = Depends(get_db),
):
    if not crud.get_grocery_item_by_id(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.get_grocery_item_by_id(db, item_id)

@router.put("/{item_id}")
async def update_grocery_list_item(
    item_id: int,
    item: GroceryItem,
    db: Session = Depends(get_db),
):
    if not crud.update_grocery_list_item(db, item_id, item):
        raise HTTPException(status_code=403, detail="Error updating item")
    return crud.update_grocery_list_item(db, item_id, item)

@router.delete("/{list_id}/items/{item_id}")
async def delete_grocery_list_item(
    list_id: int,
    item_id: int,
    db: Session = Depends(get_db),
):
    if not crud.delete_grocery_list_item(db, list_id):
        raise HTTPException(status_code=403, detail="Error deleting item")
    return crud.delete_grocery_list_item(db, item_id)