""" Using SQLite with FastAPI """
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

class Book(BaseModel):
    title: str