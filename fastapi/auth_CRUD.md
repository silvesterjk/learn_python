# FastAPI Authentication & CRUD Operations

## Table of Contents
1. [JWT Implementation](#jwt-implementation)
2. [Password Security](#password-security)
3. [CRUD Operations](#crud-operations)
4. [Combining Auth + CRUD](#combining-auth--crud)
5. [Real-World Implementation](#real-world-implementation)
6. [Testing](#testing)

### Common Authentication Methods in FastAPI

#### 1. OAuth2 with Password (and Bearer)
Most common for APIs - uses tokens for stateless authentication.

#### 2. API Keys
Simple but less secure - good for service-to-service communication.

#### 3. Session-based 
Traditional web authentication using cookies.
```
fastapi-app/
│
├── app/                          # Main application package
│   ├── __init__.py
│   ├── main.py                   # FastAPI app instance and startup
│   ├── config.py                 # Configuration settings
│   │
│   ├── core/                     # Core functionality
│   │   ├── __init__.py
│   │   ├── security.py           # JWT, password hashing, authentication
│   │   ├── database.py           # Database connection and session
│   │   └── deps.py               # Common dependencies
│   │
│   ├── models/                   # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py               # User database model
│   │   └── item.py               # Item database model
│   │
│   ├── schemas/                  # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py               # User Pydantic models
│   │   ├── item.py               # Item Pydantic models
│   │   └── token.py              # Token schemas
│   │
│   ├── crud/                     # CRUD operations
│   │   ├── __init__.py
│   │   ├── base.py               # Base CRUD class
│   │   ├── user.py               # User CRUD operations
│   │   └── item.py               # Item CRUD operations 
│   │
│   ├── api/                      # API routes
│   │   ├── __init__.py
│   │   ├── api_v1/               # Version 1 of API
│   │   │   ├── __init__.py
│   │   │   ├── api.py            # API router aggregation
│   │   │   └── endpoints/        # Individual endpoint files
│   │   │       ├── __init__.py
│   │   │       ├── auth.py       # Authentication endpoints
│   │   │       ├── users.py      # User CRUD endpoints
│   │   │       └── items.py      # Item CRUD endpoints
│   │   └── deps.py               # API-specific dependencies
│   │
│   ├── services/                 # Business logic layer
│   │   ├── __init__.py
│   │   ├── user_service.py       # User business logic
│   │   └── item_service.py       # Item business logic
│   │
│   └── utils/                    # Utility functions
│       ├── __init__.py
│       ├── validators.py         # Input validation functions
│       └── exceptions.py         # Custom exception classes
│
├── tests/                        # Test files
│   ├── __init__.py
│   ├── conftest.py               # Pytest configuration and fixtures
│   ├── test_main.py              # Main app tests
│   │
│   ├── api/                      # API endpoint tests
│   │   ├── __init__.py
│   │   ├── test_auth.py          # Authentication tests
│   │   ├── test_users.py         # User endpoint tests
│   │   └── test_items.py         # Item endpoint tests
│   │
│   ├── crud/                     # CRUD operation tests
│   │   ├── __init__.py
│   │   ├── test_user_crud.py     # User CRUD tests
│   │   └── test_item_crud.py     # Item CRUD tests
│   │
│   └── utils/                    # Utility tests
│       ├── __init__.py
│       └── test_validators.py    # Validation tests
│
├── alembic/                      # Database migrations
│   ├── versions/                 # Migration files
│   ├── env.py                    # Alembic configuration
│   ├── script.py.mako            # Migration template
│   └── alembic.ini               # Alembic settings
│
├── scripts/                      # Utility scripts
│   ├── create_superuser.py       # Create admin user script
│   ├── init_db.py                # Initialize database
│   └── populate_data.py          # Seed database with sample data
│
├── .env                          # Environment variables (not in git)
├── .env.example                  # Example environment file
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── requirements-dev.txt          # Development dependencies
├── pyproject.toml               # Project configuration
├── README.md                     # Project documentation
├── Dockerfile                    # Docker configuration
├── docker-compose.yml           # Docker Compose setup
└── pytest.ini                   # Pytest configuration
```

## JWT Implementation

### Required Dependencies
```bash
pip install fastapi[all] python-jose[cryptography] passlib[bcrypt] python-multipart
```

### Basic JWT Setup

```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

# Configuration
SECRET_KEY = "your-secret-key-here"  # Use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

### User Models

```python
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
```

### Authentication Functions

```python
def verify_password(plain_password, hashed_password):
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Hash a password"""
    return pwd_context.hash(password)

def authenticate_user(fake_users_db, username: str, password: str):
    """Authenticate a user"""
    user = get_user(fake_users_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current user from JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """Get current active user (not disabled)"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
```

### Authentication Endpoints

```python
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login endpoint - returns JWT token"""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    """Register a new user"""
    if user.username in fake_users_db:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    hashed_password = get_password_hash(user.password)
    user_dict = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    fake_users_db[user.username] = UserInDB(**user_dict)
    return User(**user_dict)

@auth_router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user info"""
    return current_user
```

## Password Security

### Best Practices

```python
from passlib.context import CryptContext
import secrets

# Strong password context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12  # Higher rounds = more secure but slower
)

def generate_secure_secret_key():
    """Generate a cryptographically secure secret key"""
    return secrets.token_urlsafe(32)

def validate_password_strength(password: str) -> bool:
    """Validate password meets security requirements"""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        return False
    return True

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    
    @validator('password')
    def validate_password(cls, v):
        if not validate_password_strength(v):
            raise ValueError('Password must be at least 8 characters with uppercase, lowercase, number, and special character')
        return v
```

## CRUD Operations

### Database Setup with SQLAlchemy

```python
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# For PostgreSQL: "postgresql://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="items")

# Create tables
Base.metadata.create_all(bind=engine)
```

### Pydantic Schemas

```python
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

# Item schemas
class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Item(ItemBase):
    id: int
    owner_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserWithItems(User):
    items: List[Item] = []
```

### Database Dependency

```python
from sqlalchemy.orm import Session

def get_db():
    """Database dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### CRUD Operations

```python
from sqlalchemy.orm import Session
from typing import List, Optional

class UserCRUD:
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()
    
    def create_user(self, db: Session, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def update_user(self, db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        db_user = self.get_user(db, user_id)
        if not db_user:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
        
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def delete_user(self, db: Session, user_id: int) -> bool:
        db_user = self.get_user(db, user_id)
        if not db_user:
            return False
        db.delete(db_user)
        db.commit()
        return True

class ItemCRUD:
    def get_item(self, db: Session, item_id: int) -> Optional[Item]:
        return db.query(Item).filter(Item.id == item_id).first()
    
    def get_items(self, db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.query(Item).offset(skip).limit(limit).all()
    
    def get_user_items(self, db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.query(Item).filter(Item.owner_id == user_id).offset(skip).limit(limit).all()
    
    def create_item(self, db: Session, item: ItemCreate, user_id: int) -> Item:
        db_item = Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def update_item(self, db: Session, item_id: int, item_update: ItemUpdate) -> Optional[Item]:
        db_item = self.get_item(db, item_id)
        if not db_item:
            return None
        
        update_data = item_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)
        
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def delete_item(self, db: Session, item_id: int) -> bool:
        db_item = self.get_item(db, item_id)
        if not db_item:
            return False
        db.delete(db_item)
        db.commit()
        return True

# Create instances
user_crud = UserCRUD()
item_crud = ItemCRUD()
```

## Combining Auth + CRUD

### Protected CRUD Endpoints

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Users router
users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all users (admin only)"""
    if not current_user.is_admin:  # Add admin check
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return user_crud.get_users(db, skip=skip, limit=limit)

@users_router.get("/me", response_model=UserWithItems)
async def read_user_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get current user with their items"""
    return current_user

@users_router.put("/me", response_model=User)
async def update_user_me(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update current user"""
    updated_user = user_crud.update_user(db, current_user.id, user_update)
    return updated_user

@users_router.delete("/me")
async def delete_user_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete current user account"""
    success = user_crud.delete_user(db, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Account deleted successfully"}

# Items router
items_router = APIRouter(prefix="/items", tags=["items"])

@items_router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all items (public)"""
    return item_crud.get_items(db, skip=skip, limit=limit)

@items_router.get("/my-items", response_model=List[Item])
async def read_my_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get current user's items"""
    return item_crud.get_user_items(db, current_user.id, skip=skip, limit=limit)

@items_router.post("/", response_model=Item)
async def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create new item"""
    return item_crud.create_item(db, item, current_user.id)

@items_router.get("/{item_id}", response_model=Item)
async def read_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get specific item"""
    item = item_crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@items_router.put("/{item_id}", response_model=Item)
async def update_item(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update item (owner only)"""
    item = item_crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    updated_item = item_crud.update_item(db, item_id, item_update)
    return updated_item

@items_router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete item (owner only)"""
    item = item_crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    success = item_crud.delete_item(db, item_id)
    return {"message": "Item deleted successfully"}
```

## Real-World Implementation

### Complete Application Structure

```python
# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, users, items
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Secure API",
    description="API with JWT authentication and CRUD operations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Welcome to My Secure API"}
```

### Environment Configuration

```python
# config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./test.db"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### Error Handling

```python
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "path": request.url.path
        }
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": str(exc),
            "status_code": 400,
            "path": request.url.path
        }
    )
```

## Testing

### Test Setup

```python
# test_main.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..database import get_db, Base

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
```

### Authentication Tests

```python
def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "full_name": "Test User",
            "password": "TestPass123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert "password" not in data

def test_login():
    # First register a user
    client.post("/auth/register", json={
        "username": "testuser2",
        "email": "test2@example.com", 
        "full_name": "Test User 2",
        "password": "TestPass123!"
    })
    
    # Then login
    response = client.post(
        "/auth/token",
        data={"username": "testuser2", "password": "TestPass123!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials():
    response = client.post(
        "/auth/token",
        data={"username": "nonexistent", "password": "wrong"}
    )
    assert response.status_code == 401

def get_auth_headers():
    """Helper function to get authentication headers"""
    login_response = client.post(
        "/auth/token",
        data={"username": "testuser", "password": "TestPass123!"}
    )
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

### CRUD Tests

```python
def test_create_item():
    headers = get_auth_headers()
    response = client.post(
        "/items/",
        json={"title": "Test Item", "description": "Test Description"},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "Test Description"

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_my_items():
    headers = get_auth_headers()
    response = client.get("/items/my-items", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item():
    headers = get_auth_headers()
    
    # Create item first
    create_response = client.post(
        "/items/",
        json={"title": "Original Title", "description": "Original Description"},
        headers=headers
    )
    item_id = create_response.json()["id"]
    
    # Update item
    update_response = client.put(
        f"/items/{item_id}",
        json={"title": "Updated Title"},
        headers=headers
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Original Description"  # Unchanged

def test_delete_item():
    headers = get_auth_headers()
    
    # Create item first
    create_response = client.post(
        "/items/",
        json={"title": "To Delete", "description": "Will be deleted"},
        headers=headers
    )
    item_id = create_response.json()["id"]
    
    # Delete item
    delete_response = client.delete(f"/items/{item_id}", headers=headers)
    assert delete_response.status_code == 200
    
    # Verify item is deleted
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404

def test_unauthorized_operations():
    # Try to create item without authentication
    response = client.post(
        "/items/",
        json={"title": "Test", "description": "Test"}
    )
    assert response.status_code == 401
    
    # Try to access protected endpoints
    response = client.get("/users/me")
    assert response.status_code == 401
```

## Best Practices

### Security Best Practices

1. **Environment Variables**
```python
import os
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-key-for-development")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
```

2. **Password Validation**
```python
def validate_password_policy(password: str):
    """Implement organization password policy"""
    errors = []
    if len(password) < 12:
        errors.append("Password must be at least 12 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain lowercase letter")
    if not re.search(r"\d", password):
        errors.append("Password must contain number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain special character")
    return errors
```

3. **Rate Limiting**
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/auth/token")
@limiter.limit("5/minute")
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # Login logic
    pass
```

4. **Input Validation**
```python
from pydantic import validator
import re

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not re.match("^[a-zA-Z0-9_]+$", v):
            raise ValueError('Username must be alphanumeric')
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        return v
    
    @validator('email')
    def email_valid(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email format')
        return v.lower()
```

### Performance Best Practices

1. **Database Indexing**
```python
# Add indexes for frequently queried fields
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)  # Indexed for lookups
    email = Column(String, unique=True, index=True)     # Indexed for lookups
    created_at = Column(DateTime, default=datetime.utcnow, index=True)  # For sorting
```

2. **Query Optimization**
```python
def get_user_with_items(db: Session, user_id: int):
    """Use eager loading to avoid N+1 queries"""
    return db.query(User).options(joinedload(User.items)).filter(User.id == user_id).first()
```

3. **Pagination**
```python
from fastapi import Query

@router.get("/items/")
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    total = db.query(Item).count()
    return {
        "items": items,
        "total": total,
        "skip": skip,
        "limit": limit
    }
```

### Code Organization Best Practices

1. **Dependency Injection for Services**
```python
class UserService:
    def __init__(self, user_crud: UserCRUD):
        self.user_crud = user_crud
    
    async def register_user(self, db: Session, user_data: UserCreate):
        # Business logic here
        existing_user = self.user_crud.get_user_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.user_crud.create_user(db, user_data)

def get_user_service() -> UserService:
    return UserService(user_crud)
```

2. **Middleware for Logging**
```python
import logging
import time

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.4f}s"
    )
    return response
```

3. **Error Responses**
```python
class ErrorResponse(BaseModel):
    detail: str
    code: str
    timestamp: datetime
    path: str

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content=ErrorResponse(
            detail=exc.detail,
            code="NOT_FOUND",
            timestamp=datetime.utcnow(),
            path=request.url.path
        ).dict()
    )
```


