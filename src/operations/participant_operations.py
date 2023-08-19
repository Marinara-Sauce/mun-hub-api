from typing import Optional

from src.schemas.committee_schema import Committee

PARTICIPANT_ID_PREFIX = "PARTICIPANT"

from sqlalchemy.orm import Session

from src.database.create_id import create_id
from src.models.models import Participant
from src.schemas import participant_schema


# get participants
def get_participants(db: Session):
    return db.query(Participant).all()


# get participant by ID
def get_participant_by_id(db: Session, participant_id: str) -> Optional[Participant]:
    return db.query(Participant).filter(Participant.participant_id == participant_id).first()


# create participant
def create_participant(db: Session, user: participant_schema.ParticipantCreate) -> Optional[Participant]:
    # check for valid committee
    if not db.query(Committee).filter(Committee.committee_id == user.committee_id).first():
        return None

    # check for valid delegation
    if not db.query(Committee).filter(Committee.committee_id == user.delegation_id).first():
        return None

    # TODO: Check valid country code

    # create participant
    db_user = Participant(participant_id=create_id(PARTICIPANT_ID_PREFIX), committee_id=user.committee_id,
                          delegation_id=user.delegation_id, country_code=user.country_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
