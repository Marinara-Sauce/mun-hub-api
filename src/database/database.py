import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_PROD_DATABASE_URL = "sqlite:///./db/prod_hub.db"
SQLALCHEMY_DEV_DATABASE_URL = "postgresql://admin:password123@db/hub"

engine = create_engine(
    SQLALCHEMY_PROD_DATABASE_URL if os.getenv("ENVIRONMENT") == "production" else SQLALCHEMY_DEV_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()