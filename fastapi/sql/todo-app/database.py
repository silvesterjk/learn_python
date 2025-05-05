from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DB_URL = 'sqlite:///./todos.db'

engine = create_engine(SQL_ALCHEMY_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # This is to create a database session and the variables are used to create a database session.

Base = declarative_base()