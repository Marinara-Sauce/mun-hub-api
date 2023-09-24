from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
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
@router.post("/token", tags=["User"])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user: AdminUser = get_user_by_username(db, form_data.username)

    if not user:
        raise HTTPException(status_code=404, detail=(f"No users with the username {form_data.username}"))
    
    # check the password
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=403, detail=(f"Incorrect Password"))
    
    user.__delattr__("password")
    token = generate_token(user.user_id)
    return {"access_token": token, "token_type": "bearer", "expiration": 30, "user": user} # TODO: Not hard code the 30 minutes

