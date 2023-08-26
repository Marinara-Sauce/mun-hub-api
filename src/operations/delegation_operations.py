from typing import Optional

from src.models.models import Delegation
DELEGATION_ID_PREFIX = "DELEGATION"

from sqlalchemy.orm import Session

from src.database.create_id import create_id

from src.schemas.delegation_schema import DelegationCreate


def get_delegations(db: Session) -> list[Delegation]:
    return db.query(Delegation).all()


def get_delegate_by_id(db: Session, delegation_id: str) -> Optional[Delegation]:
    return db.query(Delegation).filter(Delegation.delegation_id == delegation_id).first()


def create_delegation(db: Session, user: DelegationCreate) -> Delegation:
    db_user = Delegation(delegation_id=create_id(DELEGATION_ID_PREFIX),
                         delegation_name=user.delegation_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_delegation(db: Session, delegation_id: str, new_delegation_name: str) -> Optional[Delegation]:
    db_user = db.query(Delegation).filter(Delegation.delegation_id == delegation_id).first()

    # check for no valid Delegation
    if db_user is None:
        return None

    db_user.delegation_name = new_delegation_name
    db.commit()
    db.refresh(db_user)
    return db_user
