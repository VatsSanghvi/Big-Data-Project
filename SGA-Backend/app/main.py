from fastapi import FastAPI, APIRouter
from app.routers import category_routes, flyer_routes, grocerylist_routes, price_comparison_routes, product_routes, store_routes, user_routes, department_routes
from app.models import category_model, flyer_model, grocerylist_model, price_comparison_model, product_model, store_model, user_model, department_model
from app.database import engine

user_model.Base.metadata.create_all(bind=engine)
department_model.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
# flyer_model.Base.metadata.create_all(bind=engine)
# grocerylist_model.Base.metadata.create_all(bind=engine)
# price_comparison_model.Base.metadata.create_all(bind=engine)
store_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()
router = APIRouter()

# Include the routers
app.include_router(category_routes.router, prefix="/category")
# app.include_router(flyer_routes.router, prefix="/flyer")
# app.include_router(grocerylist_routes.router, prefix="/grocerylist")
# app.include_router(price_comparison_routes.router, prefix="/price_comparison")
app.include_router(product_routes.router, prefix="/products")
app.include_router(store_routes.router, prefix="/store")
app.include_router(user_routes.router, prefix="/users")
app.include_router(department_routes.router, prefix="/department")

