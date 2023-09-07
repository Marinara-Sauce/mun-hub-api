from typing import Optional

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
    """
    Return the entire speaker list

    :param speakerlist_id: SpeakerList ID
    :param db: Database object
    :return: A list of SpeakerListEntry objects
    """
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # return all speakerlist entries
    result = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first

    if result is None:
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")
    else:
        return result.speakerlist_entries


# pop
@router.get("/speakerlist/get_next/{speakerlist_id}", tags=["Speaker List"])
def get_next_speaker(speakerlist_id: str, db: Session = Depends(get_db)) -> Optional[SpeakerListEntry]:
    """
    Get the next speaker on the list and remove it from the list

    :param speakerlist_id: SpeakerList ID
    :param db: Database object
    :return: The next to speak, if any.
    """
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # get speakerlist
    speakerlist = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # check if speakerlist is empty
    if len(speakerlist.speakerlist_entries) == 0:
        return None

    # get next speaker
    next_speaker = speakerlist.speakerlist_entries[0]

    # remove speaker from list
    speakerlist.speakerlist_entries.remove(next_speaker)

    # commit changes
    db.commit()

    return next_speaker


# randomize speaker's list
@router.get("/speakerlist/randomize/{speakerlist_id}", tags=["Speaker List"])
def randomize_speakerlist(speakerlist_id: str, db: Session = Depends(get_db)):
    """
    Randomize the speakerlist

    :param speakerlist_id: SpeakerList ID
    :param db: Database object
    :return: None
    """
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # get speakerlist
    speakerlist = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # randomize speakerlist
    import random
    random.shuffle(speakerlist.speakerlist_entries)

    # commit changes
    db.commit()

    return None

# add user to speaker list
@router.post("/speakerlist/add_user/{speakerlist_id}/{participant_id}", tags=["Speaker List"])
def add_user_to_speakerlist(speakerlist_id: str, participant_id: str, db: Session = Depends(get_db)):
    """
    Add a user to the speakerlist

    :param speakerlist_id: SpeakerList ID
    :param participant_id: Participant ID
    :param db: Database object
    :return: None
    """
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # check for valid participant
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Participant of ID {participant_id} not found.")

    # get speakerlist
    speakerlist = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # get participant
    participant = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # create speakerlist entry
    speakerlist_entry = SpeakerListEntry(speakerlist=speakerlist.speakerlist_id, participant=participant.participant_id)

    # add participant to speakerlist
    speakerlist.speakerlist_entries.append(speakerlist_entry)

    # commit changes
    db.commit()

    return None

@router.delete("/speakerlist/remove_user/{speakerlist_id}/{participant_id}", tags=["Speaker List"])
def remove_user_from_speakerlist(speakerlist_id: str, participant_id: str, db: Session = Depends(get_db)):
    """
    Remove a user from the speakerlist

    :param speakerlist_id: SpeakerList ID
    :param participant_id: Participant ID
    :param db: Database object
    :return: None
    """
    # check for valid speakerlist
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Speakerlist of ID {speakerlist_id} not found.")

    # check for valid participant
    if not db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first():
        raise HTTPException(status_code=404, detail=f"Participant of ID {participant_id} not found.")

    # get speakerlist
    speakerlist = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # get participant
    participant = db.query(SpeakerList).filter(SpeakerList.speakerlist_id == speakerlist_id).first()

    # remove participant from speakerlist
    speakerlist.speakerlist_entries.remove(participant)

    # commit changes
    db.commit()

    return None