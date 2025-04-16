""" Using SQLite with FastAPI """
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Database connection
def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()