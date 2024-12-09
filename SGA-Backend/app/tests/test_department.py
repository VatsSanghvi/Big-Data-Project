from app.database import TestingSessionLocal
from app.schemas.department_schema import DepartmentCreate
from app.crud import department_crud
from app.models import user_model,category_model, department_model, product_model, store_model, grocery_list_model, budget_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    budget_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    grocery_list_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testing the function
def test_insert_department():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_department = DepartmentCreate(
        department_name="Electronics",
        fk_store_id=1
    )

    # Call the function
    inserted_department = department_crud.insert_department(db=db, department=new_department)

    # Validate results
    assert inserted_department.department_name == new_department.department_name

def test_get_all_departments():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Call the function
    all_departments = department_crud.get_all_departments(db=db)

    # Validate results
    assert len(all_departments) > 0

def test_get_department_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_department = DepartmentCreate(
        department_name="Test department",
        fk_store_id=1
    )

    # Insert a new department
    inserted_department = department_crud.insert_department(db=db, department=new_department)

    # Call the function
    department_by_id = department_crud.get_department_by_id(db=db, department_id=inserted_department.department_id)

    # Validate results
    assert department_by_id.department_id == inserted_department.department_id

def test_update_department():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_department = DepartmentCreate(
        department_name="Test department",
        fk_store_id=1
    )

    # Insert a new department
    inserted_department = department_crud.insert_department(db=db, department=new_department)

    # Mock updated data
    updated_department = DepartmentCreate(
        department_name="Home Appliances",
        fk_store_id=1
    )

    # Call the function
    updated_department = department_crud.update_department(db=db, department_id=inserted_department.department_id, updates=updated_department)

    # Validate results
    assert updated_department.department_name == "Home Appliances"

def test_delete_department():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_department = DepartmentCreate(
        department_name="Electronics",
        fk_store_id=1
    )

    # Insert a new department
    inserted_department = department_crud.insert_department(db=db, department=new_department)

    # Call the function
    deleted_department = department_crud.delete_department(db=db, department_id=inserted_department.department_id)

    # Validate results
    assert deleted_department == f"Department {inserted_department.department_name} deleted successfully."


