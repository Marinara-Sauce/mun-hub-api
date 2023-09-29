from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.models import AdminUser
from src.operations.authentication import get_current_user

from src.database.database import SessionLocal
from src.operations import participant_operations

router = APIRouter()


# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



