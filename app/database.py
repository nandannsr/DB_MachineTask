"""Database connection and session management.

This module provides functions for database connection,
session creation, and database initialization.
"""
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

# Database configuration
SQLITE_FILE_NAME = "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

# Create engine with thread safety for SQLite
connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)


def create_db_and_tables() -> None:
    """Initialize database and create tables based on SQLModel definitions."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Provide a database session for dependency injection.

    Yields:
        Session: SQLModel database session.
    """
    with Session(engine) as session:
        yield session