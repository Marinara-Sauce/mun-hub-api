from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.schemas.speakerlist_schema import SpeakerList, SpeakerListEntry

SPEAKERLIST_ID_PREFIX = "SPEAKERLIST"

router = APIRouter()


# get database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create
@router.get("/speakerlist/get_entries/{speakerlist_id}", tags=["Speaker List"])
def get_speakerlist_contents(speakerlist_id: str, db: Session = Depends(get_db)) -> list[SpeakerListEntry]:
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # return all speakerlist entries
    result = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first

    if result is None:
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")
    else:
        return result.speakerlist_entries
