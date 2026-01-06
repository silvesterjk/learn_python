# JWT Authentication in FastAPI

## What is JWT?
**JWT (JSON Web Token)** is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

### Key Characteristics
- **Stateless**: No server side-session storage required
- **Self-contained**: All necessary information is in the token itself
- **Compact**: Small size, suitable for URLs, HTTP headers, and HTML form parameters
- **Secure**: Digitally signed to prevent tampering

## How JWT Works

### The Flow
1. **User Login**: Client sends credentials to server
2. **Server Validation**: Server verifies credentials
3. **Token Generation**: Server creates a signed JWT containing user info
4. **Token Return**: Server sends JWT back to client
5. **Token Storage**: Client stores JWT (usually in localStorage or httpOnly cookie)
6. **Authenticated Requests**: Client includes JWT in subsequent requests
7. **Token Verification**: Server validates JWT signature and extracts user info

### JWT Structure

A JWT consists of three parts separated by dots (`.`): 

```
header.payload.signature
```

#### Example JWT:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

#### 1. Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
- `alg`: Algorithm used for signing (e.g., HS256, RS256)
- `typ`: Token type (always "JWT")

#### 2. Payload (Claims)
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "exp": 1516242622
}
```
- `sub`: Subject (user ID)
- `iat`: Issued at (timestamp)
- `exp`: Expiration time (timestamp)
- Custom claims can be added

#### 3. Signature
```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

## Why Use JWT for Authentication?

### Advantages
- **Stateless**: No server-side session storage
- **Scalable**: Works well with microservices and distributed systems
- **Cross-domain**: Can be used across different domains
- **Mobile-friendly**: No cookies required
- **Self-contained**: All user info in the token
- **Performance**: Fast validation (no database lookup)

### Disadvantages
- **Token size**: Larger than session IDs
- **Revocation complexity**: Hard to invalidate before expiration
- **Security concerns**: Must be stored securely on client
- **No automatic refresh**: Requires implementation

## FastAPI JWT Implementation

### Required Dependencies

```bash
pip install python-jose[cryptography] passlib[bcrypt] python-multipart
```

### Basic Setup

#### 1. Configuration and Imports

```python
from datetime import datetime, timedelta
from typing import Optional, Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# Configuration
SECRET_KEY = "your-secret-key-here"  # Use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
```

#### 2. Data Models

```python
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str
```

#### 3. Utility Functions

```python
# Fake database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
    }
}

def verify_password(plain_password, hashed_password):
    """Verify a plain password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Hash a password."""
    return pwd_context.hash(password)

def get_user(db, username: str):
    """Get user from database."""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    """Authenticate user credentials."""
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current user from JWT token."""
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
    """Get current active user."""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
```

#### 4. Authentication Endpoints

```python
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login endpoint that returns JWT token."""
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

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user info."""
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    """Get current user's items."""
    return [{"item_id": "Foo", "owner": current_user.username}]

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    """Example protected route."""
    return {"message": f"Hello {current_user.username}, this is a protected route!"}
```

## Advanced JWT Implementation

### 1. Refresh Token Pattern

```python
from uuid import uuid4

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

# Store refresh tokens (use Redis in production)
refresh_tokens_db = {}

def create_refresh_token(username: str):
    """Create a refresh token."""
    refresh_token = str(uuid4())
    refresh_tokens_db[refresh_token] = {
        "username": username,
        "created_at": datetime.utcnow()
    }
    return refresh_token

@app.post("/token", response_model=TokenResponse)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    # Create refresh token
    refresh_token = create_refresh_token(user.username)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@app.post("/refresh", response_model=Token)
async def refresh_access_token(refresh_token: str):
    """Refresh access token using refresh token."""
    if refresh_token not in refresh_tokens_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )
    
    token_data = refresh_tokens_db[refresh_token]
    username = token_data["username"]
    
    # Create new access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logout")
async def logout(refresh_token: str, current_user: User = Depends(get_current_active_user)):
    """Logout and invalidate refresh token."""
    if refresh_token in refresh_tokens_db:
        del refresh_tokens_db[refresh_token]
    return {"message": "Successfully logged out"}
```

### 2. Role-Based Access Control

```python
from enum import Enum
from typing import List

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"

class UserWithRoles(User):
    roles: List[Role] = []

def create_access_token_with_roles(username: str, roles: List[Role], expires_delta: Optional[timedelta] = None):
    """Create JWT token with roles."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode = {
        "sub": username,
        "exp": expire,
        "roles": [role.value for role in roles]
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user_with_roles(token: str = Depends(oauth2_scheme)):
    """Get current user with roles from JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        roles: List[str] = payload.get("roles", [])
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username=username)
    if user is None:
        raise credentials_exception
    
    user_with_roles = UserWithRoles(**user.dict(), roles=[Role(role) for role in roles])
    return user_with_roles

def require_roles(required_roles: List[Role]):
    """Dependency to require specific roles."""
    def role_checker(current_user: UserWithRoles = Depends(get_current_user_with_roles)):
        if not any(role in current_user.roles for role in required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return current_user
    return role_checker

# Usage
@app.get("/admin-only")
async def admin_only_route(current_user: UserWithRoles = Depends(require_roles([Role.ADMIN]))):
    return {"message": "This is an admin-only route", "user": current_user.username}

@app.get("/moderator-or-admin")
async def mod_or_admin_route(
    current_user: UserWithRoles = Depends(require_roles([Role.ADMIN, Role.MODERATOR]))
):
    return {"message": "This route requires moderator or admin role"}
```

### 3. JWT with Database Integration

```python
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import func

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

def get_db():
    """Database dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_username(db: Session, username: str):
    """Get user by username from database."""
    return db.query(UserDB).filter(UserDB.username == username).first()

def create_user(db: Session, username: str, email: str, password: str):
    """Create new user in database."""
    hashed_password = get_password_hash(password)
    db_user = UserDB(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_current_user_from_db(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get current user from database using JWT token."""
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
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/register")
async def register_user(
    username: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    """Register new user."""
    # Check if user already exists
    if get_user_by_username(db, username):
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    # Create user
    user = create_user(db, username, email, password)
    return {"message": "User created successfully", "username": user.username}
```

## Security Best Practices

### 1. Environment Configuration

```python
import os
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "fallback-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
```

### 2. Environment Variables (.env file)

```env
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### 3. Security Headers Middleware

```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "*.yourdomain.com"]
)

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
```

### 4. Rate Limiting

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/token")
@limiter.limit("5/minute")  # 5 login attempts per minute
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # ... login logic
    pass
```

## Testing JWT Authentication

### 1. Test Setup

```python
import pytest
from fastapi.testclient import TestClient
from jose import jwt
from datetime import datetime, timedelta

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpassword"
    }

@pytest.fixture
def access_token():
    """Create a test access token."""
    token_data = {
        "sub": "testuser",
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
```

### 2. Authentication Tests

```python
def test_login_success(client, test_user):
    """Test successful login."""
    response = client.post(
        "/token",
        data={"username": test_user["username"], "password": test_user["password"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client):
    """Test login with invalid credentials."""
    response = client.post(
        "/token",
        data={"username": "wronguser", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_protected_route_with_token(client, access_token):
    """Test accessing protected route with valid token."""
    response = client.get(
        "/users/me/",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200

def test_protected_route_without_token(client):
    """Test accessing protected route without token."""
    response = client.get("/users/me/")
    assert response.status_code == 401

def test_protected_route_with_invalid_token(client):
    """Test accessing protected route with invalid token."""
    response = client.get(
        "/users/me/",
        headers={"Authorization": "Bearer invalid-token"}
    )
    assert response.status_code == 401
```

### 3. Integration Tests

```python
def test_full_authentication_flow(client):
    """Test complete authentication flow."""
    # Register user
    response = client.post(
        "/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword"
        }
    )
    assert response.status_code == 200
    
    # Login
    response = client.post(
        "/token",
        data={"username": "newuser", "password": "newpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Access protected route
    response = client.get(
        "/users/me/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"
```

## Common Pitfalls and Solutions

### 1. Token Storage on Frontend

```javascript
// Bad: localStorage (vulnerable to XSS)
localStorage.setItem('token', token);

// Better: httpOnly cookies (if possible)
// Set in backend:
response.set_cookie(
    key="access_token",
    value=token,
    httponly=True,
    secure=True,
    samesite="lax"
)

// Alternative: Secure localStorage with XSS protection
// Use Content Security Policy and sanitize all user input
```

### 2. Token Expiration Handling

```python
async def get_current_user_safe(token: str = Depends(oauth2_scheme)):
    """Safe user getter that handles expired tokens gracefully."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        exp: int = payload.get("exp")
        
        # Check if token is expired
        if exp and datetime.utcnow().timestamp() > exp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        # ... rest of validation
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token validation failed: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
```

### 3. Secret Key Management

```python
# Bad: Hardcoded secret
SECRET_KEY = "my-secret-key"

# Good: Environment variable
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is required")

# Better: Generate strong secret
import secrets
SECRET_KEY = secrets.token_urlsafe(32)  # Generate and store this
```

## Production Considerations

### 1. Use HTTPS Only
```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Redirect HTTP to HTTPS
app.add_middleware(HTTPSRedirectMiddleware)
```

### 2. Use Strong Secrets
- Generate secrets with at least 256 bits of entropy
- Use different secrets for different environments
- Rotate secrets regularly

### 3. Implement Token Blacklisting
```python
# Use Redis for token blacklist
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def blacklist_token(token: str, expires_in: int):
    """Add token to blacklist."""
    redis_client.setex(f"blacklist:{token}", expires_in, "1")

def is_token_blacklisted(token: str) -> bool:
    """Check if token is blacklisted."""
    return redis_client.exists(f"blacklist:{token}")
```

### 4. Monitor and Log
```python
import logging

logger = logging.getLogger(__name__)

async def get_current_user_with_logging(token: str = Depends(oauth2_scheme)):
    try:
        # ... validation logic
        logger.info(f"User {username} authenticated successfully")
        return user
    except JWTError as e:
        logger.warning(f"JWT validation failed: {str(e)}")
        raise HTTPException(...)
```

## Use cases may include:
1. JWTs, or JSON Web Tokens, are primarily used for authentication and authorization in modern web applications and APIs. After a user successfully logs in with their credentials, the server generates a JWT and sends it to the client.
2. The client then includes this token in the header of every subsequent request to access protected routes or resources. The server can verify the token's signature to authenticate the request without needing to query a database for user session information, making it a stateless and scalable solution. Another key use case is secure information exchange.
3. Since JWTs can be signed and encrypted, they provide a compact and verified way to transmit information between parties, ensuring that the data is trustworthy and hasn't been tampered with during transit.

2025
