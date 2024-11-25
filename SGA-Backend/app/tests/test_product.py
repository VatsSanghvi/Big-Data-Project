from datetime import date
from app.database import TestingSessionLocal
from app.schemas.product_schema import ProductInsert
from app.crud import product_crud
from app.models import user_model, department_model, category_model, product_model, store_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testing the function
def test_insert_product():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_product = ProductInsert(
        product_name="Test product",
        stock_quantity=10,
        price=20.00,
        status="In Stock",
        unit_of_measure="kg",
        ingredients="Test ingredients",
        price_valid_from=date(2021, 1, 1),
        price_valid_to=date(2021, 12, 31),
        fk_department_id=1,
        fk_category_id=1,
        fk_store_id=1
    )

    # Call the function
    inserted_product = product_crud.insert_product(db=db, product=new_product)

    # Validate results
    assert inserted_product.product_name == new_product.product_name

def test_get_all_products():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Call the function
    all_products = product_crud.get_all_products(db=db)

    # Validate results
    assert len(all_products) > 0

def test_get_product_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_product = ProductInsert(
        product_name="Test product",
        stock_quantity=10,
        price=20.00,
        status="In Stock",
        unit_of_measure="kg",
        ingredients="Test ingredients",
        price_valid_from=date(2021, 1, 1),
        price_valid_to=date(2021, 12, 31),
        fk_department_id=1,
        fk_category_id=1,
        fk_store_id=1
    )

    # Insert a new product
    inserted_product = product_crud.insert_product(db=db, product=new_product)

    # Call the function
    product_by_id = product_crud.get_product_by_id(db=db, product_id=inserted_product.product_id)

    # Validate results
    assert product_by_id.product_id == inserted_product.product_id

def test_update_product():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_product = ProductInsert(
        product_name="Test product",
        stock_quantity=10,
        price=20.00,
        status="In Stock",
        unit_of_measure="kg",
        ingredients="Test ingredients",
        price_valid_from=date(2021, 1, 1),
        price_valid_to=date(2021, 12, 31),
        fk_department_id=1,
        fk_category_id=1,
        fk_store_id=1
    )

    # Insert a new product
    inserted_product = product_crud.insert_product(db=db, product=new_product)

    # Mock updated data
    updated_product = ProductInsert(
        product_name="Updated product",
        stock_quantity=20,
        price=40.00,
        status="In Stock",
        unit_of_measure="kg",
        ingredients="Test ingredients updated",
        price_valid_from=date(2022, 2, 2),
        price_valid_to=date(2022, 12, 31),
        fk_department_id=2,
        fk_category_id=2,
        fk_store_id=2
    )

    # Call the function
    updated_product = product_crud.update_product(db=db, product_id=inserted_product.product_id, updates=updated_product)

    # Validate results
    assert updated_product.product_name == "Updated product"
    assert updated_product.department.department_id == 2

# Run the tests
test_insert_product()
test_get_all_products()
test_get_product_by_id()
test_update_product()



