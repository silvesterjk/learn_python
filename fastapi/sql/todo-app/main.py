from fastapi import FastAPI, Depends, HTTPException, Path
from database import engine, SessionLocal
from models import Todos, Base
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

annotated_db = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: annotated_db):
    return db.query(Todos).all()

@app.get("/get_todo/{todo_id}")
async def read_all_todo(db: annotated_db, todo_id: int = Path(gt=0)):
    todo_model= db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_model