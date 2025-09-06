from fastapi import FastAPI
from app.routes import nasa  # Import our NASA routes

# Create the FastAPI application instance
app = FastAPI(
    title="NASA Urban Planning API",
    description="Backend API for NASA Space Apps Challenge project",
    version="1.0.0"
)

# Register the NASA routes under the /nasa prefix
app.include_router(nasa.router, prefix="/nasa", tags=["NASA Data"])

# Root endpoint for quick health check
@app.get("/")
def read_root():
    return {"message": "Welcome to the NASA Space Urban Planning API"}