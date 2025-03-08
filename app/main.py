"""Main application module.

This module initializes and configures the FastAPI application.
"""
import uvicorn
from fastapi import FastAPI

from database import create_db_and_tables
from routers.contacts import router as contacts_router

# Create FastAPI application
app = FastAPI(
    title="Contact Management API",
    description="API for managing contact information",
    version="1.0.0",
)

# Register routers
app.include_router(contacts_router)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database and tables on application startup."""
    create_db_and_tables()


# Entry point for running the application directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7000, reload=True)