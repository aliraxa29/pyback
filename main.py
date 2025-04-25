from fastapi import FastAPI
from pyback.model_loader import register_all_models
from pyback.router import router as crud_router
from pyback.method_router import router as method_router

app = FastAPI()

# Register Models
register_all_models()

# Include API Routers
app.include_router(crud_router)
app.include_router(method_router)