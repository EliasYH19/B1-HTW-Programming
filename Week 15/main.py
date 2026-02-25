from fastapi import FastAPI
from routes import users  # Import the users router 

# Initialize FastAPI with metadata 
app = FastAPI(
    title="User Management API",
    description="FastAPI backend for managing users",
    version="1.0.0"
)

# Include the user router with the specified tags
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API is running"} 

@app.get("/health")
def detailed_health():

    return {"status": "healthy", "details": "All systems operational"}

