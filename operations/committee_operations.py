from typing import Optional

from sqlalchemy.orm import Session

from database.create_id import create_id
from models.models import Committee, CommitteeSessionTypes
from schemas.committee_schema import CommitteeCreate

COMMITTEE_ID_PREFIX = "COMMITTEE"


def get_committees(db: Session):
    return db.query(Committee).all()


def create_committee(db: Session, user: CommitteeCreate):
    db_user = Committee(committee_id=create_id(COMMITTEE_ID_PREFIX),
                        country_alpha_2=user.country_alpha_2)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_committee(db: Session, committee_id: str):
    # verify that the committee exists
    if db.query(Committee).filter(Committee.committee_id == committee_id).first().rowcount == 0:
        raise Exception("Committee does not exist. [committee_id=" + committee_id + "]")

    # delete element
    q = db.query(Committee).filter(Committee.committee_id == committee_id).delete()

    # check for success
    if q.rowcount == 0:
        db.rollback()
        raise Exception("Delete failed." + q)
    else:
        db.commit()


def get_committee_by_id(db: Session, committee_id: str) -> Optional[Committee]:
    """
    Get a committee by its id.

    :param db: Database session object
    :param committee_id: ID of the committee
    :return: The committee, if it exists, otherwise None
    """
    return db.query(Committee).filter(Committee.committee_id == committee_id).first()


def change_committee_description(db: Session, committee_id: str, new_description: str) -> bool:
    """
    Change the description of a committee.

    :param db: Database session object
    :param committee_id: Committee object to change
    :param new_description: New description of the committee
    :return: True if successful, False otherwise
    """
    # try getting committee object
    committee = get_committee_by_id(db, committee_id)

    if committee is None:
        return False

    # update
    committee.committee_description = new_description

    # commit
    db.commit()


def change_committee_status(db: Session, committee_id: str, new_status: CommitteeSessionTypes):
    """
    Change the status of a committee.

    :param db: Database session object
    :param committee_id: Committee object to change
    :param new_status: New status of the committee
    :return: True if successful, False otherwise
    """
    # try getting committee object
    committee = get_committee_by_id(db, committee_id)

    if committee is None:
        return False

    # update
    committee.committee_status = new_status

    # commit
    db.commit()