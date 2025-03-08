"""Contact data models.

This module contains SQLModel-based models for contact management.
"""
from sqlmodel import Field, SQLModel


class Contact(SQLModel, table=True):
    """Contact model for storing contact information.

    Attributes:
        id: Unique identifier for the contact.
        name: Full name of the contact.
        email: Email address of the contact.
        message: Message or notes associated with the contact.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    message: str