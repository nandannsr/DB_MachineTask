"""Contact service layer.

This module contains business logic for contact operations.
"""
from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.contact import Contact


def create_contact(contact: Contact, session: Session) -> Contact:
    """Create a new contact if not already registered.

    Args:
        contact: Contact model with data to be saved.
        session: Database session.

    Returns:
        Contact: Newly created contact with ID.

    Raises:
        HTTPException: If contact with same name and email already exists.
    """
    stmt = select(Contact).where(
        Contact.name == contact.name, 
        Contact.email == contact.email
    )
    result = session.execute(stmt)
    
    if result.first():
        raise HTTPException(
            status_code=400, 
            detail="Contact already registered"
        )
    
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return contact


def get_contacts(session: Session, offset: int = 0, limit: int = 100) -> list[Contact]:
    """Retrieve a list of contacts with pagination.

    Args:
        session: Database session.
        offset: Number of records to skip.
        limit: Maximum number of records to return.

    Returns:
        list[Contact]: List of contact records.
    """
    contacts = session.exec(
        select(Contact).offset(offset).limit(limit)
    ).all()
    return contacts


def get_contact_by_id(contact_id: int, session: Session) -> Contact:
    """Retrieve a contact by ID.

    Args:
        contact_id: ID of the contact to retrieve.
        session: Database session.

    Returns:
        Contact: Contact record.

    Raises:
        HTTPException: If contact with the specified ID does not exist.
    """
    contact = session.get(Contact, contact_id)
    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )
    return contact