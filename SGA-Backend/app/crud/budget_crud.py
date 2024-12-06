from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from decimal import Decimal
from app.models.budget_model import Budget
from app.schemas.budget_schema import BudgetCreate

def create_budget(db: Session, user_id: int, budget: BudgetCreate):
    """
    Create a new budget for the user
    :param db: SQLAlchemy Session
    :param budget: BudgetCreate DTO object
    :return: Budget object
    """
    try:
        db_budget = Budget(
            user_id=user_id,
            amount=budget.amount,
            total_spent=Decimal('0.00')
        )
        db.add(db_budget)
        db.commit()
        db.refresh(db_budget)
        return db_budget
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create budget: {str(e)}")

def get_budget(db: Session, budget_id: int, user_id: int):
    """
    Get a specific budget by ID
    :param db: SQLAlchemy Session
    :param budget_id: ID of the budget
    :return: Budget object
    """
    budget = db.query(Budget).filter(Budget.budget_id == budget_id, Budget.user_id == user_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

def update_budget_spending(db: Session, budget_id: int, user_id: int, updates: BudgetCreate):
    """
    Update the total spent amount for a budget
    :param db: SQLAlchemy Session
    :param budget_id: ID of the budget
    :param amount: Amount to add to the total spent
    :return: Budget object
    """
    try:
        budget = get_budget(db, budget_id, user_id)
        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found")

        new_total = budget.total_spent + updates.amount

        if new_total > budget.amount:
            raise HTTPException(status_code=400, detail="This purchase would exceed your budget")

        budget.total_spent = new_total

        db.commit()
        db.refresh(budget)
        return budget
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to update budget: {str(e)}")

def reset_budget(db: Session, budget_id: int, user_id: int):
    """
    Reset the total spent amount for a budget
    :param db: SQLAlchemy Session
    :param budget_id: ID of the budget
    :return: Budget object
    """
    try:
        budget = get_budget(db, budget_id, user_id)
        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found")

        budget.total_spent = Decimal('0.00')

        db.commit()
        db.refresh(budget)
        return "Budget reset successfully"
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to reset budget: {str(e)}")