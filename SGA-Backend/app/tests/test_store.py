from app.database import TestingSessionLocal
from app.schemas.store_schema import StoreCreateRequest, StoreUpdateRequest
from app.crud import store_crud
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
def test_insert_store():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreCreateRequest(
        store_name="Walmart",
        location="Waterloo",
        fk_owner_id=1,
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
    all_stores = store_crud.get_stores(db=db)

    # Validate results
    assert len(all_stores) > 0

def test_get_store_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreCreateRequest(
        store_name="Test Store",
        location="Test Location",
        fk_owner_id=1,
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
    new_store = StoreCreateRequest(
        store_name="Test Store",
        location="Test Location",
        fk_owner_id=1,
    )

    # Insert a new store
    inserted_store = store_crud.insert_store(db=db, store=new_store)

    # Mock updated data
    updated_store = StoreUpdateRequest(
        store_name="Walmart",
        location="Target",
        manager_email="andre_manager@gmail.com"
    )

    # Call the function
    updated_store = store_crud.update_store(db=db, store_id=inserted_store.store_id, updates=updated_store)

    # Validate results
    assert updated_store.store_name == "Walmart"

def test_delete_store():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_store = StoreCreateRequest(
        store_name="Test Store",
        location="Test Location",
        fk_owner_id=1,
    )

    # Insert a new store
    inserted_store = store_crud.insert_store(db=db, store=new_store)

    # Call the function
    deleted_store = store_crud.delete_store(db=db, store_id=inserted_store.store_id)

    # Validate results
    assert deleted_store == f"Store {inserted_store.store_name} deleted successfully."