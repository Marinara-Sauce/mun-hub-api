from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from src.operations.authentication import generate_token, verify_password

from src.database.database import SessionLocal
from src.operations.user_operations import get_user_by_username
from src.schemas.user_schema import AdminUser

router = APIRouter()

# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# attempt a login
@router.post("/user", tags=["User"])
def login(username: str, password: str, db: Session = Depends(get_db)) -> Optional[str]:
    user: AdminUser = get_user_by_username(db, username)

    if not user:
        raise HTTPException(status_code=404, detail=(f"No users with the username {username}"))
    
    # check the password
    if not verify_password(password, user.password):
        raise HTTPException(status_code=403, detail=(f"Incorrect Password"))
    
    token = generate_token(user.user_id)
    return token

