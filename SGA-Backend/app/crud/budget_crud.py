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

def update_budget(db: Session, budget_id: int, user_id: int, new_amount: Decimal):
    """
    Update the budget amount for a specific user and budget.
    :param db: SQLAlchemy Session
    :param budget_id: ID of the budget
    :param user_id: ID of the user
    :param new_amount: New budget amount to set
    :return: Updated Budget object
    """
    try:
        # Fetch the budget by ID and user_id
        budget = db.query(Budget).filter(
            Budget.budget_id == budget_id, 
            Budget.user_id == user_id
        ).first()

        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found")

        # Update the budget amount
        budget.amount = new_amount
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
    
def get_remaining_budget(db: Session, budget_id: int, user_id: int):
    """
    Get the remaining budget by subtracting total_spent from the amount.
    :param db: SQLAlchemy Session
    :param budget_id: ID of the budget
    :param user_id: User ID
    :return: Dictionary containing the remaining budget
    """
    budget = db.query(Budget).filter(
        Budget.budget_id == budget_id,
        Budget.user_id == user_id
    ).first()

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    remaining_budget = budget.amount - budget.total_spent
    return {"remaining_budget": remaining_budget}


def total_expense(db: Session, budget_id: int, user_id: int):
    """
    Get the remaining budget for a given user and budget_id.
    
    :param db: SQLAlchemy Session
    :param budget_id: Budget ID
    :param user_id: User ID
    :return: Remaining budget amount or error if total_spent exceeds amount
    """
    try:
        # Fetch the budget from the database
        budget = db.query(Budget).filter(Budget.budget_id == budget_id, Budget.user_id == user_id).first()

        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found")

        # Check if total_spent exceeds the budget amount
        if budget.total_spent > budget.amount:
            raise HTTPException(status_code=400, detail="Exceeds budget")

        # Calculate the remaining budget
        remaining_budget = budget.amount - budget.total_spent

        # Return remaining budget as part of a dictionary
        return {"remaining_budget": remaining_budget}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to fetch remaining budget: {str(e)}")
