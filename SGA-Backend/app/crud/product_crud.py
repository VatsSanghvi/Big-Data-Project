from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.store_model import Store
from app.models.department_model import Department
from app.models.category_model import Category
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreateRequest, ProductResponse

def insert_product(db: Session, product: ProductCreateRequest):
    """
    Insert a Product record into the database.

    :param db: SQLAlchemy database session.
    :param product: ProductCreateRequest DTO to be inserted.
    :return: ProductResponse object representing the inserted product.
    """
    try:
        # Map DTO to SQLAlchemy Product object
        product_obj = Product(
            product_name=product.product_name,
            stock_quantity=product.stock_quantity,
            price=product.price,
            fk_category_id=product.fk_category_id,
            fk_department_id=product.fk_department_id,
            fk_store_id=product.fk_store_id,
        )
        
        # Add and commit the product
        db.add(product_obj)
        db.commit()

        # Refresh the object to get updated values
        db.refresh(product_obj)

        # Convert to Pydantic model for returning
        return ProductResponse.model_validate(product_obj)

    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert product: {str(e)}") from e
    
def get_products_by_owner(owner_id: int, db: Session):
    """
    Retrieve all Product records from the database.

    :param db: SQLAlchemy database session.
    :return: List of ProductResponse objects.
    """
    products = []
    stores = db.query(Store).filter(Store.fk_owner_id == owner_id).all()
    if not stores:
        raise RuntimeError("No stores found.")
    for store in stores:
        products_by_store = db.query(Product).filter(Product.fk_store_id == store.store_id).all()
        products.extend(products_by_store)

    return [ProductResponse.model_validate(product) for product in products]

def get_all_products(db: Session):
    """
    Retrieve all Product records from the database.

    :param db: SQLAlchemy database session.
    :return: List of ProductResponse objects.
    """
    products = db.query(Product).all()
    return [ProductResponse.model_validate(product) for product in products]

def update_product(db: Session, product_id: int, updates: ProductCreateRequest):
    """
    Update a Product record in the database.

    :param db: SQLAlchemy database session.
    :param product_id: ID of the product to update.
    :param updates: ProductCreateRequest DTO containing the updated data.
    :return: ProductResponse object representing the updated product.
    :raises: RuntimeError if the product is not found.
    """
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise RuntimeError(f"Product with ID {product_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    try:
        db.commit()
        db.refresh(product)
        return ProductResponse.model_validate(product)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update product: {str(e)}") from e

def delete_product(db: Session, product_id: int):
    """
    Delete a Product record from the database.

    :param db: SQLAlchemy database session.
    :param product_id: ID of the product to delete.
    :raises: RuntimeError if the product is not found.
    """
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise RuntimeError(f"Product with ID {product_id} not found.")

    try:
        db.delete(product)
        db.commit()

        return f"Product {product.product_name} deleted successfully."
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete product: {str(e)}") from e