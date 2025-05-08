from fastapi import FastAPI, Depends, HTTPException, Path, status, Body
from database import engine, SessionLocal
from models import Todos, Base
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

annotated_db = Annotated[Session, Depends(get_db)] # Depends is to get the database session

class TodoRequest(BaseModel):
    title: str = Field(..., min_length=3) # ... means that the field is required
    description: str = Field(..., min_length=3) # ... means that the field is required
    priority: int = Field(gt=0, le=5) # gt means greater than and le means less than
    complete: bool

@app.get("/")
async def read_all(db: annotated_db):
    return db.query(Todos).all()

@app.get("/get_todo/{todo_id}")
async def read_all_todo(db: annotated_db, todo_id: int = Path(gt=0)):
    todo_model= db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_model

@app.post("/create_todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: annotated_db, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()
    return todo_model

@app.put("/update_todo/{todo_id}")
async def update_todo(db: annotated_db, todo_id: int = Path(gt=0), todo_request: TodoRequest = Body(...)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()
    return todo_model

@app.delete("/delete_todo/{todo_id}")
async def delete_todo(db: annotated_db, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first() # First is used to get the first record
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()
    return todo_model
