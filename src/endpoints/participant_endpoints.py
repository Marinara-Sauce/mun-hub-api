from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.operations import participant_operations
from src.schemas import participant_schema

router = APIRouter()


# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/participants", tags=["Participants"])
def get_participants(db: Session = Depends(get_db)):
    return participant_operations.get_participants(db)


@router.get("/participants/{participant_id}", tags=["Participants"])
def get_participant_by_id(participant_id: str, db: Session = Depends(get_db)):
    return participant_operations.get_participant_by_id(db, participant_id)


@router.post("/participants", tags=["Participants"])
def create_participant(user: participant_schema.ParticipantCreate, db: Session = Depends(get_db)):
    return participant_operations.create_participant(db, user)
