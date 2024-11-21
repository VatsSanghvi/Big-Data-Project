from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductInsert, ProductResponse

def insert_product(db: Session, product: ProductInsert) -> ProductResponse:
    """
    Insert a Product record into the database.

    :param db: SQLAlchemy database session.
    :param product: ProductInsert DTO to be inserted.
    :return: ProductResponse object representing the inserted product.
    """
    try:
        # Map DTO to SQLAlchemy Product object
        product_obj = Product(
            product_name=product.product_name,
            stock_quantity=product.stock_quantity,
            price=product.price,
            status=product.status,
            unit_of_measure=product.unit_of_measure,
            ingredients=product.ingredients,
            price_valid_from=product.price_valid_from,
            price_valid_to=product.price_valid_to,
            category_id=product.category_id,
            department_id=product.department_id,
            store_id=product.store_id,
        )
        
        # Add and commit the product
        db.add(product_obj)
        db.commit()

        # Refresh the object to get updated values (e.g., auto-generated ID)
        db.refresh(product_obj)

        # Convert to Pydantic model for returning
        return ProductResponse.model_validate(product_obj)

    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        raise RuntimeError(f"Failed to insert product: {str(e)}") from e
    
def get_all_products(db: Session) -> List[ProductResponse]:
    """
    Retrieve all Product records from the database.

    :param db: SQLAlchemy database session.
    :return: List of ProductResponse objects.
    """
    products = db.query(Product).all()
    return [ProductResponse.model_validate(product) for product in products]

def get_product_by_id(db: Session, product_id: int) -> ProductResponse:
    """
    Retrieve a single Product record by its ID.

    :param db: SQLAlchemy database session.
    :param product_id: ID of the product to retrieve.
    :return: ProductResponse object if found.
    :raises: RuntimeError if the product is not found.
    """
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise RuntimeError(f"Product with ID {product_id} not found.")
    return ProductResponse.model_validate(product)

def update_product(db: Session, product_id: int, updates: ProductInsert) -> ProductResponse:
    """
    Update a Product record in the database.

    :param db: SQLAlchemy database session.
    :param product_id: ID of the product to update.
    :param updates: ProductInsert DTO containing the updated data.
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

def delete_product(db: Session, product_id: int) -> None:
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
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to delete product: {str(e)}") from e
