from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# Engine is the interface to the database
# connect_args={'check_same_thread': False}: This is only needed for SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# SessionLocal is a factory for creating new database sessions
# autocommit=False: Transactions are not automatically committed to the database
# autoflush=False: Changes are not automatically flushed to the database
# bind=engine: The engine is the interface to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the base class for all models
Base = declarative_base()