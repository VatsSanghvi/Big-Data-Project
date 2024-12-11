from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.crud import grocery_list_crud as crud
from app.schemas.grocery_list_schema import GroceryListResponse, GroceryListCreate, GroceryItemBase, GroceryItemCreate
from app.database import SessionLocal
from app.utils.base_response import BaseResponse

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/", response_model=BaseResponse[GroceryListResponse])
async def insert_grocery_list(
    grocery_list: GroceryListCreate,
    db: Session = Depends(get_db),
):
    try:
        inserted_grocery_list = crud.insert_grocery_list(db, grocery_list)
        return BaseResponse.success_response(
            data=inserted_grocery_list,
            message="Grocery list created successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/{user_id}", response_model=BaseResponse[GroceryListResponse])
async def get_grocery_list(
    user_id: int,
    db: Session = Depends(get_db),
):
    try:
        grocery_list = crud.get_grocery_list(db, user_id)
        return BaseResponse.success_response(
            data=grocery_list,
            message="Grocery lists retrieved successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.delete("/{list_id}", response_model=BaseResponse)
async def delete_grocery_list(
    list_id: int,
    db: Session = Depends(get_db)
):
    try:
        deleted_grocery_list = crud.delete_grocery_list(db, list_id)
        return BaseResponse.success_response(
            data=deleted_grocery_list,
            message="Grocery list deleted successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/item/{list_id}", response_model=BaseResponse[List[GroceryItemBase]])
async def get_grocery_list_items(
    list_id: int,
    db: Session = Depends(get_db)
):
    try:
        grocery_list_items = crud.get_grocery_list_items(db, list_id)
        return BaseResponse.success_response(
            data=grocery_list_items,
            message="Grocery list items retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.post("/item", response_model=BaseResponse[GroceryItemBase])
async def insert_grocery_list_item(
    item: GroceryItemCreate,
    db: Session = Depends(get_db),
):
    try:
        inserted_grocery_item = crud.insert_grocery_list_item(db, item)
        return BaseResponse.success_response(
            data=inserted_grocery_item,
            message="Grocery list item created successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/item/{list_id}/{item_id}", response_model=BaseResponse[GroceryItemBase])
async def get_grocery_list_item_by_id(
    item_id: int,
    db: Session = Depends(get_db),
):
    try:
        grocery_item = crud.get_grocery_item_by_id(db, item_id)
        return BaseResponse.success_response(
            data=grocery_item,
            message="Grocery item retrieved successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.put("/item/{list_id}/{item_id}", response_model=BaseResponse[GroceryItemBase])
async def update_grocery_list_item(
    list_id: int,
    item_id: int,
    updates: GroceryItemCreate,
    db: Session = Depends(get_db),
):
    try:
        updated_grocery_item = crud.update_grocery_list_item(db, list_id, item_id, updates)
        return BaseResponse.success_response(
            data=updated_grocery_item,
            message="Grocery item updated successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.delete("/item/{list_id}/{item_id}", response_model=BaseResponse)
async def delete_grocery_list_item(
    list_id: int,
    item_id: int,
    db: Session = Depends(get_db),
):
    try:
        deleted_grocery_item = crud.delete_grocery_list_item(db, list_id, item_id)
        return BaseResponse.success_response(
            data=deleted_grocery_item,
            message="Grocery item deleted successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )
