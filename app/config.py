from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "BooksExchange"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_VERSION: str = "1.0.0"  # ← Added
    
    # CORS
    FRONTEND_URL: str = "http://localhost:3000"
    
    # File Uploads
    MAX_UPLOAD_SIZE_MB: int = 5  # ← Added
    ALLOWED_IMAGE_TYPES: str = ".jpg,.jpeg,.png,.webp"  # ← Added
    UPLOAD_DIR: str = "./uploads"  # ← Added
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60  # ← Added
    AUTH_RATE_LIMIT: int = 10  # ← Added
    
    # Logging
    LOG_LEVEL: str = "INFO"  # ← Added
    LOG_TO_FILE: bool = False  # ← Added
    LOG_FILE_PATH: str = "./logs/app.log"  # ← Added
    
    # Pydantic configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"  # This ignores extra fields instead of rejecting them
    )

# Create single instance
settings = Settings()

# Optional: Print confirmation
if settings.DEBUG:
    print("✓ Loaded configuration from .env file")
    print(f"  Database: {settings.DATABASE_URL}")
    print(f"  Environment: {settings.ENVIRONMENT}")