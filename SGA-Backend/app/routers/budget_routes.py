from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import budget_crud
from app.schemas.budget_schema import BudgetCreate, BudgetResponse
from app.database import SessionLocal
from app.utils.base_response import BaseResponse

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}", response_model=BaseResponse[BudgetResponse])
async def create_budget(
    user_id: int,
    budget: BudgetCreate,
    db: Session = Depends(get_db)
):
    """Create a new budget for the user"""
    try:
        budget_created = budget_crud.create_budget(db, user_id, budget)
        return BaseResponse.success_response(data=budget_created, message="Budget created successfully")
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.get("/{budget_id}/{user_id}", response_model=BaseResponse[BudgetResponse])
async def get_budget(
    user_id: int,
    budget_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific budget by ID"""
    try:
        budget = budget_crud.get_budget(db, budget_id, user_id)
        if not budget or budget.user_id != user_id:
            return BaseResponse.error_response(message="Failed to retrieve budget")
        return BaseResponse.success_response(data=budget, message="Budget retrieved successfully")
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.put("/{budget_id}/{user_id}", response_model=BaseResponse[BudgetResponse])
async def update_budget_spending(
    user_id: int,
    budget_id: int,
    budget: BudgetCreate,
    db: Session = Depends(get_db)
):
    """Add spending to a budget"""
    try:
        update_budget = budget_crud.update_budget_spending(db, budget_id, user_id, budget)
        return BaseResponse.success_response(data=update_budget, message="Budget updated successfully")
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.post("/reset/{budget_id}/{user_id}", response_model=BaseResponse)
async def reset_budget(
    user_id: int,
    budget_id: int,
    db: Session = Depends(get_db)
):
    """Reset a budget's total spent to zero"""
    try:
        reset = budget_crud.reset_budget(db, budget_id, user_id)
        return BaseResponse.success_response(data=reset, message="Budget reset successfully")
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )