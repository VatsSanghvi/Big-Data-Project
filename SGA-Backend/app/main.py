from fastapi import FastAPI, APIRouter
from app.routers import category_routes, grocery_list_routes, product_routes, store_routes, user_routes, department_routes
from app.models import category_model, grocery_list_model, product_model, store_model, user_model, department_model
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

user_model.Base.metadata.create_all(bind=engine)
department_model.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
grocery_list_model.Base.metadata.create_all(bind=engine)
store_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()
router = APIRouter()

origins = [
    "http://localhost:5173",  # Add the origin of your frontend app here
    "http://127.0.0.1:5173",  # You can add more origins as needed
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins to make requests
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include the routers
app.include_router(category_routes.router, prefix="/category")
app.include_router(grocery_list_routes.router, prefix="/grocery-list")
app.include_router(product_routes.router, prefix="/products")
app.include_router(store_routes.router, prefix="/store")
app.include_router(user_routes.router, prefix="/users")
app.include_router(department_routes.router, prefix="/department")

