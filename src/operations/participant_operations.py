from typing import Optional
from sqlalchemy.orm import Session
from src.models.models import Committee, Participant
from fastapi import HTTPException, status

# get participants
def get_participants(db: Session):
    return db.query(Participant).all()


# get participant by ID
def get_participant_by_id(db: Session, participant_id: str) -> Optional[Participant]:
    return db.query(Participant).filter(Participant.participant_id == participant_id).first()


# add many delegations to a single committee
def create_multiple_participants(db: Session, committee_id: int, delegation_ids: [int]) -> [Participant]:
    if not db.query(Committee).filter(Committee.committee_id == committee_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Commitee {committee_id} Not Found"
        )
    
    participants = [Participant(committee_id=committee_id, delegation_id=d) for d in delegation_ids]
    
    db.add_all(participants) # TODO: Catch unique errors
    db.commit()

    return participants


# remove a delegation from a committee
def remove_participant(db: Session, committee_id: int, delegation_id: int) -> bool:
    participant = db.query(Participant).filter(Participant.committee_id == committee_id).filter(Participant.delegation_id == delegation_id).first()

    if participant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find delegation with id: {delegation_id} in committee: {committee_id}"
        )
    
    db.delete(participant)
    db.commit()
    
    return participant