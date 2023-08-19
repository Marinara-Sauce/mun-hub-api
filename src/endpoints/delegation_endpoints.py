from fastapi import APIRouter, Depends

from src.database.database import SessionLocal
from src.schemas.delegation_schema import Delegation
from src.operations import delegation_operations

router = APIRouter()


# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all delegations
@router.get("/delegations", tags=["Delegations"])
def get_delegations(db=Depends(get_db)):
    return delegation_operations.get_delegations(db)


# Get delegations by ID
@router.get("/delegations/{delegation_id}", tags=["Delegations"])
def get_delegations_by_id(delegation_id: str, db=Depends(get_db)):
    result = delegation_operations.get_delegate_by_id(db, delegation_id)

    if result is None:
        return {"message": f"Delegation ID [{delegation_id}] not found"}
    else:
        return result


# Create a delegation
@router.post("/delegations", tags=["Delegations"])
def create_delegation(delegation: Delegation, db=Depends(get_db)):
    return delegation_operations.create_delegation(db, delegation)


# Update a delegation
@router.put("/delegations/{delegation_id}", tags=["Delegations"])
def update_delegation(delegation_id: str, new_delegation_name: str, db=Depends(get_db)):
    result = delegation_operations.update_delegation(db, delegation_id, new_delegation_name)

    if result is None:
        return {"message": f"Delegation ID [{delegation_id}] not found"}
    else:
        return result
