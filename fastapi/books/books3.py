""" Using SQLite with FastAPI """
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Database connection
def get_db_connection():