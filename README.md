# Books Exchange Platform - Backend API

RESTful API backend for a books exchange platform where users can list, exchange, and request books.

## About The Project

This backend service handles user authentication, book listings, and exchange requests. Users can register, login, browse available books, list their own books for exchange, and request books from other users.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLite** - Lightweight database
- **SQLAlchemy** - ORM for database operations
- **JWT** - JSON Web Tokens for authentication
- **Python 3.13+**

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{id}` | Get specific book |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |


