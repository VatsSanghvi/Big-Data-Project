from app.database import TestingSessionLocal
from app.schemas.category_schema import CategoryInsert
from app.crud import category_crud
from app.models import user_model,category_model, department_model, product_model, store_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testing the function
def test_insert_category():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_category = CategoryInsert(
        category_name="Test Category",
        fk_department_id=1
    )

    # Call the function
    inserted_category = category_crud.insert_category(db=db, category=new_category)

    # Validate results
    assert inserted_category.category_name == new_category.category_name

def test_get_all_categories():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Call the function
    all_categories = category_crud.get_all_categories(db=db)

    # Validate results
    assert len(all_categories) > 0

def test_get_category_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_category = CategoryInsert(
        category_name="Test Category",
        fk_department_id=1
    )

    # Insert a new category
    inserted_category = category_crud.insert_category(db=db, category=new_category)

    # Call the function
    category_by_id = category_crud.get_category_by_id(db=db, category_id=inserted_category.category_id)

    # Validate results
    assert category_by_id.category_id == inserted_category.category_id

def test_update_category():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_category = CategoryInsert(
        category_name="Test Category",
        fk_department_id=1
    )

    # Insert a new category
    inserted_category = category_crud.insert_category(db=db, category=new_category)

    # Mock updated data
    updated_category = CategoryInsert(
        category_name="Updated Category",
        fk_department_id=2
    )

    # Call the function
    updated_category = category_crud.update_category(db=db, category_id=inserted_category.category_id, updates=updated_category)

    # Validate results
    assert updated_category.category_name == "Updated Category"
    assert updated_category.fk_department_id == 2

# Run the tests
test_insert_category()
test_get_all_categories()
test_get_category_by_id()
test_update_category()



