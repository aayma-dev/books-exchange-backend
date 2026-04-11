from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app import schemas, models, utils
from app.database import get_db
from app.config import settings

router = APIRouter(prefix="/api/auth", tags=["authentication"])

@router.post("/register", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = utils.auth.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        city=user.city,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.auth.create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    
    # Return user data with token
    user_response = schemas.UserResponse(
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        city=db_user.city,
        is_active=db_user.is_active
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_response
    }

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    # Authenticate user
    user = utils.auth.authenticate_user(db, user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    # Return user data with token
    user_response = schemas.UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        city=user.city,
        is_active=user.is_active
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_response
    }

@router.post("/logout")
def logout():
    # Since we're using JWT tokens, logout is handled client-side
    # by removing the token from storage
    return {"message": "Successfully logged out"}
@router.get("/me", response_model=schemas.UserResponse)
def get_current_user(current_user: models.User = Depends(utils.auth.get_current_active_user)):
    return schemas.UserResponse(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        city=current_user.city,
        is_active=current_user.is_active
    )