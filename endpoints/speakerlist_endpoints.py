from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal
from schemas.speakerlist_schema import SpeakerList

SPEAKERLIST_ID_PREFIX = "SPEAKERLIST"


# get database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create
def get_speakerlist_contents(speakerlist_id: str, db: Session = Depends(get_db)):
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # return all speakerlist entries
    for entry in db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).all():

