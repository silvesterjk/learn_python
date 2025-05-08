from fastapi import FastAPI
from database import engine
import models 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = SessionLocal()
pass

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/todos")
def read_todos():
    return {"todos": []}