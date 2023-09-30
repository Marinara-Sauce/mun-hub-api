from typing import List, Optional
from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from src.schemas.workingpaper_schema import WorkingPaperCreate, WorkingPaper

from src.models.models import Committee, CommitteePollingTypes, Participant, WorkingPaper
from src.schemas.committee_schema import CommitteeCreate, CommitteeUpdate


def get_committees(db: Session):
    return db.query(Committee).all()


def create_committee(db: Session, user: CommitteeCreate):
    db_user = Committee(
        committee_name=user.committee_name, 
        committee_abbreviation=user.committee_abbreviation
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_committee_by_id(db: Session, committee_id: str) -> Optional[Committee]:
    """
    Get a committee by its id.

    :param db: Database session object
    :param committee_id: ID of the committee
    :return: The committee, if it exists, otherwise None
    """
    return db.query(Committee).filter(Committee.committee_id == committee_id).first()


def patch_committee(db: Session, committee_update: CommitteeUpdate) -> Optional[Committee]:
    old_committee = get_committee_by_id(db, committee_update.committee_id)
    
    if old_committee is None:
        return False
    
    for key, value in committee_update.model_dump().items():
        setattr(old_committee, key, value)
    
    db.commit()
    db.refresh(old_committee)
    
    return old_committee
    

def change_committee_poll(db: Session, committee_id: str, new_poll: CommitteePollingTypes):
    """
    Change the poll of a committee.

    :param db: Database session object
    :param committee_id: Committee object to change
    :param new_status: New poll for the community
    :return: True if successful, False otherwise
    """
    # try getting committee object
    committee = get_committee_by_id(db, committee_id)

    if committee is None:
        return False

    # update
    committee.committee_poll = new_poll

    # commit
    db.commit()
    
    return True


def delete_committee(db: Session, committee_id: str):
    committee = db.query(Committee).filter(Committee.committee_id == committee_id).first()
    
    if committee is None:
        return False
    
    db.delete(committee)
    db.commit()

    return True


# get participants
def get_participants(db: Session):
    return db.query(Participant).all()


# get participant by ID
def get_participant_by_id(db: Session, participant_id: str) -> Optional[Participant]:
    return db.query(Participant).filter(Participant.participant_id == participant_id).first()


# add many delegations to a single committee
def add_participants(db: Session, committee_id: int, delegation_ids: [int]) -> [Participant]:
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
    
    return True


# add a working paper to a committee
def add_working_paper(db: Session, working_paper: WorkingPaperCreate) -> Optional[WorkingPaper]:

    db_working_paper = WorkingPaper(
        committee_id = working_paper.committee_id,
        working_group_name = working_paper.working_group_name,
        paper_link = working_paper.paper_link,
    )

    db.add(db_working_paper)
    db.commit()

    return db_working_paper
