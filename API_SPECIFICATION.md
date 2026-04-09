# BooksExchange API Documentation

## Base URL
`http://localhost:8000`

## Authentication Endpoints

### POST `/api/auth/register`
Register a new user

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "booklover",
  "password": "securepass123",
  "full_name": "John Doe"  // optional
}