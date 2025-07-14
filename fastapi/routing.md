# FastAPI APIRouter

## What is APIRouter?

APIRouter is a class in FastAPI that allows you to organize and modularize your API endpoints into separate files and logical groups. It's essentially a mini FastAPI application that can be included in your main application.

## Why Use APIRouter?

### Code Organization
- **Separation of Concerns**: Group related endpoints together
- **Modularity**: Split large applications into smaller, manageable modules
- **Team Collaboration**: Different developers can work on different routers
- **Maintainability**: Easier to locate and modify specific functionality

### Scalability
- **Reusability**: Routers can be reused across different applications
- **Testing**: Individual routers can be tested in isolation
- **Deployment**: Easier to enable/disable specific feature sets

## Basic Usage

### Creating a Router

```python
from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes using the router
@router.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]

@router.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}
```

### Including Router in Main App

```python
from fastapi import FastAPI
from .routers import items  # Import your router module

app = FastAPI()

# Include the router
app.include_router(items.router)
```

## Router Configuration Options

### Prefix
Add a common prefix to all routes in the router:

```python
router = APIRouter(prefix="/api/v1")

@router.get("/items/")  # Actual path: /api/v1/items/
async def read_items():
    return {"message": "Items"}
```

### Tags
Group endpoints for OpenAPI documentation:

```python
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")  # Will be tagged as "users" in docs
async def get_users():
    return {"users": []}
```

### Dependencies
Apply dependencies to all routes in the router:

```python
from fastapi import Depends

def common_dependency():
    return {"message": "This dependency runs for all routes"}

router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(common_dependency)]
)
```

### Response Models
Set default response models:

```python
from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str

router = APIRouter(
    prefix="/items",
    responses={404: {"description": "Not found"}}
)
```

## Advanced Router Features

### Nested Routers
You can include routers within other routers:

```python
# sub_router.py
sub_router = APIRouter(prefix="/sub")

@sub_router.get("/endpoint")
async def sub_endpoint():
    return {"message": "Sub endpoint"}

# main_router.py
main_router = APIRouter(prefix="/main")
main_router.include_router(sub_router)

# Final path: /main/sub/endpoint
```

### Router with Custom Classes

```python
class ItemsRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/items", tags=["items"])
        self._setup_routes()
    
    def _setup_routes(self):
        self.router.add_api_route("/", self.get_items, methods=["GET"])
        self.router.add_api_route("/{item_id}", self.get_item, methods=["GET"])
    
    async def get_items(self):
        return {"items": []}
    
    async def get_item(self, item_id: int):
        return {"item_id": item_id}

# Usage
items_handler = ItemsRouter()
app.include_router(items_handler.router)
```

## Real-World Example Structure

### Project Structure
```
app/
├── main.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── users.py
│   ├── items.py
│   └── admin.py
├── models/
├── dependencies/
└── database.py
```

### auth.py Router
```python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={401: {"description": "Unauthorized"}}
)

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: UserLogin):
    # Authentication logic
    return {"access_token": "fake-token", "token_type": "bearer"}

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}
```

### users.py Router
```python
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user)]  # Apply to all routes
)

class User(BaseModel):
    id: int
    username: str
    email: str

@router.get("/", response_model=List[User])
async def get_users():
    return []

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return {"id": user_id, "username": "john", "email": "john@example.com"}

@router.post("/", response_model=User)
async def create_user(user: User):
    return user
```

### main.py
```python
from fastapi import FastAPI
from .routers import auth, users, items, admin

app = FastAPI(title="My API", version="1.0.0")

# Include all routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/api/v1",  # Additional prefix
    dependencies=[Depends(verify_admin)]  # Additional dependencies
)
```

## Best Practices

### 1. Logical Grouping
Group related functionality together:
- `/auth` - Authentication and authorization
- `/users` - User management
- `/items` - Item operations
- `/admin` - Administrative functions

### 2. Consistent Naming
```python
# Good
router = APIRouter(prefix="/users", tags=["users"])

# Better - use plural for collections
@router.get("/")  # GET /users/
@router.get("/{user_id}")  # GET /users/123
```

### 3. Use Dependencies Wisely
```python
# Apply common dependencies at router level
router = APIRouter(
    dependencies=[Depends(verify_authentication)]
)

# Add specific dependencies to individual routes
@router.get("/admin-only", dependencies=[Depends(verify_admin)])
async def admin_endpoint():
    pass
```

### 4. Version Your APIs
```python
v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

app.include_router(v1_router)
app.include_router(v2_router)
```

### 5. Error Handling
```python
from fastapi import HTTPException

router = APIRouter(
    responses={
        404: {"description": "Item not found"},
        400: {"description": "Bad request"}
    }
)

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Invalid item ID")
    # ... rest of the logic
```

## Common Patterns

### 1. CRUD Router Pattern
```python
class CRUDRouter:
    def __init__(self, model_name: str, prefix: str):
        self.router = APIRouter(prefix=prefix, tags=[model_name])
        self.model_name = model_name
        self._setup_crud_routes()
    
    def _setup_crud_routes(self):
        self.router.add_api_route("/", self.create, methods=["POST"])
        self.router.add_api_route("/", self.read_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.read, methods=["GET"])
        self.router.add_api_route("/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete, methods=["DELETE"])
```

### 2. Middleware on Routers
```python
from fastapi import Request
import time

@router.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

`@router.middleware` is a decorator that allows you to add middleware to a specific router, rather than applying it to your entire FastAPI application. It's a way to run code before and/or after the route handlers in that particular router are executed.

## How Router Middleware Works

```python
from fastapi import APIRouter, Request, Response
import time

router = APIRouter(prefix="/api")

@router.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # Code that runs BEFORE the route handler
    start_time = time.time()
    
    # Call the actual route handler
    response = await call_next(request)
    
    # Code that runs AFTER the route handler
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    
    return response

@router.get("/users/")
async def get_users():
    return {"users": []}
```

## Key Characteristics

**Scope**: Only affects routes within that specific router
**Execution Order**: Runs for every request to routes in that router
**Parameters**: 
- `request`: The incoming request object
- `call_next`: A function that calls the actual route handler

    ## Common Use Cases
    
    ### 1. Logging Router-Specific Activity
    ```python
    import logging
    
    @router.middleware("http")
    async def log_api_requests(request: Request, call_next):
        logger = logging.getLogger("api_router")
        logger.info(f"API request: {request.method} {request.url}")
        
        response = await call_next(request)
        
        logger.info(f"API response: {response.status_code}")
        return response
    ```
    
    ### 2. Authentication for Router Groups
    ```python
    @router.middleware("http")
    async def verify_api_key(request: Request, call_next):
        api_key = request.headers.get("X-API-Key")
        
        if not api_key or not is_valid_api_key(api_key):
            return Response(
                content="Invalid API key",
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        response = await call_next(request)
        return response
    ```
    
    ### 3. Rate Limiting for Specific Routes
    ```python
    from collections import defaultdict
    from datetime import datetime, timedelta
    
    # Simple in-memory rate limiter (use Redis in production)
    request_counts = defaultdict(list)
    
    @router.middleware("http")
    async def rate_limit_middleware(request: Request, call_next):
        client_ip = request.client.host
        now = datetime.now()
        
        # Clean old requests (older than 1 minute)
        request_counts[client_ip] = [
            req_time for req_time in request_counts[client_ip]
            if now - req_time < timedelta(minutes=1)
        ]
        
        # Check if limit exceeded (max 10 requests per minute)
        if len(request_counts[client_ip]) >= 10:
            return Response(
                content="Rate limit exceeded",
                status_code=429,
                headers={"Retry-After": "60"}
            )
        
        # Add current request
        request_counts[client_ip].append(now)
        
        response = await call_next(request)
        return response
    ```
    
    ### 4. Adding CORS Headers for Specific API Versions
    ```python
    @router.middleware("http")
    async def add_cors_headers(request: Request, call_next):
        response = await call_next(request)
        
        response.headers["Access-Control-Allow-Origin"] = "https://myapp.com"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        
        return response
    ```
    
    ## Router Middleware vs App Middleware
    
    ### App-Level Middleware
    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.middleware("http")
    async def global_middleware(request: Request, call_next):
        # Runs for ALL routes in the entire application
        response = await call_next(request)
        return response
    ```
    
    ### Router-Level Middleware
    ```python
    router = APIRouter()
    
    @router.middleware("http")
    async def router_specific_middleware(request: Request, call_next):
        # Only runs for routes in THIS router
        response = await call_next(request)
        return response
    ```
    
    ## Multiple Middlewares and Execution Order
    
    ```python
    # First middleware (outermost)
    @router.middleware("http")
    async def first_middleware(request: Request, call_next):
        print("First middleware - before")
        response = await call_next(request)
        print("First middleware - after")
        return response
    
    # Second middleware (inner)
    @router.middleware("http")
    async def second_middleware(request: Request, call_next):
        print("Second middleware - before")
        response = await call_next(request)
        print("Second middleware - after")
        return response
    
    @router.get("/test")
    async def test_route():
        print("Route handler")
        return {"message": "test"}
    
    # Execution order:
    # 1. First middleware - before
    # 2. Second middleware - before  
    # 3. Route handler
    # 4. Second middleware - after
    # 5. First middleware - after
    ```
    
    ## Error Handling in Router Middleware
    
    ```python
    @router.middleware("http")
    async def error_handling_middleware(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ValueError as e:
            return Response(
                content=f"Value error: {str(e)}",
                status_code=400
            )
        except Exception as e:
            return Response(
                content="Internal server error",
                status_code=500
            )
    ```
    
    ## Real-World Example: Admin Router with Middleware
    
    ```python
    admin_router = APIRouter(prefix="/admin", tags=["admin"])
    
    @admin_router.middleware("http")
    async def admin_auth_middleware(request: Request, call_next):
        # Check if user is admin
        token = request.headers.get("Authorization")
        if not token or not verify_admin_token(token):
            return Response(
                content="Admin access required",
                status_code=403
            )
        
        response = await call_next(request)
        return response
    
    @admin_router.middleware("http")
    async def admin_audit_middleware(request: Request, call_next):
        # Log all admin actions
        user_id = get_user_from_token(request.headers.get("Authorization"))
        log_admin_action(user_id, request.method, request.url)
        
        response = await call_next(request)
        return response
    
    @admin_router.get("/users")
    async def get_all_users():
        # This will only run after both middlewares pass
        return {"users": get_all_users_from_db()}
    ```
    
    ## When to Use Router Middleware
    
    **Good for:**
    - Router-specific authentication/authorization
    - Feature-specific logging or monitoring
    - API version-specific behavior
    - Route group rate limiting
    - Adding headers for specific API sections
    
    **Avoid for:**
    - Global concerns (use app middleware instead)
    - Heavy computational tasks (consider dependencies)
    - Database operations that could fail (use dependencies with proper error handling)
    
    The key advantage is that router middleware gives you fine-grained control over which routes get which middleware, without affecting your entire application.

## Testing Routers

### Unit Testing Individual Routers
```python
from fastapi.testclient import TestClient
from fastapi import FastAPI
from myapp.routers.users import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []
```

### Integration Testing
```python
def test_full_user_workflow():
    # Create user
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "test@example.com"
    })
    assert response.status_code == 201
    user_id = response.json()["id"]
    
    # Get user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
```
