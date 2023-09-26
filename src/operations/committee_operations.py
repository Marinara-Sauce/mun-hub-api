from typing import Optional

from sqlalchemy.orm import Session

from src.models.models import Committee, CommitteePollingTypes, CommitteeSessionTypes
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