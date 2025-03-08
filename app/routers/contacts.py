"""Contact routes module.

This module defines API endpoints for contact operations.
"""
from typing import Annotated, List

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.models.contact import Contact
from app.services.contact_service import (
    create_contact,
    get_contact_by_id,
    get_contacts,
)

router = APIRouter(prefix="/contacts", tags=["contacts"])

# Type hint for session dependency
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=Contact)
def create_contact_endpoint(contact: Contact, session: SessionDep) -> Contact:
    """Create a new contact.

    Args:
        contact: Contact data.
        session: Database session.

    Returns:
        Contact: Created contact with ID.
    """
    return create_contact(contact, session)


@router.get("/", response_model=List[Contact])
def read_contacts_endpoint(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> List[Contact]:
    """Get paginated list of contacts.

    Args:
        session: Database session.
        offset: Number of records to skip.
        limit: Maximum number of records to return (max 100).

    Returns:
        List[Contact]: List of contacts.
    """
    return get_contacts(session, offset, limit)


@router.get("/{contact_id}", response_model=Contact)
def read_contact_endpoint(contact_id: int, session: SessionDep) -> Contact:
    """Get contact by ID.

    Args:
        contact_id: ID of the contact to retrieve.
        session: Database session.

    Returns:
        Contact: Contact record.
    """
    return get_contact_by_id(contact_id, session)