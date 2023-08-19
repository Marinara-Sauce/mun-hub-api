from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.models.models import CommitteeSessionTypes
from src.schemas import committee_schema
from src.operations import committee_operations

router = APIRouter()


# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all
@router.get("/committees", tags=["Committees"])
def get_committees(db: Session = Depends(get_db)) -> Optional[list[committee_schema.Committee]]:
    return committee_operations.get_committees(db)


# Get by ID
@router.get("/committees/{committee_id}", tags=["Committees"])
def get_committee_by_id(committee_id: str, db: Session = Depends(get_db)) -> Optional[committee_schema.Committee]:
    result = committee_operations.get_committee_by_id(db, committee_id)

    # check for valid result
    if committee_id is None:
        raise HTTPException(status_code=404, detail=f"Committee of ID {committee_id} not found.")
    else:
        return result


# Create
@router.post("/committees", tags=["Committees"])
def create_committee(committee: committee_schema.CommitteeCreate, db: Session = Depends(get_db)):
    return committee_operations.create_committee(db, committee)


# Change description
@router.put("/committees/{committee_id}/description", tags=["Committees"])
def change_committee_description(committee_id: str, new_description: str, db: Session = Depends(get_db)):
    response = committee_operations.change_committee_description(db, committee_id, new_description)

    # check for valid change
    if response:
        return {"message": "Description changed."}
    else:
        raise HTTPException(status_code=404, detail=f"Committee of ID {committee_id} not found.")


# change status
@router.put("/committees/{committee_id}/status", tags=["Committees"])
def change_committee_status(committee_id: str, new_status: CommitteeSessionTypes, db: Session = Depends(get_db)):
    response = committee_operations.change_committee_status(db, committee_id, new_status)

    # check for valid change
    if response:
        return {"message": "Status changed."}
    else:
        raise HTTPException(status_code=404, detail=f"Committee of ID {committee_id} not found.")
