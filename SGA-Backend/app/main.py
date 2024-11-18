from fastapi import FastAPI, APIRouter
from app.routers import category,flyer,grocerylist,price_comparison,product,store,user_routes
from app.database import engine
from app.models import category,flyer,grocerylist,price_comparison,product,store,user

user.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()
router = APIRouter()

# Include the routers
""" app.include_router(category.router, prefix="/category")
app.include_router(flyer.router, prefix="/flyer")
app.include_router(grocerylist.router, prefix="/grocerylist")
app.include_router(price_comparison.router, prefix="/price_comparison")
app.include_router(product.router, prefix="/product")
app.include_router(store.router, prefix="/store") """
app.include_router(user_routes.router, prefix="/users")

