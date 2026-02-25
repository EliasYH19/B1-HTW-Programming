from fastapi import FastAPI
from routes import users  # Import the users router [cite: 41, 47]

# Initialize FastAPI with metadata [cite: 42, 48, 49, 50]
app = FastAPI(
    title="User Management API",
    description="FastAPI backend for managing users",
    version="1.0.0"
)

# Include the user router with the specified prefix and tags [cite: 43, 51]
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    """Root endpoint for simple health check [cite: 44, 52, 53]"""
    return {"status": "healthy", "message": "API is running"} [cite: 54]

@app.get("/health")
def detailed_health():
    """Endpoint for detailed health monitoring [cite: 45]"""
    return {"status": "healthy", "details": "All systems operational"}