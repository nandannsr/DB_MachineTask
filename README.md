# Contact Management API

A FastAPI application for managing contacts with SQLModel and SQLite.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── contact.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── contacts.py
│   └── services/
│       ├── __init__.py
│       └── contact_service.py
└── README.md
```

## Running the Application

```bash
# Install dependencies
pip install fastapi uvicorn sqlmodel

# Run the application
python -m app.main
```

## API Endpoints

- `POST /contacts/` - Create a new contact
- `GET /contacts/` - Get a list of contacts with pagination
- `GET /contacts/{contact_id}` - Get a specific contact by ID

## Swagger Documentation

Access the API documentation at `http://127.0.0.1:7000/docs` after starting the application.