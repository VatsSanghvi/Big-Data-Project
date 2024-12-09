from app.database import TestingSessionLocal
from app.schemas.budget_schema import BudgetCreate, BudgetBase, BudgetResponse, BudgetUpdate
from app.schemas.user_schema import UserCreate, UserLogin, PasswordUpdate, UserUpdate
from app.crud import budget_crud, user_crud
from app.models.budget_model import Budget
from app.models import user_model,store_model, product_model, department_model, category_model, grocery_list_model, budget_model
from app.database import engine
from fastapi import HTTPException
from decimal import Decimal

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    grocery_list_model.Base.metadata.create_all(bind=engine)
    budget_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_set_budget():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data for the budget
    budget_data = BudgetCreate(amount=250.00)

    # Call the function to create a budget
    created_budget = budget_crud.create_budget(db=db, user_id=1, budget=budget_data)

    # Validate the created budget
    assert created_budget is not None
    assert created_budget.user_id == 1
    assert created_budget.amount == budget_data.amount
    assert created_budget.total_spent == Decimal('0.00')  # Initial total spent should be 0


def test_update_budget():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock existing budget data
    existing_budget_id = 1
    user_id = 1
    new_amount = Decimal('1200.00')

    # Call the function to update the budget amount
    updated_budget = budget_crud.update_budget(
        db=db, 
        budget_id=existing_budget_id, 
        user_id=user_id, 
        new_amount=new_amount
    )

    # Validate the updated budget
    assert updated_budget is not None
    assert updated_budget.amount == Decimal('1200.00')


def test_reset_budget():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock existing budget data
    existing_budget_id = 1
    user_id = 1

    # Call the function to reset the budget
    reset_message = budget_crud.reset_budget(
        db=db, 
        budget_id=existing_budget_id, 
        user_id=user_id
    )

    # Fetch the budget from the database to validate reset
    budget = db.query(Budget).filter(
        Budget.budget_id == existing_budget_id, 
        Budget.user_id == user_id
    ).first()

    # Assertions
    assert reset_message == "Budget reset successfully"
    assert budget is not None
    assert budget.total_spent == Decimal('0.00')

def test_get_remaining_budget():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock budget data in the database
    existing_budget_id = 1
    user_id = 1

    # Call the CRUD function to get the remaining budget
    result = budget_crud.get_remaining_budget(
        db=db,
        budget_id=existing_budget_id,
        user_id=user_id
    )

    # Debugging step: print result to ensure it's correct
    print(f"Result: {result}")

    # Fetch the budget from the database for validation
    budget = db.query(Budget).filter(
        Budget.budget_id == existing_budget_id,
        Budget.user_id == user_id
    ).first()

    # Calculate expected remaining budget
    expected_remaining_budget = budget.amount - budget.total_spent

    # Assertions
    assert result["remaining_budget"] == expected_remaining_budget
    assert budget is not None
    assert budget.budget_id == existing_budget_id


def test_get_remaining_budget_exceeds_budget():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock budget data in the database where total_spent exceeds amount
    existing_budget_id = 1
    user_id = 1

    # Fetch the budget from the database
    budget = db.query(Budget).filter(
        Budget.budget_id == existing_budget_id,
        Budget.user_id == user_id
    ).first()

    # Manually set the total_spent to a value greater than the amount for this test
    budget.total_spent = budget.amount + 1  # Exceeds the budget

    # Log the values for debugging
    print(f"Test - Budget Amount: {budget.amount}, Total Spent: {budget.total_spent}")

    db.commit()

    try:
        # Call the CRUD function to get the remaining budget
        result = budget_crud.total_expense(
            db=db,
            budget_id=existing_budget_id,
            user_id=user_id
        )
    except HTTPException as e:
        # Assertions
        assert e.status_code == 400
        assert e.detail == "Exceeds budget"
        print(f"Error: {e.detail}")
        return  # Test passed as error was raised

    # If no exception was raised, the test should fail
    assert False, "Expected HTTPException for exceeding budget"
