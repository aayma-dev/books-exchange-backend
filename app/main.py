from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth
from app.database import engine, Base

# Create database tables
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")

# Create FastAPI app
app = FastAPI(
    title="BooksExchange API",
    description="Community-Driven Book Swapping Platform",
    version="1.0.0"
)

# Configure CORS (allows frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",        # Local React
        "http://localhost:5174",        # Vite default port
        "http://127.0.0.1:3000",        # Local alternative
        "http://127.0.0.1:5174",        # Vite alternative
        "http://10.56.94.210:3000",      # YOUR actual IP for React
        "http://10.56.94.210:5174",      # YOUR actual IP for Vite
        "http://192.168.222.1:3000",    # VMware adapter (keep for compatibility)
        "http://192.168.222.1:5174",    # VMware adapter for Vite
        "*"  # For development - allows any origin
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to BooksExchange API",
        "docs": "/docs",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}

# Run with: uvicorn app.main:app --reload --port 8000