import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONTAINER_DATABASE_URL = "postgresql://postgres:Password123@db/mun"
LOCAL_DATABASE_URL = "postgresql://postgres:Password123@localhost:5432/mun"

engine = create_engine(
    CONTAINER_DATABASE_URL if os.getenv("CONTAINERIZED") else LOCAL_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()