from app.database import TestingSessionLocal
from app.schemas.store_schema import StoreInsert
from app.crud import store_crud
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
def test_insert_store():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreInsert(
        store_name="Test Store",
        location="Test Location",
        fk_manager_id=1,
    )

    # Call the function
    inserted_store = store_crud.insert_store(db=db, store=new_store)

    # Validate results
    assert inserted_store.store_name == new_store.store_name

def test_get_all_stores():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Call the function
    all_stores = store_crud.get_all_stores(db=db)

    # Validate results
    assert len(all_stores) > 0

def test_get_store_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreInsert(
        store_name="Test Store",
        location="Test Location",
        fk_manager_id=1,
    )

    # Insert a new store
    inserted_store = store_crud.insert_store(db=db, store=new_store)

    # Call the function
    store_by_id = store_crud.get_store_by_id(db=db, store_id=inserted_store.store_id)

    # Validate results
    assert store_by_id.store_id == inserted_store.store_id

def test_update_store():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreInsert(
        store_name="Test Store",
        location="Test Location",
        fk_manager_id=1,
    )

    # Insert a new store
    inserted_store = store_crud.insert_store(db=db, store=new_store)

    # Mock updated data
    updated_store = StoreInsert(
        store_name="Updated Store",
        location="Updated Location",
        fk_manager_id=2,
    )

    # Call the function
    updated_store = store_crud.update_store(db=db, store_id=inserted_store.store_id, updates=updated_store)

    # Validate results
    assert updated_store.store_name == "Updated Store"
    assert updated_store.manager.user_id == 2

# Run the tests
test_insert_store()
test_get_all_stores()
test_get_store_by_id()
test_update_store()



